# 📸 Bildstöd tillagt!

## ✨ Nya funktioner

### 1. **Automatisk bildnedladdning**
Scrapern laddar nu automatiskt ner alla bilder från artiklarna:
- ✅ Bilder sparas lokalt i `documentation/[kategori]/images/`
- ✅ Unika filnamn baserade på artikel + bild-hash
- ✅ Bilder länkas korrekt i både Markdown och HTML

### 2. **Bildvisning på startsidan**
- ✅ Badge visar antal bilder per artikel (📸 3)
- ✅ Lätt att se vilka artiklar som har bilder
- ✅ Filtrering fungerar fortfarande perfekt

### 3. **Förbättrad artikelvy**
- ✅ **Bilder integrerade i artikeltext**
- ✅ **Separat bildgalleri** längst ner
- ✅ **Lightbox** för fullskärmsvisning
  - Klicka på bild för att förstora
  - Tryck ESC eller klicka för att stänga
- ✅ **Responsiva bilder** med snygga skuggor
- ✅ **Lazy loading** för snabb sidladdning

### 4. **Tekniska förbättringar**
- ✅ Bilder sparas både i Markdown och HTML-format
- ✅ Bildmetadata inkluderad i `index.json`
- ✅ Alt-text och titles bevarade
- ✅ Felhantering om bilder inte kan laddas

---

## 📊 Bildstruktur

```
documentation/
├── time/
│   ├── images/
│   │   ├── hur-stamplar-man-sin-tid_abc12345.jpg
│   │   ├── hur-stamplar-man-sin-tid_def67890.png
│   │   └── ...
│   ├── index.json (inkluderar bildinfo)
│   ├── hur-stamplar-man-sin-tid.md (med bildreferenser)
│   └── hur-stamplar-man-sin-tid.html (HTML-version)
├── employee/
│   ├── images/
│   └── ...
└── ...
```

---

## 🎨 Visuella förbättringar

### Startsidan:
```
┌─────────────────────────────────────┐
│ Hur stämplar man sin tid i mobilen?│
│                                     │
│ Beskrivning av artikeln...         │
│                                     │
│ [Mellan] [📸 3] #mobil #stämpling  │
└─────────────────────────────────────┘
```

### Artikelvyn:
```
┌───────────────────────────────────────┐
│ # Hur stämplar man sin tid i mobilen?│
│                                       │
│ Artikeltext med förklaring...        │
│                                       │
│ [Bild visas här - klickbar]          │
│                                       │
│ Mer text...                           │
│                                       │
│ ## 📸 Bilder från artikeln            │
│ [thumbnail] [thumbnail] [thumbnail]   │
│                                       │
│ ## 📌 Relaterade artiklar             │
│ ...                                   │
└───────────────────────────────────────┘
```

### Lightbox:
```
┌───────────────────────────────────────┐
│                                       │
│         [Stor bild centrerad]         │
│                                       │
│     (Klicka eller tryck ESC för att   │
│      stänga)                          │
└───────────────────────────────────────┘
```

---

## 🚀 Användning

### Kör scraper med bildstöd:

```bash
python3 scraper_enhanced.py
```

Detta kommer nu att:
1. ✅ Skrapa alla artiklar (som förut)
2. ✅ **NYTT:** Identifiera alla bilder i artiklarna
3. ✅ **NYTT:** Ladda ner bilder till lokala mappar
4. ✅ **NYTT:** Skapa bildreferenser i Markdown
5. ✅ **NYTT:** Spara HTML-version med original-bilder
6. ✅ **NYTT:** Uppdatera metadata med bildinfo

---

## 📈 Metadata-exempel

```json
{
  "title": "Hur stämplar man sin tid i mobilen?",
  "file": "hur-stamplar-man-sin-tid-i-mobilen.md",
  "htmlFile": "hur-stamplar-man-sin-tid-i-mobilen.html",
  "slug": "hur-stamplar-man-sin-tid-i-mobilen",
  "category": "time",
  "subcategory": "Mobil & Stämpling",
  "type": "howto",
  "difficulty": "beginner",
  "tags": ["mobil", "stämpling", "tidrapport"],
  "imageCount": 3,
  "images": [
    "images/hur-stamplar-man-sin-tid_abc12345.jpg",
    "images/hur-stamplar-man-sin-tid_def67890.png",
    "images/hur-stamplar-man-sin-tid_ghi11213.jpg"
  ],
  "excerpt": "HRM Mobile - Stämpling..."
}
```

---

## 🎯 Funktioner i detalj

