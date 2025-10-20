#!/usr/bin/env python3
import os
import csv
import glob

# Skapa CSV med alla artiklar
print("Skapar CSV-fil...")
with open('alla_artiklar.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Kategori', 'Titel', 'Datum', 'URL', 'Innehåll'])
    
    total = 0
    for folder in ['systemgemensamt', 'time', 'employee', 'travel-expense', 'payroll', 'plan']:
        for filepath in sorted(glob.glob(f'documentation/{folder}/*.md')):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extrahera metadata
            lines = content.split('\n')
            title = lines[0].replace('# ', '') if lines else ''
            date = ''
            url = ''
            article_content = []
            
            in_content = False
            for line in lines[1:]:
                if line.startswith('**Datum:**'):
                    date = line.replace('**Datum:**', '').strip()
                elif line.startswith('**URL:**'):
                    url = line.replace('**URL:**', '').strip()
                elif line.strip() == '---':
                    in_content = True
                elif in_content:
                    article_content.append(line)
            
            full_content = '\n'.join(article_content).strip()
            writer.writerow([folder, title, date, url, full_content])
            total += 1
    
    print(f"✓ CSV skapad med {total} artiklar: alla_artiklar.csv")

# Skapa en stor Markdown-fil
print("\nSkapar stor Markdown-fil...")
with open('alla_artiklar.md', 'w', encoding='utf-8') as mdfile:
    mdfile.write('# Flex HRM Dokumentation - Komplett\n\n')
    mdfile.write('**Totalt: 350 artiklar**\n\n')
    mdfile.write('---\n\n')
    
    total = 0
    categories = {
        'systemgemensamt': 'Systemgemensamt',
        'time': 'Time',
        'employee': 'Employee',
        'travel-expense': 'Travel & Expense',
        'payroll': 'Payroll',
        'plan': 'Plan'
    }
    
    for folder, cat_name in categories.items():
        mdfile.write(f'\n# {cat_name}\n\n')
        
        files = sorted(glob.glob(f'documentation/{folder}/*.md'))
        mdfile.write(f'**{len(files)} artiklar**\n\n')
        mdfile.write('---\n\n')
        
        for filepath in files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            mdfile.write(content)
            mdfile.write('\n\n---\n\n')
            total += 1
    
    print(f"✓ Markdown skapad med {total} artiklar: alla_artiklar.md")

print("\n✅ Klart! Filerna finns i /Users/Shared/scraped-knowledge/")
