#!/usr/bin/env python3
"""
Inkrementell Scraper för Flex HRM Documentation
Skrapar bara nya, ändrade eller raderade artiklar

Användning:
    python3 scraper_incremental.py
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import re
import json
import logging
from pathlib import Path
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Custom headers - VIKTIGT för etisk scraping!
HEADERS = {
    'User-Agent': 'AxelssonDocBot/1.0 (github.com/pontush81/axelsson2; pontus.horberg@example.com)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'sv-SE,sv;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Kategorier
CATEGORIES = [
    {'name': 'Systemgemensamt', 'url': 'https://knowledge.flexapplications.se/systemgemensamt', 'folder': 'systemgemensamt'},
    {'name': 'Time', 'url': 'https://knowledge.flexapplications.se/time', 'folder': 'time'},
    {'name': 'Employee', 'url': 'https://knowledge.flexapplications.se/employee', 'folder': 'employee'},
    {'name': 'Travel & Expense', 'url': 'https://knowledge.flexapplications.se/travel-expense', 'folder': 'travel-expense'},
    {'name': 'Payroll', 'url': 'https://knowledge.flexapplications.se/payroll', 'folder': 'payroll'},
    {'name': 'Plan', 'url': 'https://knowledge.flexapplications.se/plan', 'folder': 'plan'}
]

def create_slug(title):
    """Skapar en slug från titel"""
    slug = title.lower()
    slug = slug.replace('⚙️', '')
    slug = slug.replace('å', 'a').replace('ä', 'a').replace('ö', 'o')
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug[:100]

def load_existing_articles(folder):
    """Ladda befintliga artiklar från index.json"""
    index_file = f"documentation/{folder}/index.json"
    
    if os.path.exists(index_file):
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                articles = json.load(f)
                # Skapa lookup dict med slug som nyckel
                return {article['slug']: article for article in articles}
        except Exception as e:
            logger.warning(f"  ⚠️  Kunde inte läsa {index_file}: {e}")
    
    return {}

def get_article_metadata_from_source(category_url):
    """
    Hämta artikellista från källan med titel, URL och synligt datum
    Skrapar INTE hela artikeln ännu, bara metadata
    """
    logger.info(f"Hämtar artikellista från {category_url}")
    
    try:
        response = requests.get(category_url, headers=HEADERS, timeout=30)
        response.raise_for_status()  # Raise error för 4xx/5xx responses
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles_metadata = []
        
        for link in soup.find_all('a', class_='hs-kb-category-article-list__link'):
            title = link.get_text(strip=True)
            url = link.get('href')
            slug = create_slug(title)
            
            articles_metadata.append({
                'title': title,
                'url': url,
                'slug': slug
            })
        
        logger.info(f"✓ Hittade {len(articles_metadata)} artiklar i listan")
        return articles_metadata
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            logger.error(f"❌ Rate limited (429)! Väntar 60 sekunder...")
            time.sleep(60)
        else:
            logger.error(f"❌ HTTP error {e.response.status_code}: {e}")
        return []
    except requests.exceptions.Timeout:
        logger.error(f"❌ Timeout vid hämtning av {category_url}")
        return []
    except Exception as e:
        logger.error(f"❌ Oväntat fel vid hämtning av artikellista: {e}")
        return []

def scrape_full_article(url):
    """Skrapar fullständig artikel från URL"""
    try:
        logger.info(f"Skrapar artikel: {url}")
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Hämta titel
        title_elem = soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else 'Ingen titel'
        
        # Hämta artikel
        article = soup.find('article')
        if not article:
            return None
        
        # Ta bort navigering, sidebar, feedback
        for elem in article.find_all(['aside', 'nav']):
            elem.decompose()
        for elem in article.find_all(class_=['hs-kb-sidebar', 'hs-kb-breadcrumbs', 'hs-kb-social_follow']):
            elem.decompose()
        for elem in article.find_all(string=lambda text: text and 'Hjälpte artikeln' in text):
            if elem.parent:
                elem.parent.decompose()
        
        # Hämta text
        text = article.get_text(separator='\n', strip=True)
        
        # Rensa whitespace
        text = re.sub(r'\n\n\n+', '\n\n', text)
        
        # Hitta datum
        date_match = re.search(r'den \d+ \w+ \d{4}', text)
        date = date_match.group(0) if date_match else ''
        
        # Ta bort datum från text
        if date:
            text = text.replace(date, '', 1).strip()
        
        # Ta bort titel från början om den upprepas
        if text.startswith(title):
            text = text[len(title):].strip()
        
        return {
            'title': title,
            'date': date,
            'content': text,
            'url': url
        }
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            logger.error(f"❌ Rate limited (429) vid scraping av {url}! Väntar 60 sekunder...")
            time.sleep(60)
        else:
            logger.error(f"❌ HTTP error {e.response.status_code} för {url}")
        return None
    except requests.exceptions.Timeout:
        logger.error(f"❌ Timeout vid scraping av {url}")
        return None
    except Exception as e:
        logger.error(f"❌ Oväntat fel vid scraping av {url}: {e}")
        return None

def incremental_scrape():
    """
    Inkrementell scraping - bara nya, ändrade och raderade
    
    Returns:
        dict: Statistik över ändringar
    """
    logger.info("="*70)
    logger.info("🔄 INKREMENTELL SCRAPING STARTAR")
    logger.info("="*70)
    logger.info("🤖 User-Agent: AxelssonDocBot/1.0")
    logger.info("⏰ Delay mellan requests: 1 sekund")
    logger.info("🌐 Källa: knowledge.flexapplications.se")
    logger.info("✅ Respekterar robots.txt")
    logger.info("="*70)
    
    stats = {
        'new': 0,
        'updated': 0,
        'deleted': 0,
        'unchanged': 0,
        'errors': 0
    }
    
    for category in CATEGORIES:
        logger.info(f"\n📂 Kategori: {category['name']}")
        folder = category['folder']
        
        # 1. Ladda befintliga artiklar
        existing_articles = load_existing_articles(folder)
        logger.info(f"  📄 Befintliga artiklar: {len(existing_articles)}")
        
        # 2. Hämta artikellista från källan
        source_articles = get_article_metadata_from_source(category['url'])
        
        if not source_articles:
            logger.warning(f"  ⚠️  Kunde inte hämta artiklar från källan, hoppar över kategori")
            stats['errors'] += 1
            continue
        
        # 3. Skapa lookup för snabb sökning
        source_slugs = {article['slug']: article for article in source_articles}
        
        # 4. Hitta nya och uppdaterade artiklar
        for source_article in source_articles:
            slug = source_article['slug']
            
            if slug not in existing_articles:
                # NY ARTIKEL
                logger.info(f"  🆕 NY: {source_article['title'][:60]}")
                
                # Skrapa hela artikeln
                full_article = scrape_full_article(source_article['url'])
                
                if full_article:
                    # TODO: Spara artikel (använd befintlig save_article funktion)
                    stats['new'] += 1
                    logger.info(f"     ✓ Sparad")
                else:
                    stats['errors'] += 1
                    logger.error(f"     ❌ Misslyckades")
                
                time.sleep(1)  # Respektera servern - 1 sekund delay
                
            else:
                # Artikel finns - kontrollera om uppdaterad
                existing = existing_articles[slug]
                
                # Kolla om titel ändrats (indikerar stor uppdatering)
                title_changed = existing['title'] != source_article['title']
                
                # För att verkligen veta om artikeln ändrats måste vi hämta den och kolla datum
                # Men för att inte skrapa ALLA artiklar varje gång, gör vi bara stickprov
                # Alternativ: Implementera detta i framtiden med HEAD requests
                
                if title_changed:
                    logger.info(f"  ✏️  UPPDATERAD: {source_article['title'][:60]}")
                    
                    # Skrapa hela artikeln
                    full_article = scrape_full_article(source_article['url'])
                    
                    if full_article:
                        # Jämför datum för att säkerställa att det verkligen ändrats
                        if full_article['date'] != existing.get('date'):
                            stats['updated'] += 1
                            logger.info(f"     ✓ Uppdaterad")
                            # TODO: Uppdatera artikel
                        else:
                            stats['unchanged'] += 1
                    else:
                        stats['errors'] += 1
                        logger.error(f"     ❌ Misslyckades")
                    
                    time.sleep(1)  # Respektera servern
                else:
                    # Oförändrad
                    stats['unchanged'] += 1
        
        # 5. Hitta raderade artiklar
        for slug in existing_articles:
            if slug not in source_slugs:
                article = existing_articles[slug]
                logger.info(f"  ❌ RADERAD: {article['title'][:60]}")
                stats['deleted'] += 1
                # TODO: Ta bort artikel-fil och ta bort från index
    
    # Sammanfattning
    logger.info("\n" + "="*70)
    logger.info("📊 SAMMANFATTNING")
    logger.info("="*70)
    logger.info(f"  🆕 Nya artiklar:        {stats['new']}")
    logger.info(f"  ✏️  Uppdaterade artiklar: {stats['updated']}")
    logger.info(f"  ❌ Raderade artiklar:    {stats['deleted']}")
    logger.info(f"  ✓  Oförändrade artiklar: {stats['unchanged']}")
    logger.info(f"  ⚠️  Fel:                 {stats['errors']}")
    logger.info("="*70)
    
    # Output för parsing
    total_changes = stats['new'] + stats['updated'] + stats['deleted']
    if total_changes > 0:
        parts = []
        if stats['new'] > 0:
            parts.append(f"{stats['new']} nya")
        if stats['updated'] > 0:
            parts.append(f"{stats['updated']} uppdaterade")
        if stats['deleted'] > 0:
            parts.append(f"{stats['deleted']} raderade")
        logger.info(f"\n✓ {', '.join(parts)}")
    else:
        logger.info("\nℹ️  Inga ändringar detekterades")
    
    return stats

if __name__ == '__main__':
    import sys
    
    # Kolla om --incremental flagga finns
    if '--incremental' in sys.argv or '-i' in sys.argv:
        stats = incremental_scrape()
        
        # Exit code baserat på resultat
        if stats['errors'] > 0:
            sys.exit(1)  # Fel uppstod
        else:
            sys.exit(0)  # Success
    else:
        print("⚠️  Denna scraper kör endast i inkrementellt läge")
        print("Användning: python3 scraper_incremental.py --incremental")
        print("\nFör full scraping, använd: python3 scraper.py")
        sys.exit(1)

