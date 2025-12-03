#!/usr/bin/env python3
"""
Uppdaterar last_check i master_index.json
Används av GitHub Actions workflow
"""
import json
from datetime import datetime

def main():
    with open('documentation/master_index.json', 'r', encoding='utf-8') as f:
        master = json.load(f)

    master['last_check'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    master['last_check_status'] = 'success'

    with open('documentation/master_index.json', 'w', encoding='utf-8') as f:
        json.dump(master, f, ensure_ascii=False, indent=2)

    print(f"✅ last_check uppdaterad: {master['last_check']}")

if __name__ == '__main__':
    main()