### 1. Bildnedladdning
- **Automatisk detektering** av alla `<img>` taggar
- **Konvertering** av relativa URLs till absoluta
- **Unika filnamn** via MD5-hash (undviker dubletter)
- **Stöd för olika format**: JPG, PNG, GIF, WEBP
- **Timeout-hantering** (10 sekunder per bild)
- **Felhantering** - scriptet fortsätter även om en bild misslyckas

### 2. Bildoptimering
- **Lazy loading** - bilder laddas endast när de scrollas in
- **Responsiva** - anpassar sig efter skärmstorlek
- **Komprimerade** - bevarar original men optimerar visning
- **Cachning** - bilder cachas av webbläsaren

### 3. Lightbox
- **Fullskärmsvisning** med mörk bakgrund
- **Keyboard support** - ESC för att stänga
- **Click-to-close** - klicka var som helst för att stänga
- **Smooth animations** - mjuka övergångar

### 4. Bildgalleri
- **Grid layout** - snyggt rutnät med thumbnails
- **Hover effects** - bilder förstoras vid hover
- **Click to expand** - öppnar lightbox
- **Alt-text preserved** - tillgänglighet bibehålls

---

## 🔄 Jämförelse: Innan vs Efter

| Feature | Innan | Efter |
|---------|-------|-------|
| Bilder i artiklar | ❌ Saknas | ✅ Inkluderade |
| Bildnedladdning | ❌ Nej | ✅ Automatisk |
| Lightbox | ❌ Nej | ✅ Fullskärm |
| Bildgalleri | ❌ Nej | ✅ Separat sektion |
| Bildräknare | ❌ Nej | ✅ Badge på kort |
| Lazy loading | ❌ Nej | ✅ Optimerat |
| Metadata | ❌ Ingen bildinfo | ✅ Antal + sökvägar |

---

## 💾 Diskutrymme

Bilderna kommer att ta lite diskutrymme:

- **Genomsnittlig bildstorlek**: ~50-200 KB
- **Artiklar med bilder**: ~30-40% (uppskattning)
- **Genomsnitt bilder per artikel**: 2-3
- **Total storlek**: ~50-100 MB (uppskattning)

Detta är helt OK för moderna system och Vercel's free tier (100 MB gräns).

---

## 🧪 Testscenario

Efter att ha kört den nya scrapern kan du testa:

### 1. Verifiera bildnedladdning
```bash
ls -lh documentation/time/images/
# Bör visa nedladdade bilder
```

### 2. Kontrollera metadata
```bash
cat documentation/time/index.json | grep imageCount
# Bör visa antal bilder per artikel
```

### 3. Testa i webbläsare
```bash
./test_website.sh
# Öppna: http://localhost:8000/index_new.html
```

### 4. Klicka på artikel med bilder
- Leta efter artiklar med 📸-badge
- Klicka för att öppna
- Scrolla ner till bildgalleriet
- Klicka på bild för lightbox

---

## 🎨 CSS-anpassningar

### Ändra bildstil:
```css
.article-body img {
    max-width: 100%;
    border-radius: 8px;        /* Rundade hörn */
    box-shadow: 0 4px 12px;    /* Skugga */
    margin: 2rem 0;            /* Marginal */
}
```

### Ändra gallery-layout:
```css
.images-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    /* Ändra 250px till önskat min-storlek */
}
```

### Ändra lightbox-bakgrund:
```css
.lightbox {
    background: rgba(0, 0, 0, 0.9);  /* Mörkhet (0-1) */
}
```

---

## 🔮 Framtida förbättringar

- [ ] Bildzooming (pinch-to-zoom på mobil)
- [ ] Bildkarusell (navigera mellan bilder med pilar)
- [ ] Bildkommentarer/beskrivningar
- [ ] Bildfiltrering på startsidan
- [ ] Thumbnail-generering för snabbare laddning
- [ ] WebP-konvertering för mindre filstorlek

---

## 📞 Support

Om bilder inte laddas:
1. **Kontrollera nätverksanslutning** under scraping
2. **Verifiera att images/-mappar skapades**
3. **Kolla konsolen** för felmeddelanden
4. **Testa med en artikel** först

---

## 🎉 Sammanfattning

Nu har du:
✅ **Kategorisering** (30+ underkategorier)  
✅ **Sökning & filtrering** (typ, svårighet, kategori)  
✅ **Bilder** (automatisk nedladdning + lightbox)  
✅ **Relaterade artiklar** (AI-baserad matchning)  
✅ **Modern design** (responsiv & snabb)  

**Total uppgradering från originalversionen! 🚀**

---

**Uppdaterad:** 2025-12-01  
**Version:** 2.1 (med bildstöd)

