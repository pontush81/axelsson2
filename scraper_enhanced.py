#!/usr/bin/env python3
"""
Flex HRM Knowledge Base Scraper - Enhanced Version
Skrapar alla artiklar med rik metadata, kategorisering och taggning
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import re
import json
from urllib.parse import unquote, urljoin, urlparse
from collections import defaultdict
import hashlib

# Kategorier att skrapa
CATEGORIES = [
    {'name': 'Systemgemensamt', 'url': 'https://knowledge.flexapplications.se/systemgemensamt', 'folder': 'systemgemensamt'},
    {'name': 'Time', 'url': 'https://knowledge.flexapplications.se/time', 'folder': 'time'},
    {'name': 'Employee', 'url': 'https://knowledge.flexapplications.se/employee', 'folder': 'employee'},
    {'name': 'Travel & Expense', 'url': 'https://knowledge.flexapplications.se/travel-expense', 'folder': 'travel-expense'},
    {'name': 'Payroll', 'url': 'https://knowledge.flexapplications.se/payroll', 'folder': 'payroll'},
    {'name': 'Plan', 'url': 'https://knowledge.flexapplications.se/plan', 'folder': 'plan'}
]

def create_slug(title: str) -> str:
    """Skapar en slug från titel"""
    slug = title.lower()
    slug = slug.replace('⚙️', '')
    slug = slug.replace('å', 'a').replace('ä', 'a').replace('ö', 'o')
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug[:100]

def classify_article_type(title: str, content: str) -> str:
    """Klassificerar artikeltyp baserat på titel och innehåll"""
    title_lower = title.lower()
    
    # Begrepp/glossary artiklar
    if 'begrepp' in title_lower or 'vad betyder' in title_lower or 'vad är' in title_lower:
        return 'concept'
    
    # Hur-gör-jag (howto) artiklar
    if title_lower.startswith('hur ') or 'hur gör' in title_lower or 'hur skapar' in title_lower:
        return 'howto'
    
    # Konfigurations artiklar (har ofta ⚙️)
    if '⚙️' in title or 'inställningar' in title_lower or 'ställer in' in title_lower:
        return 'config'
    
    # FAQ artiklar
    if title_lower.startswith('kan ') or title_lower.startswith('går det'):
        return 'faq'
    
    # Funktionsbeskrivningar
    if 'fungerar' in title_lower or 'används' in title_lower:
        return 'feature'
    
    return 'other'

def extract_tags(title: str, content: str, category: str) -> list:
    """Extraherar relevanta tags från titel och innehåll"""
    tags = set()
    
    # Vanliga nyckelord per kategori
    keywords_map = {
        'time': ['tidrapport', 'stämpling', 'schema', 'frånvaro', 'semester', 'övertid', 
                 'ob', 'lön', 'mobil', 'attestering', 'saldo', 'tidkod', 'beredskap'],
        'employee': ['anställning', 'dokument', 'signering', 'medarbetarsamtal', 'kompetens', 
                     'kurs', 'onboarding', 'offboarding', 'lönerevision', 'cv'],
        'payroll': ['lön', 'semester', 'skatt', 'agi', 'pension', 'bokföring', 'löneart'],
        'travel-expense': ['resa', 'traktamente', 'utlägg', 'bil', 'kvitto', 'attestering'],
        'systemgemensamt': ['användare', 'behörighet', 'roll', 'säkerhet', 'integration', 'mobil'],
        'plan': ['schema', 'kalender', 'prenumeration']
    }
    
    # Sök efter relevanta keywords
    text = (title + ' ' + content).lower()
    category_keywords = keywords_map.get(category, [])
    
    for keyword in category_keywords:
        if keyword in text:
            tags.add(keyword)
    
    # Extrahera specifika begrepp från titel
    if 'mobil' in title.lower():
        tags.add('mobil')
    if 'hrm time' in title.lower():
        tags.add('hrm-time')
    if 'hrm employee' in title.lower():
        tags.add('hrm-employee')
    
    return sorted(list(tags))[:8]  # Max 8 tags

def determine_difficulty(title: str, content: str, article_type: str) -> str:
    """Bestämmer svårighetsgrad"""
    content_lower = content.lower()
    title_lower = title.lower()
    
    # Avancerade indikatorer
    advanced_indicators = ['formel', 'integration', 'api', 'regelverk', 'beräkning', 'koncern']
    if any(ind in content_lower or ind in title_lower for ind in advanced_indicators):
        return 'advanced'
    
    # Konfig är oftast intermediate
    if article_type == 'config':
        return 'intermediate'
    
    # Begrepp är oftast beginner
    if article_type == 'concept':
        return 'beginner'
    
    # Default till beginner för korta, enkla artiklar
    if len(content) < 500:
        return 'beginner'
    
    return 'intermediate'

def categorize_subcategory(title: str, content: str, category: str, tags: list) -> str:
    """Kategoriserar artikel i underkategori"""
    title_lower = title.lower()
    content_lower = content.lower()
    
    subcategory_rules = {
        'time': {
            'Mobil & Stämpling': ['mobil', 'stämpl', 'timeclock', 'stämpelklocka'],
            'Tidrapportering': ['tidrapport', 'dagredovisning', 'periodredovisning', 'tidkod'],
            'Frånvaro & Semester': ['frånvaro', 'semester', 'sjuk', 'ledighet', 'vab'],
            'Inställningar': ['⚙️', 'inställning', 'ställer in', 'konfigurer'],
            'Schema & Planering': ['schema', 'dagschema', 'planering', 'schemastartdatum'],
            'Lön & Överföring': ['överför', 'lön', 'lönesystem'],
            'Övertid & Ersättning': ['övertid', 'ob', 'ersättning', 'beredskap'],
            'Attestering & Granskning': ['attestering', 'granskning', 'delattestering'],
            'Saldon & Beräkning': ['saldo', 'beräkning', 'händelse', 'formel']
        },
        'employee': {
            'Anställningshantering': ['anställning', 'personaldata', 'anställd', 'las'],
            'Dokument & E-signering': ['dokument', 'signering', 'scrive', 'verified'],
            'Medarbetarsamtal': ['medarbetarsamtal', 'performance', 'samtalsmallar'],
            'Kompetens & Kurser': ['kompetens', 'kurs', 'utbildning'],
            'Onboarding & Offboarding': ['onboarding', 'offboarding', 'nyanställning'],
            'Lönerevision': ['lönerevision', 'löneöversyn', 'lönepott'],
            'Organisation': ['organisation', 'organisationsträd', 'chef'],
            'Integration': ['integration', 'teamtailor', 'winningtemp', 'bky']
        },
        'payroll': {
            'Löneberedning': ['löneberedning', 'lönekörning', 'löneunderlag'],
            'Semesterhantering': ['semester', 'semesterlön', 'semestergrundande'],
            'Skatt & AGI': ['skatt', 'agi', 'arbetsgivaravgift'],
            'Pension': ['pension', 'tjänstepension'],
            'Bokföring': ['bokföring', 'kontering', 'verifikation'],
            'Lönearter': ['löneart', 'lönekod'],
            'Inställningar': ['⚙️', 'inställning']
        },
        'travel-expense': {
            'Reseräkningar': ['reseräkning', 'resa'],
            'Traktamente': ['traktamente', 'trakta'],
            'Utlägg & Kvitton': ['utlägg', 'kvitto', 'bilaga'],
            'Bilresor': ['bil', 'milersättning'],
            'Attestering': ['attestering', 'granskning'],
            'Inställningar': ['⚙️', 'inställning']
        },
        'systemgemensamt': {
            'Användare & Behörighet': ['användare', 'behörighet', 'roll', 'säkerhet'],
            'Mobil': ['mobil', 'mobile', 'app'],
            'Integration': ['integration', 'api', 'import', 'export'],
            'Rapporter': ['rapport', 'rapportgenerator'],
            'Register': ['register', 'projekt', 'kund', 'kontering'],
            'Inställningar': ['⚙️', 'inställning']
        },
        'plan': {
            'Schemaläggning': ['schema', 'planering'],
            'Kalender': ['kalender', 'prenumeration'],
            'Begrepp': ['begrepp'],
            'Inställningar': ['⚙️', 'inställning']
        }
    }
    
    rules = subcategory_rules.get(category, {})
    
    # Räkna matchningar för varje underkategori
    matches = defaultdict(int)
    for subcat, keywords in rules.items():
        for keyword in keywords:
            if keyword in title_lower or keyword in content_lower:
                matches[subcat] += 1
    
    # Returnera bästa matchning
    if matches:
        return max(matches, key=matches.get)
    
    return 'Övrigt'

def get_article_links(category_url: str) -> list:
    """Hämtar alla artikellänkar från en kategorisida"""
    print(f"  Hämtar artiklar från {category_url}...")
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    article_links = []
    for link in soup.find_all('a', class_='hs-kb-category-article-list__link'):
        title = link.get_text(strip=True)
        url = link.get('href')
        article_links.append({'title': title, 'url': url})
    
    print(f"  ✓ Hittade {len(article_links)} artiklar")
    return article_links

def download_image(img_url: str, article_slug: str, folder: str) -> str:
    """Laddar ner en bild och returnerar lokal sökväg"""
    try:
        # Skapa images-mapp
        images_dir = f"documentation/{folder}/images"
        os.makedirs(images_dir, exist_ok=True)
        
        # Skapa unikt filnamn baserat på URL
        url_hash = hashlib.md5(img_url.encode()).hexdigest()[:8]
        ext = os.path.splitext(urlparse(img_url).path)[1] or '.jpg'
        filename = f"{article_slug}_{url_hash}{ext}"
        filepath = os.path.join(images_dir, filename)
        
        # Ladda ner om den inte redan finns
        if not os.path.exists(filepath):
            response = requests.get(img_url, timeout=10)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
        
        # Returnera relativ sökväg
        return f"images/{filename}"
    except Exception as e:
        print(f"\n    ⚠️  Kunde inte ladda ner bild: {str(e)}")
        return None

def scrape_article(url: str) -> dict:
    """Skrapar innehåll från en artikel"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Hämta titel
    title_elem = soup.find('h1')
    title = title_elem.get_text(strip=True) if title_elem else 'Ingen titel'
    
    # Hämta artikel
    article = soup.find('article')
    if not article:
        return None
    
    # Samla alla bilder innan vi tar bort element
    images = []
    for img in article.find_all('img'):
        img_url = img.get('src') or img.get('data-src')
        if img_url:
            # Konvertera till absolut URL
            if not img_url.startswith('http'):
                img_url = urljoin(url, img_url)
            
            # Spara bildinformation
            images.append({
                'url': img_url,
                'alt': img.get('alt', ''),
                'title': img.get('title', '')
            })
    
    # Ta bort navigering, sidebar, feedback
    for elem in article.find_all(['aside', 'nav']):
        elem.decompose()
    for elem in article.find_all(class_=['hs-kb-sidebar', 'hs-kb-breadcrumbs', 'hs-kb-social_follow']):
        elem.decompose()
    for elem in article.find_all(string=lambda text: text and 'Hjälpte artikeln' in text):
        if elem.parent:
            elem.parent.decompose()
    
    # Hämta HTML-innehåll för bilder
    html_content = str(article)
    
    # Hämta text
    text = article.get_text(separator='\n', strip=True)
    
    # Rensa bort överdrivet whitespace
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
        'html_content': html_content,
        'images': images,
        'url': url
    }

