#!/usr/bin/env python3
"""
Efecte Community Scraper

Scrapar forum-innehåll från community.efecte.com (kräver inloggning).

Användning:
    # Första gången - logga in och spara cookies:
    EFECTE_EMAIL=din@email.com EFECTE_PASSWORD=xxx python3 scraper_efecte.py --login

    # Scrapa allt innehåll:
    python3 scraper_efecte.py --scrape

    # Inkrementell scraping (bara nytt):
    python3 scraper_efecte.py --incremental
"""

import os
import sys
import json
import time
import re
import logging
import hashlib
import requests
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, urljoin
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper_efecte.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Konfiguration
COOKIES_FILE = "efecte_cookies.json"
BASE_URL = "https://community.efecte.com"
OUTPUT_DIR = "documentation_efecte"
DELAY_BETWEEN_REQUESTS = 1  # sekunder


def create_slug(title: str) -> str:
    """Skapar en URL-vänlig slug från titel"""
    slug = title.lower()
    slug = slug.replace('å', 'a').replace('ä', 'a').replace('ö', 'o')
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug[:100]


def download_image(img_url: str, category_slug: str, article_slug: str) -> str:
    """Laddar ner en bild och returnerar lokalt filnamn"""
    try:
        # Skapa bilder-mapp
        img_folder = Path(OUTPUT_DIR) / category_slug / "images"
        img_folder.mkdir(parents=True, exist_ok=True)

        # Generera unikt filnamn baserat på URL
        url_hash = hashlib.md5(img_url.encode()).hexdigest()[:8]

        # Hämta filextension från URL
        parsed = urlparse(img_url)
        ext = os.path.splitext(parsed.path)[1] or '.jpg'
        if '?' in ext:
            ext = ext.split('?')[0]

        # Skapa filnamn
        filename = f"{article_slug}_{url_hash}{ext}"
        filepath = img_folder / filename

        # Ladda ner om filen inte finns redan
        if not filepath.exists():
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(img_url, headers=headers, timeout=15)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                logger.info(f"      📸 Bild: {filename}")

        return f"images/{filename}"
    except Exception as e:
        logger.warning(f"      ⚠️ Kunde inte ladda ner bild: {e}")
        return None


def save_cookies(context, filepath=COOKIES_FILE):
    """Spara cookies till fil"""
    cookies = context.cookies()
    with open(filepath, 'w') as f:
        json.dump(cookies, f, indent=2)
    logger.info(f"Cookies sparade till {filepath}")


def load_cookies(context, filepath=COOKIES_FILE):
    """Ladda cookies från fil"""
    if not os.path.exists(filepath):
        return False
    try:
        with open(filepath, 'r') as f:
            cookies = json.load(f)
        context.add_cookies(cookies)
        logger.info(f"Cookies laddade från {filepath}")
        return True
    except Exception as e:
        logger.warning(f"Kunde inte ladda cookies: {e}")
        return False


