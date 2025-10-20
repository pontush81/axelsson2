#!/usr/bin/env python3
"""
Enkel scraper som använder BeautifulSoup (inget Puppeteer behövs för denna statiska sida)
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import re
import json

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
    """Skapar filnamn från titel"""
    slug = title.lower()
    slug = slug.replace('⚙️', '').replace('️', '')
    slug = slug.replace('å', 'a').replace('ä', 'a').replace('ö', 'o')
    slug = slug.replace('é', 'e').replace('à', 'a')
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug[:80]

def get_article_links(category_url):
    """Hämtar artikellänkar från kategorisida"""
    print(f"  Hämtar länkar från {category_url}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        response = requests.get(category_url, headers=headers, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        links = []
        for link in soup.find_all('a', class_='hs-kb-category-article-list__link'):
            title = link.get_text(strip=True)
            url = link.get('href')
            if url and title:
                links.append({'title': title, 'url': url})
        
        print(f"  ✓ Hittade {len(links)} artiklar")
        return links
    except Exception as e:
        print(f"  ✗ Fel: {e}")
        return []

def scrape_article(url):
    """Skrapar en artikel"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Titel
        title_elem = soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else 'Ingen titel'
        
        # Hitta artikel
        article = soup.find('article')
        if not article:
            return None
        
        # Ta bort oönskade element
        for elem in article.find_all(['aside', 'nav']):
            elem.decompose()
        for cls in ['hs-kb-sidebar', 'hs-kb-breadcrumbs', 'hs-kb-social_follow']:
            for elem in article.find_all(class_=cls):
                elem.decompose()
        
        # Extrahera text
        text = article.get_text(separator='\n', strip=True)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Hitta datum
        date_match = re.search(r'den \d+ \w+ \d{4}', text)
        date = date_match.group(0) if date_match else ''
        
        # Rensa text
        if date:
            text = text.replace(date, '', 1).strip()
        if text.startswith(title):
            text = text[len(title):].strip()
        
        # Ta bort "Hjälpte artikeln?" feedback-text
        text = re.sub(r'Hjälpte artikeln\?.*', '', text, flags=re.DOTALL)
        
        return {
            'title': title,
            'date': date,
            'content': text.strip(),
            'url': url
        }
    except Exception as e:
        print(f"    ✗ Fel vid skrapning: {e}")
        return None

def save_article(article_data, folder, category_name):
    """Sparar artikel som markdown"""
    slug = create_slug(article_data['title'])
    os.makedirs(f"documentation/{folder}", exist_ok=True)
    filepath = f"documentation/{folder}/{slug}.md"
    
    md = f"""# {article_data['title']}

**Datum:** {article_data['date']}  
**Kategori:** {category_name}  
**URL:** {article_data['url']}

---

{article_data['content']}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)
    
    return filepath

def main():
    print("\n" + "="*70)
    print("  FLEX HRM KNOWLEDGE BASE SCRAPER")
    print("="*70 + "\n")
    
    total = 0
    saved = 0
    failed = 0
    
    for cat in CATEGORIES:
        print(f"\n📂 {cat['name']}")
        print("-" * 70)
        
        links = get_article_links(cat['url'])
        total += len(links)
        
        for i, link in enumerate(links, 1):
            print(f"  [{i}/{len(links)}] {link['title'][:55]}...", end=' ')
            
            article = scrape_article(link['url'])
            
            if article:
                save_article(article, cat['folder'], cat['name'])
                saved += 1
                print("✓")
            else:
                failed += 1
                print("✗")
            
            time.sleep(0.3)  # Var snäll mot servern
    
    print("\n" + "="*70)
    print(f"✅ KLART!")
    print(f"📊 Sparade: {saved}/{total} artiklar")
    if failed > 0:
        print(f"⚠️  Misslyckades: {failed}")
    print(f"📁 Plats: /Users/Shared/scraped-knowledge/documentation/")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

