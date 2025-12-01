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
from pathlib import Path
from datetime import datetime

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
            print(f"  ⚠️  Kunde inte läsa {index_file}: {e}")
    
    return {}

def get_article_metadata_from_source(category_url):
    """
    Hämta artikellista från källan med titel, URL och synligt datum
    Skrapar INTE hela artikeln ännu, bara metadata
    """
    print(f"  Hämtar artikellista från {category_url}...")
    
    try:
        response = requests.get(category_url, timeout=30)
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
        
        print(f"  ✓ Hittade {len(articles_metadata)} artiklar i listan")
        return articles_metadata
        
    except Exception as e:
        print(f"  ❌ Fel vid hämtning av artikellista: {e}")
        return []

def scrape_full_article(url):
    """Skrapar fullständig artikel från URL"""
    try:
        response = requests.get(url, timeout=30)
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
    except Exception as e:
        print(f"  ❌ Fel vid scraping av {url}: {e}")
        return None

def incremental_scrape():
    """
    Inkrementell scraping - bara nya, ändrade och raderade
    
    Returns:
        dict: Statistik över ändringar
    """
    print("\n🔄 INKREMENTELL SCRAPING STARTAR")
    print("="*70)
    
    stats = {
        'new': 0,
        'updated': 0,
        'deleted': 0,
        'unchanged': 0,
        'errors': 0
    }
    
    for category in CATEGORIES:
        print(f"\n📂 Kategori: {category['name']}")
        folder = category['folder']
        
        # 1. Ladda befintliga artiklar
        existing_articles = load_existing_articles(folder)
        print(f"  📄 Befintliga artiklar: {len(existing_articles)}")
        
        # 2. Hämta artikellista från källan
        source_articles = get_article_metadata_from_source(category['url'])
        
        if not source_articles:
            print(f"  ⚠️  Kunde inte hämta artiklar från källan, hoppar över kategori")
            continue
        
        # 3. Skapa lookup för snabb sökning
        source_slugs = {article['slug']: article for article in source_articles}
        
        # 4. Hitta nya och uppdaterade artiklar
        for source_article in source_articles:
            slug = source_article['slug']
            
            if slug not in existing_articles:
                # NY ARTIKEL
                print(f"  🆕 NY: {source_article['title'][:60]}")
                
                # Skrapa hela artikeln
                full_article = scrape_full_article(source_article['url'])
                
                if full_article:
                    # TODO: Spara artikel (använd befintlig save_article funktion)
                    stats['new'] += 1
                else:
                    stats['errors'] += 1
                
                time.sleep(1)  # Rate limiting
                
            else:
                # Artikel finns - kontrollera om uppdaterad
                existing = existing_articles[slug]
                
                # Enkel check: om titel ändrats
                if existing['title'] != source_article['title']:
                    print(f"  ✏️  UPPDATERAD: {source_article['title'][:60]}")
                    
                    # Skrapa hela artikeln
                    full_article = scrape_full_article(source_article['url'])
                    
                    if full_article:
                        # Jämför datum för att säkerställa att det verkligen ändrats
                        if full_article['date'] != existing.get('date'):
                            stats['updated'] += 1
                            # TODO: Uppdatera artikel
                        else:
                            stats['unchanged'] += 1
                    else:
                        stats['errors'] += 1
                    
                    time.sleep(1)
                else:
                    # Oförändrad
                    stats['unchanged'] += 1
        
        # 5. Hitta raderade artiklar
        for slug in existing_articles:
            if slug not in source_slugs:
                article = existing_articles[slug]
                print(f"  ❌ RADERAD: {article['title'][:60]}")
                stats['deleted'] += 1
                # TODO: Ta bort artikel-fil och ta bort från index
    
    # Sammanfattning
    print("\n" + "="*70)
    print("📊 SAMMANFATTNING")
    print("="*70)
    print(f"  🆕 Nya artiklar:        {stats['new']}")
    print(f"  ✏️  Uppdaterade artiklar: {stats['updated']}")
    print(f"  ❌ Raderade artiklar:    {stats['deleted']}")
    print(f"  ✓  Oförändrade artiklar: {stats['unchanged']}")
    print(f"  ⚠️  Fel:                 {stats['errors']}")
    print("="*70)
    
    # Output för parsing i API
    total_changes = stats['new'] + stats['updated'] + stats['deleted']
    if total_changes > 0:
        parts = []
        if stats['new'] > 0:
            parts.append(f"{stats['new']} nya")
        if stats['updated'] > 0:
            parts.append(f"{stats['updated']} uppdaterade")
        if stats['deleted'] > 0:
            parts.append(f"{stats['deleted']} raderade")
        print(f"\n✓ {', '.join(parts)}")
    else:
        print("\nℹ️  Inga ändringar detekterades")
    
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