def login(email: str, password: str, headless: bool = False) -> bool:
    """
    Logga in på Efecte Community.

    Args:
        email: Inloggnings-email
        password: Lösenord
        headless: Kör utan synlig webbläsare

    Returns:
        True om inloggningen lyckades
    """
    logger.info("=" * 70)
    logger.info("EFECTE COMMUNITY LOGIN")
    logger.info("=" * 70)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            viewport={'width': 1280, 'height': 800}
        )
        page = context.new_page()

        try:
            # Navigera till login
            logger.info("Navigerar till login-sidan...")
            page.goto(f"{BASE_URL}/login", wait_until='networkidle')

            # Vänta på formulär
            page.wait_for_selector('input[name="email"]', timeout=10000)

            # Fyll i uppgifter
            logger.info(f"Fyller i email: {email}")
            page.locator('input[name="email"]').fill(email)
            page.locator('input[name="password"]').fill(password)

            # Klicka login
            logger.info("Klickar på Login...")
            page.locator('button.btn-login').click()

            # Vänta på respons
            time.sleep(2)

            # Kolla efter felmeddelande
            error_elem = page.locator('.error-message, .alert-error, [class*="error"]')
            if error_elem.count() > 0:
                error_text = error_elem.first.text_content()
                if 'invalid' in error_text.lower() or 'incorrect' in error_text.lower():
                    logger.error(f"Login-fel: {error_text}")
                    return False

            # Kolla om reCAPTCHA
            recaptcha = page.locator('iframe[src*="recaptcha"]')
            if recaptcha.count() > 0:
                logger.warning("reCAPTCHA detekterad - väntar på manuell lösning (120s)...")
                try:
                    page.wait_for_url(lambda url: 'login' not in url.lower(), timeout=120000)
                except PlaywrightTimeout:
                    logger.error("Timeout vid reCAPTCHA")
                    return False

            # Vänta på redirect
            try:
                page.wait_for_url(lambda url: 'login' not in url.lower(), timeout=10000)
            except PlaywrightTimeout:
                logger.error("Fortfarande på login-sidan - inloggning misslyckades")
                page.screenshot(path='efecte_login_failed.png')
                return False

            logger.info(f"Inloggad! URL: {page.url}")
            save_cookies(context)
            return True

        except Exception as e:
            logger.error(f"Fel vid inloggning: {e}")
            page.screenshot(path='efecte_login_error.png')
            return False

        finally:
            browser.close()


def get_authenticated_page(playwright):
    """Skapa en autentiserad sida med sparade cookies"""
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    )

    if not load_cookies(context):
        raise Exception("Inga sparade cookies - kör --login först")

    page = context.new_page()
    return browser, context, page


def is_logged_in(page) -> bool:
    """Kontrollera om sessionen är aktiv"""
    page.goto(BASE_URL, wait_until='networkidle')
    return 'login' not in page.url.lower()


def discover_categories(page) -> list:
    """Hitta alla forum-kategorier"""
    logger.info("Letar efter kategorier...")
    page.goto(BASE_URL, wait_until='networkidle')

    categories = []

    # Efecte Community använder /category/ för kategorier
    links = page.locator('a[href*="/category/"]').all()

    for link in links:
        href = link.get_attribute('href')
        text = link.text_content().strip()
        if href and text:
            # Extrahera slug från URL
            slug = href.split('/category/')[-1].rstrip('/')
            full_url = href if href.startswith('http') else BASE_URL + href
            categories.append({
                'name': text if text else slug,
                'url': full_url,
                'slug': slug
            })

    # Ta bort dubbletter
    seen = set()
    unique_categories = []
    for cat in categories:
        if cat['url'] not in seen:
            seen.add(cat['url'])
            unique_categories.append(cat)

    logger.info(f"Hittade {len(unique_categories)} kategorier")
    return unique_categories


def discover_topics(page, category_url: str) -> list:
    """Hitta alla topics/trådar i en kategori"""
    logger.info(f"Hämtar topics från {category_url}")
    page.goto(category_url, wait_until='networkidle')

    topics = []

    # Efecte Community använder /t/ för topics
    links = page.locator('a[href*="/t/"]').all()

    for link in links:
        href = link.get_attribute('href')
        text = link.text_content().strip()
        if href and text and '/t/' in href:
            # Rensa bort query params och anchors
            clean_href = href.split('?')[0].split('#')[0]
            full_url = clean_href if clean_href.startswith('http') else BASE_URL + clean_href
            topics.append({
                'title': text,
                'url': full_url,
                'slug': create_slug(text)
            })

    # Ta bort dubbletter
    seen = set()
    unique_topics = []
    for topic in topics:
        if topic['url'] not in seen:
            seen.add(topic['url'])
            unique_topics.append(topic)

    logger.info(f"  Hittade {len(unique_topics)} topics")
    return unique_topics


