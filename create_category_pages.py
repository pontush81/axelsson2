#!/usr/bin/env python3
import os
import glob

categories = {
    'systemgemensamt': {'name': 'Systemgemensamt', 'desc': 'Frågor och svar som rör de gemensamma delarna i Flex HRM'},
    'time': {'name': 'Time', 'desc': 'Frågor och svar som rör HRM Time - tidrapportering och schema'},
    'employee': {'name': 'Employee', 'desc': 'Frågor och svar som rör HRM Employee - anställningar och dokument'},
    'travel-expense': {'name': 'Travel & Expense', 'desc': 'Frågor och svar som rör HRM Travel & Expense'},
    'payroll': {'name': 'Payroll', 'desc': 'Frågor och svar som rör HRM Payroll - löneberedning'},
    'plan': {'name': 'Plan', 'desc': 'Frågor och svar som rör HRM Plan - schemaläggning'}
}

for folder, info in categories.items():
    # Samla alla artiklar
    articles = []
    for filepath in sorted(glob.glob(f'documentation/{folder}/*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                title = lines[0].replace('# ', '').strip()
                filename = os.path.basename(filepath)
                articles.append({'title': title, 'file': filename})
    
    # Skapa HTML-sida
    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{info['name']} - Flex HRM Dokumentation</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}
        header {{
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }}
        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        .back-link {{
            display: inline-block;
            color: white;
            text-decoration: none;
            margin-bottom: 20px;
            font-size: 1.1rem;
        }}
        .back-link:hover {{
            text-decoration: underline;
        }}
        .content {{
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        }}
        .article-list {{
            list-style: none;
        }}
        .article-item {{
            padding: 15px;
            border-bottom: 1px solid #f0f0f0;
        }}
        .article-item:last-child {{
            border-bottom: none;
        }}
        .article-link {{
            color: #667eea;
            text-decoration: none;
            font-size: 1.1rem;
            display: block;
            transition: all 0.2s ease;
        }}
        .article-link:hover {{
            color: #764ba2;
            padding-left: 10px;
        }}
        .count {{
            color: #999;
            font-size: 0.9rem;
            margin-top: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-link">← Tillbaka till startsidan</a>
        <header>
            <h1>📚 {info['name']}</h1>
            <p>{info['desc']}</p>
        </header>
        
        <div class="content">
            <p class="count"><strong>{len(articles)} artiklar</strong></p>
            <ul class="article-list">
'''
    
    for article in articles:
        html += f'''                <li class="article-item">
                    <a href="documentation/{folder}/{article['file']}" class="article-link" target="_blank">
                        {article['title']}
                    </a>
                </li>
'''
    
    html += '''            </ul>
        </div>
    </div>
</body>
</html>'''
    
    # Spara HTML-fil
    with open(f'{folder}.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Skapade {folder}.html med {len(articles)} artiklar")

print("\n✅ Alla kategorisidor skapade!")
