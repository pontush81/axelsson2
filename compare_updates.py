#!/usr/bin/env python3
"""
Jämför två versioner av dokumentationen och visa vad som har ändrats.

Användning:
    python compare_updates.py [gammal_mapp] [ny_mapp]
    
    Om inga mappar anges:
    - gammal_mapp = documentation_backup (senaste backup)
    - ny_mapp = documentation (nuvarande)
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def load_articles(base_path):
    """Ladda alla artiklar från en dokumentationsmapp"""
    articles = {}
    categories = ['employee', 'payroll', 'plan', 'systemgemensamt', 'time', 'travel-expense']
    
    for category in categories:
        index_file = os.path.join(base_path, category, 'index.json')
        if os.path.exists(index_file):
            try:
                with open(index_file, 'r', encoding='utf-8') as f:
                    category_articles = json.load(f)
                    for article in category_articles:
                        # Använd slug som unik nyckel
                        key = f"{category}/{article['slug']}"
                        articles[key] = article
            except Exception as e:
                print(f"⚠️  Kunde inte läsa {index_file}: {e}")
    
    return articles

def load_master_index(base_path):
    """Ladda master index för att få metadata"""
    master_file = os.path.join(base_path, 'master_index.json')
    if os.path.exists(master_file):
        with open(master_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def compare_articles(old_articles, new_articles):
    """Jämför två uppsättningar artiklar"""
    old_keys = set(old_articles.keys())
    new_keys = set(new_articles.keys())
    
    # Hitta skillnader
    added = new_keys - old_keys
    removed = old_keys - new_keys
    common = old_keys & new_keys
    
    # Hitta uppdaterade artiklar
    updated = []
    for key in common:
        old = old_articles[key]
        new = new_articles[key]
        
        # Jämför datum eller titel
        if old.get('date') != new.get('date') or old.get('title') != new.get('title'):
            updated.append({
                'key': key,
                'old': old,
                'new': new
            })
    
    return {
        'added': sorted(list(added)),
        'removed': sorted(list(removed)),
        'updated': updated
    }

def get_category_stats(articles):
    """Räkna artiklar per kategori"""
    stats = defaultdict(int)
    for key in articles.keys():
        category = key.split('/')[0]
        stats[category] += 1
    return dict(stats)

def print_report(old_articles, new_articles, old_master, new_master):
    """Skriv ut en fin rapport"""
    
    print("\n" + "="*70)
    print("📊 UPPDATERINGSRAPPORT - Flex HRM Dokumentation")
    print("="*70)
    
    # Datum
    if old_master and new_master:
        old_date = old_master.get('last_updated', 'Okänt')
        new_date = new_master.get('last_updated', 'Okänt')
        print(f"\n🗓️  Period: {old_date} → {new_date}")
    
    # Översikt
    print(f"\n📈 ÖVERSIKT:")
    print(f"   Totalt förut:  {len(old_articles):>4} artiklar")
    print(f"   Totalt nu:     {len(new_articles):>4} artiklar")
    
    # Jämför
    diff = compare_articles(old_articles, new_articles)
    
    added_count = len(diff['added'])
    removed_count = len(diff['removed'])
    updated_count = len(diff['updated'])
    
    print(f"   Förändring:    {len(new_articles) - len(old_articles):>+4} artiklar")
    print(f"\n   🆕 Nya:        {added_count:>4} artiklar")
    print(f"   ❌ Borttagna:  {removed_count:>4} artiklar")
    print(f"   ✏️  Uppdaterade: {updated_count:>4} artiklar")
    
    # Statistik per kategori
    print(f"\n📂 PER KATEGORI:")
    old_stats = get_category_stats(old_articles)
    new_stats = get_category_stats(new_articles)
    
    all_categories = sorted(set(list(old_stats.keys()) + list(new_stats.keys())))
    
    print(f"   {'Kategori':<20} {'Förut':>6} {'Nu':>6} {'Ändring':>8}")
    print(f"   {'-'*20} {'-'*6} {'-'*6} {'-'*8}")
    
    for cat in all_categories:
        old_count = old_stats.get(cat, 0)
        new_count = new_stats.get(cat, 0)
        change = new_count - old_count
        change_str = f"{change:+d}" if change != 0 else "="
        
        cat_display = cat.replace('-', ' ').title()
        print(f"   {cat_display:<20} {old_count:>6} {new_count:>6} {change_str:>8}")
    
    # Nya artiklar
    if diff['added']:
        print(f"\n🆕 NYA ARTIKLAR ({len(diff['added'])}):")
        print("   " + "-"*66)
        
        # Gruppera per kategori
        by_category = defaultdict(list)
        for key in diff['added']:
            category = key.split('/')[0]
            article = new_articles[key]
            by_category[category].append(article)
        
        for category in sorted(by_category.keys()):
            cat_display = category.replace('-', ' ').title()
            articles = by_category[category]
            print(f"\n   📁 {cat_display} ({len(articles)}):")
            for article in articles[:5]:  # Max 5 per kategori
                title = article['title'][:60]
                date = article.get('date', 'N/A')
                print(f"      • {title}")
                print(f"        {date}")
            
            if len(articles) > 5:
                print(f"      ... och {len(articles) - 5} till")
    
    # Borttagna artiklar
    if diff['removed']:
        print(f"\n❌ BORTTAGNA ARTIKLAR ({len(diff['removed'])}):")
        print("   " + "-"*66)
        
        for key in diff['removed'][:10]:  # Max 10
            article = old_articles[key]
            category = key.split('/')[0].replace('-', ' ').title()
            title = article['title'][:60]
            print(f"   [{category}] {title}")
        
        if len(diff['removed']) > 10:
            print(f"   ... och {len(diff['removed']) - 10} till")
    
    # Uppdaterade artiklar
    if diff['updated']:
        print(f"\n✏️  UPPDATERADE ARTIKLAR ({len(diff['updated'])}):")
        print("   " + "-"*66)
        
        for item in diff['updated'][:15]:  # Max 15
            key = item['key']
            old = item['old']
            new = item['new']
            category = key.split('/')[0].replace('-', ' ').title()
            
            title = new['title'][:55]
            old_date = old.get('date', 'N/A')
            new_date = new.get('date', 'N/A')
            
            print(f"   [{category}] {title}")
            if old_date != new_date:
                print(f"      Datum: {old_date} → {new_date}")
            if old.get('title') != new.get('title'):
                print(f"      Titel ändrad!")
        
        if len(diff['updated']) > 15:
            print(f"   ... och {len(diff['updated']) - 15} till")
    
    # Sammanfattning
    print(f"\n{'='*70}")
    if added_count == 0 and removed_count == 0 and updated_count == 0:
        print("✅ Inga förändringar upptäcktes!")
    else:
        print(f"✅ Rapport klar! Totalt {added_count + removed_count + updated_count} förändringar.")
    print("="*70 + "\n")

def main():
    # Bestäm mappar
    if len(sys.argv) >= 3:
        old_path = sys.argv[1]
        new_path = sys.argv[2]
    else:
        # Hitta senaste backup
        base_dir = Path(__file__).parent
        backup_dirs = sorted([d for d in base_dir.glob('documentation_backup*') if d.is_dir()])
        
        if backup_dirs:
            old_path = str(backup_dirs[-1])  # Senaste backup
            new_path = str(base_dir / 'documentation')
        else:
            print("❌ Ingen backup hittades!")
            print("\nAnvändning:")
            print("  1. Skapa backup: cp -r documentation documentation_backup_$(date +%Y-%m-%d)")
            print("  2. Kör scraping")
            print("  3. Kör: python compare_updates.py")
            sys.exit(1)
    
    # Validera mappar
    if not os.path.exists(old_path):
        print(f"❌ Gammal mapp finns inte: {old_path}")
        sys.exit(1)
    
    if not os.path.exists(new_path):
        print(f"❌ Ny mapp finns inte: {new_path}")
        sys.exit(1)
    
    print(f"\n🔍 Jämför:")
    print(f"   Gammal: {old_path}")
    print(f"   Ny:     {new_path}")
    
    # Ladda artiklar
    print("\n📥 Laddar artiklar...")
    old_articles = load_articles(old_path)
    new_articles = load_articles(new_path)
    
    old_master = load_master_index(old_path)
    new_master = load_master_index(new_path)
    
    print(f"   ✓ Laddade {len(old_articles)} gamla artiklar")
    print(f"   ✓ Laddade {len(new_articles)} nya artiklar")
    
    # Skriv rapport
    print_report(old_articles, new_articles, old_master, new_master)
    
    # Spara rapport till fil
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"update_report_{timestamp}.txt"
    
    # Redirect print to file
    import io
    from contextlib import redirect_stdout
    
    with open(report_file, 'w', encoding='utf-8') as f:
        with redirect_stdout(f):
            print_report(old_articles, new_articles, old_master, new_master)
    
    print(f"💾 Rapport sparad: {report_file}")

if __name__ == '__main__':
    main()