def scrape_topic(page, topic_url: str, category_slug: str) -> dict:
    """Scrapa en enskild topic/tråd inklusive bilder"""
    logger.info(f"  Scrapar: {topic_url}")
    page.goto(topic_url, wait_until='networkidle')

    # Hämta titel - specifik selektor för Efecte/Forumbee
    title_elem = page.locator('h1.topic__title').first
    if title_elem.count() == 0:
        meta_title = page.locator('meta[property="og:title"]').first
        if meta_title.count() > 0:
            title = meta_title.get_attribute('content') or "Ingen titel"
        else:
            title = "Ingen titel"
    else:
        title = title_elem.text_content().strip()

    article_slug = create_slug(title)

    # Hämta bilder från inläggen
    images = []
    img_elements = page.locator('.post__body img, .topic__main img, .formatted img').all()
    for img in img_elements:
        src = img.get_attribute('src')
        if src:
            # Gör URL absolut
            if not src.startswith('http'):
                src = urljoin(BASE_URL, src)
            # Skippa avatarer och ikoner
            if 'avatar' not in src.lower() and 'icon' not in src.lower():
                local_path = download_image(src, category_slug, article_slug)
                if local_path:
                    images.append({'original': src, 'local': local_path})

    # Hämta HTML-innehåll för bättre formatering
    content_parts = []
    posts = page.locator('.post__body, .post-content, .message-body').all()
    for post in posts:
        # Hämta innerHTML för att bevara viss formatering
        html = post.inner_html()
        # Konvertera till text men behåll styckeindelning
        text = post.text_content().strip()
        if text and len(text) > 10:
            content_parts.append(text)

    if not content_parts:
        topic_body = page.locator('.topic__main, .topic-content').first
        if topic_body.count() > 0:
            content_parts.append(topic_body.text_content().strip())

    content = "\n\n".join(content_parts)

    # Lägg till bilder i markdown
    if images:
        content += "\n\n## Bilder\n\n"
        for img in images:
            content += f"![Bild]({img['local']})\n\n"

    # Hämta metadata - published_time
    published_date = ""
    meta_published = page.locator('meta[property="article:published_time"]').first
    if meta_published.count() > 0:
        published_date = meta_published.get_attribute('content') or ""

    # Hämta updated date
    updated_date = ""
    updated_elem = page.locator('[data-utc]').first
    if updated_elem.count() > 0:
        utc_ms = updated_elem.get_attribute('data-utc')
        if utc_ms:
            try:
                updated_date = datetime.fromtimestamp(int(utc_ms) / 1000).isoformat()
            except:
                pass

    author_elem = page.locator('.post__author, .author-name, .username').first
    author = author_elem.text_content().strip() if author_elem.count() > 0 else ""

    return {
        'title': title,
        'url': topic_url,
        'content': content,
        'published': published_date,
        'updated': updated_date,
        'author': author,
        'images': images,
        'scraped_at': datetime.now().isoformat()
    }