def save_article_enhanced(article_data: dict, folder: str, category_name: str) -> tuple:
    """Sparar artikel som markdown och returnerar metadata"""
    slug = create_slug(article_data['title'])
    filepath = f"documentation/{folder}/{slug}.md"
    
    # Skapa mapp om den inte finns
    os.makedirs(f"documentation/{folder}", exist_ok=True)
    
    # Klassificera artikel
    article_type = classify_article_type(article_data['title'], article_data['content'])
    tags = extract_tags(article_data['title'], article_data['content'], folder)
    difficulty = determine_difficulty(article_data['title'], article_data['content'], article_type)
    subcategory = categorize_subcategory(article_data['title'], article_data['content'], folder, tags)
    is_config = '⚙️' in article_data['title']
    
    # Ladda ner bilder och skapa markdown-referenser
    image_references = []
    downloaded_images = []
    
    for i, img_data in enumerate(article_data.get('images', []), 1):
        local_path = download_image(img_data['url'], slug, folder)
        if local_path:
            downloaded_images.append(local_path)
            alt_text = img_data.get('alt', f'Bild {i}')
            image_references.append(f"\n![{alt_text}]({local_path})\n")
    
    # Lägg till bilder i innehållet
    images_section = ""
    if image_references:
        images_section = "\n\n## 📸 Bilder\n" + "\n".join(image_references)
    
    # Skapa markdown-innehåll
    md_content = f"""# {article_data['title']}

**Datum:** {article_data['date']}  
**Kategori:** {category_name}  
**Underkategori:** {subcategory}  
**Typ:** {article_type}  
**Svårighetsgrad:** {difficulty}  
**Tags:** {', '.join(tags) if tags else 'Ingen'}  
**Antal bilder:** {len(downloaded_images)}  
**URL:** {article_data['url']}

---

{article_data['content']}{images_section}
"""
    
    # Spara fil
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    # Spara också HTML-version för bättre bildhantering
    html_filepath = f"documentation/{folder}/{slug}.html"
    with open(html_filepath, 'w', encoding='utf-8') as f:
        f.write(article_data.get('html_content', ''))
    
    # Returnera metadata för index
    metadata = {
        'title': article_data['title'],
        'file': f"{slug}.md",
        'htmlFile': f"{slug}.html",
        'slug': slug,
        'category': folder,
        'subcategory': subcategory,
        'type': article_type,
        'difficulty': difficulty,
        'tags': tags,
        'date': article_data['date'],
        'url': article_data['url'],
        'isConfig': is_config,
        'images': downloaded_images,
        'imageCount': len(downloaded_images),
        'excerpt': article_data['content'][:200] + '...' if len(article_data['content']) > 200 else article_data['content']
    }
    
    return filepath, metadata

