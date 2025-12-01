# 📸 Flex HRM Dokumentation - MED BILDER!

## 🎉 Vad är nytt?

Den **allra senaste versionen** inkluderar nu **fullständigt stöd för bilder**!

### ✨ Bildstöd inkluderar:

1. **📥 Automatisk nedladdning**
   - Alla bilder från artiklarna laddas ner lokalt
   - Sparas i `documentation/[kategori]/images/`
   - Unika filnamn för att undvika konflikter

2. **🖼️ Visning i artiklar**
   - Bilder visas direkt i artikelvyn
   - Responsiva bilder (anpassar sig till skärmstorlek)
   - Snygg styling med skuggor och rundade hörn

3. **🏷️ Metadata**
   - Antal bilder visas på artikelkort
   - "📸 X bilder" badge på artiklar med bilder
   - Filtrering möjlig baserat på om artikel har bilder

4. **💾 Lokal lagring**
   - Inga externa beroenden - allt lokalt!
   - Fungerar offline
   - Snabbare laddning

---

## 🚀 Användning

### Steg 1: Kör scraper med bildstöd

```bash
# Gör scriptet körbart (första gången)
chmod +x run_scraper_with_images.sh

# Kör scraper
./run_scraper_with_images.sh
```

**ELLER** kör Python-scriptet direkt:

```bash
python3 scraper_with_images.py
```

### Steg 2: Vad händer?

Scrapern kommer att:
1. ✅ Skrapa alla 369+ artiklar
2. ✅ Hitta alla bilder i varje artikel
3. ✅ Ladda ner bilderna till `documentation/[kategori]/images/`
4. ✅ Uppdatera markdown-filer med bildlänkar
5. ✅ Lägga till metadata om antal bilder per artikel

### Steg 3: Visa resultatet

```bash
# Alternativ 1: Öppna direkt
open index_new.html

# Alternativ 2: Starta lokal server
./test_website.sh
```

---

## 📁 Filstruktur efter skrapning

```
documentation/
├── master_index.json           ← Huvudindex
├── time/
│   ├── index.json             ← Metadata (inkl. imageCount!)
│   ├── images/                ← 🆕 BILDER!
│   │   ├── hur-stamplar-man_abc123.jpg
│   │   ├── hur-stamplar-man_def456.png
│   │   └── ...
│   └── *.md                   ← Artiklar med bildreferenser
├── employee/
│   ├── images/                ← 🆕 BILDER!
│   └── ...
└── [andra kategorier...]
```

---

## 🎨 Hur bilder visas

### I artikellistan (index_new.html):
```
┌─────────────────────────────────────┐
│ Hur stämplar man sin tid i mobilen?│
│                                     │
│ HRM Mobile - Stämpling...           │
│                                     │
│ [Nybörjare] [📸 3 bilder] #mobil   │
└─────────────────────────────────────┘
```

### I artikelvyn (article.html):
```
┌───────────────────────────────────────────┐
│ # Hur stämplar man sin tid i mobilen?    │
│                                           │
│ [Time] [Hur] [Nybörjare] [📸 3 bilder]  │
│                                           │
│ Innehåll med text...                      │
│                                           │
│ [BILD VISAS HÄR]                         │
│                                           │
│ Mer text...                               │
│                                           │
│ [BILD VISAS HÄR]                         │
└───────────────────────────────────────────┘
```

---

## 🔧 Tekniska detaljer

### Bildnedladdning

**Filnamnsformat:**
```
{artikel-slug}_{url-hash}.{ext}

Exempel:
hur-stamplar-man-sin-tid-i-mobilen_abc12345.jpg
```

**Stöder:**
- ✅ JPG/JPEG
- ✅ PNG
- ✅ GIF
- ✅ WebP
- ✅ Alla bildformat som webbläsare stödjer

### Bildoptimering

Bilder visas med:
```css
max-width: 100%;           /* Responsiv */
height: auto;              /* Behåller proportioner */
border-radius: 8px;        /* Rundade hörn */
box-shadow: 0 4px 12px...; /* Skugga */
margin: 2rem 0;            /* Avstånd */
```

### Metadata