def save_article(article: dict, category_slug: str):
    """Spara artikel som markdown"""
    output_dir = Path(OUTPUT_DIR) / category_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    slug = create_slug(article['title'])
    filepath = output_dir / f"{slug}.md"

    # Skapa markdown med datum
    published = article.get('published', '')
    updated = article.get('updated', '')

    md_content = f"""# {article['title']}

**Källa:** {article['url']}
**Publicerad:** {published if published else 'Okänt'}
**Uppdaterad:** {updated if updated else 'Okänt'}
**Författare:** {article.get('author', 'Okänd')}

---

{article['content']}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)

    logger.info(f"    Sparad: {filepath}")
    return filepath


def save_index(category: dict, articles: list):
    """Spara index.json för en kategori"""
    output_dir = Path(OUTPUT_DIR) / category['slug']
    output_dir.mkdir(parents=True, exist_ok=True)

    index_data = {
        'category': category['name'],
        'url': category['url'],
        'updated': datetime.now().isoformat(),
        'article_count': len(articles),
        'articles': articles
    }

    with open(output_dir / 'index.json', 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)


def scrape_all():
    """Scrapa allt innehåll från Efecte Community"""
    logger.info("=" * 70)
    logger.info("EFECTE COMMUNITY SCRAPER")
    logger.info("=" * 70)

    if not os.path.exists(COOKIES_FILE):
        logger.error(f"Cookies saknas! Kör först: python3 scraper_efecte.py --login")
        return False

    with sync_playwright() as p:
        browser, context, page = get_authenticated_page(p)

        try:
            # Verifiera inloggning
            if not is_logged_in(page):
                logger.error("Session har gått ut - kör --login igen")
                return False

            logger.info("Session aktiv!")

            # Hitta kategorier
            categories = discover_categories(page)

            if not categories:
                logger.warning("Inga kategorier hittades - sparar huvudsidans HTML för debug")
                with open('efecte_debug.html', 'w', encoding='utf-8') as f:
                    f.write(page.content())
                return False

            stats = {'categories': 0, 'topics': 0, 'errors': 0}

            for category in categories:
                logger.info(f"\n📂 Kategori: {category['name']}")
                stats['categories'] += 1

                # Hitta topics
                topics = discover_topics(page, category['url'])
                time.sleep(DELAY_BETWEEN_REQUESTS)

                articles = []

                for topic in topics:
                    try:
                        article = scrape_topic(page, topic['url'], category['slug'])
                        save_article(article, category['slug'])
                        articles.append({
                            'title': article['title'],
                            'slug': create_slug(article['title']),
                            'url': article['url'],
                            'published': article.get('published', ''),
                            'updated': article.get('updated', '')
                        })
                        stats['topics'] += 1
                        time.sleep(DELAY_BETWEEN_REQUESTS)
                    except Exception as e:
                        logger.error(f"    Fel vid scraping av {topic['url']}: {e}")
                        stats['errors'] += 1

                # Spara kategori-index
                save_index(category, articles)

            # Spara master index
            master_index = {
                'source': 'Efecte Community',
                'url': BASE_URL,
                'scraped_at': datetime.now().isoformat(),
                'stats': stats,
                'categories': [{'name': c['name'], 'slug': c['slug'], 'url': c['url']} for c in categories]
            }

            with open(Path(OUTPUT_DIR) / 'master_index.json', 'w', encoding='utf-8') as f:
                json.dump(master_index, f, indent=2, ensure_ascii=False)

            logger.info("\n" + "=" * 70)
            logger.info("SAMMANFATTNING")
            logger.info("=" * 70)
            logger.info(f"  Kategorier: {stats['categories']}")
            logger.info(f"  Topics:     {stats['topics']}")
            logger.info(f"  Fel:        {stats['errors']}")
            logger.info("=" * 70)

            return True

        except Exception as e:
            logger.error(f"Fel vid scraping: {e}")
            return False

        finally:
            browser.close()


def main():
    if '--login' in sys.argv:
        email = os.environ.get('EFECTE_EMAIL')
        password = os.environ.get('EFECTE_PASSWORD')

        if not email or not password:
            print("❌ Miljövariabler saknas!")
            print("   EFECTE_EMAIL=din@email.com EFECTE_PASSWORD=xxx python3 scraper_efecte.py --login")
            sys.exit(1)

        headless = '--headless' in sys.argv
        success = login(email, password, headless=headless)
        sys.exit(0 if success else 1)

    elif '--scrape' in sys.argv or '--incremental' in sys.argv:
        success = scrape_all()
        sys.exit(0 if success else 1)

    else:
        print("Efecte Community Scraper")
        print("-" * 40)
        print("Användning:")
        print("  --login        Logga in och spara cookies")
        print("                 (kräver EFECTE_EMAIL och EFECTE_PASSWORD)")
        print("  --scrape       Scrapa allt innehåll")
        print("  --incremental  Inkrementell scraping")
        print("")
        print("Exempel:")
        print("  EFECTE_EMAIL=x EFECTE_PASSWORD=y python3 scraper_efecte.py --login")
        print("  python3 scraper_efecte.py --scrape")
        sys.exit(0)


if __name__ == '__main__':
    main()
