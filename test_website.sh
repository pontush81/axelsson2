#!/bin/bash

echo "🌐 Startar lokal webbserver..."
echo ""
echo "✅ Webbplatsen finns på:"
echo "   http://localhost:8000/index_new.html"
echo ""
echo "📄 Artikelexempel:"
echo "   http://localhost:8000/article.html?article=hur-stamplar-man-sin-tid-i-mobilen&category=time"
echo ""
echo "💡 Tryck Ctrl+C för att stoppa servern"
echo ""

# Starta Python HTTP-server
cd /Users/pontus.horberg-Local/Sourcecode/axelsson/axelsson2
python3 -m http.server 8000

