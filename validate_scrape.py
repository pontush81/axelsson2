#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import glob
import os

print("🔍 Validerar skrapningen mot knowledge.flexapplications.se\n")
print("="*70)

categories = {
    'systemgemensamt': 'https://knowledge.flexapplications.se/systemgemensamt',
    'time': 'https://knowledge.flexapplications.se/time',
    'employee': 'https://knowledge.flexapplications.se/employee',
    'travel-expense': 'https://knowledge.flexapplications.se/travel-expense',
    'payroll': 'https://knowledge.flexapplications.se/payroll',
    'plan': 'https://knowledge.flexapplications.se/plan'
}

total_online = 0
total_local = 0
all_match = True

for folder, url in categories.items():
    print(f"\n📂 {folder.upper()}")
    print("-" * 70)
    
    # Hämta från webbplatsen
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        online_articles = soup.find_all('a', class_='hs-kb-category-article-list__link')
        online_count = len(online_articles)
        
        print(f"  Online: {online_count} artiklar")
        
    except Exception as e:
        print(f"  ⚠️  Kunde inte hämta från webben: {e}")
        online_count = 0
    
    # Räkna lokala filer
    local_files = glob.glob(f'documentation/{folder}/*.md')
    # Ta bort index.json från räkningen
    local_files = [f for f in local_files if not f.endswith('index.json')]
    local_count = len(local_files)
    
    print(f"  Lokalt: {local_count} artiklar")
    
    # Jämför
    if online_count > 0:
        if local_count >= online_count:
            print(f"  ✅ Alla artiklar nedladdade!")
        else:
            missing = online_count - local_count
            print(f"  ⚠️  Saknas: {missing} artiklar")
            all_match = False
    
    total_online += online_count
    total_local += local_count

print("\n" + "="*70)
print(f"\n📊 TOTALT:")
print(f"  Online: {total_online} artiklar")
print(f"  Lokalt: {total_local} artiklar")

if all_match and total_local >= total_online:
    print(f"\n✅ SUCCESS! Alla artiklar är nedladdade!")
else:
    diff = total_online - total_local
    if diff > 0:
        print(f"\n⚠️  Saknas totalt: {diff} artiklar")
    elif total_local > total_online:
        extra = total_local - total_online
        print(f"\n✅ Vi har {extra} extra artiklar (kan vara duplicat eller versioner)")

print("\n" + "="*70)
