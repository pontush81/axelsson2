#!/bin/bash

echo "======================================"
echo "  FLEX HRM SCRAPER - MED BILDER! 📸"
echo "======================================"
echo ""

# 1. Kör enhanced scraper med bildstöd
echo "📥 Skrapar alla artiklar MED bilder..."
echo ""
python3 scraper_with_images.py

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
echo "  - documentation/*/index.json (metadata per kategori)"
echo "  - documentation/master_index.json (huvudindex)"
echo "  - documentation/*/*.md (alla artiklar)"
echo "  - documentation/*/images/*.jpg/png (ALLA BILDER! 📸)"
echo ""
echo "🌐 Öppna index_new.html i en webbläsare för att se resultatet!"
echo ""
echo "💡 Tips: Artiklar med bilder visar nu en '📸 X bilder' badge!"
echo ""

