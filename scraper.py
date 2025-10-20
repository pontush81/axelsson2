#!/usr/bin/env python3
"""
Flex HRM Knowledge Base Scraper
Skrapar alla artiklar från knowledge.flexapplications.se
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import re
from urllib.parse import unquote

# Kategorier att skrapa
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

def get_article_links(category_url):
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

def scrape_article(url):
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
        'url': url
    }

def save_article(article_data, folder, category_name):
    """Sparar artikel som markdown"""
    slug = create_slug(article_data['title'])
    filepath = f"documentation/{folder}/{slug}.md"
    
    # Skapa mapp om den inte finns
    os.makedirs(f"documentation/{folder}", exist_ok=True)
    
    # Skapa markdown-innehåll
    md_content = f"""# {article_data['title']}

**Datum:** {article_data['date']}  
**Kategori:** {category_name}  
**URL:** {article_data['url']}

---

{article_data['content']}
"""
    
    # Spara fil
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return filepath

def main():
    """Huvudfunktion"""
    print("\n" + "="*60)
    print("  FLEX HRM KNOWLEDGE BASE SCRAPER")
    print("="*60 + "\n")
    
    total_articles = 0
    scraped_articles = 0
    
    for category in CATEGORIES:
        print(f"\n📂 Kategori: {category['name']}")
        print("-" * 60)
        
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
                    # Spara artikel
                    filepath = save_article(article_data, category['folder'], category['name'])
                    scraped_articles += 1
                    print(f" ✓")
                else:
                    print(f" ✗ (ingen data)")
                
                # Vänta lite för att inte överbelasta servern
                time.sleep(0.5)
                
            except Exception as e:
                print(f" ✗ Fel: {str(e)}")
        
        print(f"\n✓ Klar med {category['name']}: {scraped_articles} artiklar sparade")
    
    print("\n" + "="*60)
    print(f"✅ KLART! Skrapade {scraped_articles}/{total_articles} artiklar")
    print(f"📁 Artiklar sparade i: documentation/")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