def main():
    """Huvudfunktion"""
    print("\n" + "="*60)
    print("  FLEX HRM KNOWLEDGE BASE SCRAPER - ENHANCED")
    print("="*60 + "\n")
    
    total_articles = 0
    scraped_articles = 0
    all_metadata = {}
    
    for category in CATEGORIES:
        print(f"\n📂 Kategori: {category['name']}")
        print("-" * 60)
        
        category_metadata = []
        
        # Hämta alla artikellänkar
        article_links = get_article_links(category['url'])
        total_articles += len(article_links)
        
        # Skrapa varje artikel
        for i, article_link in enumerate(article_links, 1):
            try:
                print(f"  [{i}/{len(article_links)}] {article_link['title'][:50]}...", end='')
                
                # Skrapa artikel
                article_data = scrape_article(article_link['url'])
                
                if article_data:
                    # Spara artikel och få metadata
                    filepath, metadata = save_article_enhanced(article_data, category['folder'], category['name'])
                    category_metadata.append(metadata)
                    scraped_articles += 1
                    print(f" ✓")
                else:
                    print(f" ✗ (ingen data)")
                
                # Vänta lite för att inte överbelasta servern
                time.sleep(0.5)
                
            except Exception as e:
                print(f" ✗ Fel: {str(e)}")
        
        # Spara index.json för kategorin
        index_path = f"documentation/{category['folder']}/index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(category_metadata, f, ensure_ascii=False, indent=2)
        
        all_metadata[category['folder']] = category_metadata
        print(f"\n✓ Klar med {category['name']}: {len(category_metadata)} artiklar sparade")
    
    # Spara master index
    master_index = {
        'total_articles': scraped_articles,
        'total_categories': len(CATEGORIES),
        'last_updated': time.strftime('%Y-%m-%d %H:%M:%S'),
        'categories': {}
    }
    
    for cat in CATEGORIES:
        folder = cat['folder']
        if folder in all_metadata:
            # Räkna underkategorier
            subcats = defaultdict(int)
            for article in all_metadata[folder]:
                subcats[article['subcategory']] += 1
            
            master_index['categories'][folder] = {
                'name': cat['name'],
                'total': len(all_metadata[folder]),
                'subcategories': dict(subcats)
            }
    
    with open('documentation/master_index.json', 'w', encoding='utf-8') as f:
        json.dump(master_index, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*60)
    print(f"✅ KLART! Skrapade {scraped_articles}/{total_articles} artiklar")
    print(f"📁 Artiklar sparade i: documentation/")
    print(f"📊 Master index: documentation/master_index.json")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

