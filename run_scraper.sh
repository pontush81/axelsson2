#!/bin/bash

echo "======================================"
echo "  FLEX HRM SCRAPER - FULL WORKFLOW"
echo "======================================"
echo ""

# 1. Kör enhanced scraper
echo "📥 Steg 1: Skrapar alla artiklar med metadata..."
python3 scraper_enhanced.py

if [ $? -ne 0 ]; then
    echo "❌ Skrapning misslyckades!"
    exit 1
fi

echo ""
echo "======================================"
echo "✅ KLART!"
echo "======================================"
echo ""
echo "📊 Genererade filer:"
echo "  - documentation/*/index.json (per kategori)"
echo "  - documentation/master_index.json (huvudindex)"
echo "  - documentation/*/*.md (alla artiklar med metadata)"
echo ""
echo "🌐 Öppna index_new.html i en webbläsare för att se resultatet!"
echo ""