Varje artikel i `index.json` har nu:
```json
{
  "title": "...",
  "imageCount": 3,
  "hasImages": true,
  ...
}
```

---

## 📊 Förväntade resultat

### Exempel från tidigare skrapningar:

| Kategori | Artiklar | Bilder (ca) |
|----------|----------|-------------|
| Time | 114 | 200-300 |
| Employee | 75 | 150-200 |
| Payroll | 68 | 100-150 |
| Systemgemensamt | 80 | 150-200 |
| Travel & Expense | 24 | 40-60 |
| Plan | 8 | 15-20 |
| **TOTALT** | **369** | **650-930** 📸 |

**Uppskattat:**
- Tid: ~30-45 minuter (längre pga bildnedladdningar)
- Storlek: ~50-150 MB (beroende på bildkvalitet)

---

## ⚙️ Konfiguration

### Ändra bildkvalitet/storlek

Redigera `scraper_with_images.py`:

```python
# Rad ~XX: I download_image funktionen
# Lägg till bildbearbetning med Pillow:

from PIL import Image

# Efter nedladdning:
img = Image.open(filepath)
img.thumbnail((1200, 1200))  # Max storlek
img.save(filepath, optimize=True, quality=85)
```

### Hoppa över bilder (bara text)

Använd den gamla scrapern istället:
```bash
python3 scraper_enhanced.py  # Utan bilder
```

---

## 🐛 Felsökning

### Problem: Bilderna laddas inte ner

**Orsak:** Timeout eller nätverksproblem

**Lösning:**
```python
# I scraper_with_images.py, rad ~60
response = requests.get(img_url, timeout=30)  # Öka timeout
```

### Problem: Bilder visas inte i webbläsaren

**Orsak:** Fel sökväg

**Kontrollera:**
1. Finns bilderna i `documentation/*/images/`?
2. Öppnar du via HTTP-server? (inte `file://`)

**Lösning:**
```bash
# Använd alltid lokal server:
./test_website.sh
```

### Problem: För många/stora bilder

**Lösning:**
1. Begränsa bildstorlek (se Konfiguration ovan)
2. Lägg till `.gitignore` för bilder om du inte vill commita dem:
```
documentation/*/images/*.jpg
documentation/*/images/*.png
```

---

## 📈 Jämförelse: Med vs Utan bilder

| Feature | Utan bilder | Med bilder |
|---------|-------------|------------|
| Artiklar | 369 | 369 |
| Bilder | 0 | 650-930 📸 |
| Storlek | ~5 MB | ~50-150 MB |
| Skraptid | ~10 min | ~30-45 min |
| Offline | ✅ | ✅ |
| Visuellt | 📝 Text | 🖼️ Text + Bilder |
| Användarvänlighet | Bra | **Utmärkt!** |

---

## 💡 Tips & Tricks

### 1. Separera bilder från kod

```bash
# Lägg till i .gitignore
documentation/*/images/

# Spara bilder på CDN/separat server istället
# Uppdatera bildlänkar i markdown-filerna
```

### 2. Optimera bilder innan deployment

```bash
# Använd ImageMagick för batch-optimering
find documentation -name "*.jpg" -exec convert {} -quality 85 {} \;
find documentation -name "*.png" -exec convert {} -colors 256 {} \;
```

### 3. Lazy loading för snabbare laddning

Uppdatera `article.html`:
```javascript
// I loadArticleContent()
.replace(/!\[(.*?)\]\((.*?)\)/g, '<img src="/documentation/' + 
    currentArticle.category + '/$2" alt="$1" loading="lazy" ...>')
```

---

## 🎯 Nästa steg

1. ✅ Kör `./run_scraper_with_images.sh`
2. ✅ Vänta 30-45 minuter
3. ✅ Öppna `index_new.html`
4. ✅ Njut av dokumentation med bilder! 🎉

---

## 📞 Support

**Tekniska frågor:**
- Kolla `README_NEW.md` för grundläggande info
- Kolla `SUMMARY.md` för översikt

**Bildfrågor:**
- Denna fil (`MED_BILDER.md`)

---

**🎉 Lycka till med den nya bildrika dokumentationen!**

*Skapad: 2025-12-01*  
*Version: 2.1 - Med bilder! 📸*

