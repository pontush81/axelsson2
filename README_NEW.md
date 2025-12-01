## 🚀 Flex HRM Dokumentation - Enhanced Version

### 📊 Vad är nytt?

Den här versionen har **massiva förbättringar** jämfört med den tidigare:

#### ✨ Nya funktioner:

1. **🔍 Intelligent sökning**
   - Sök i titlar, innehåll och tags
   - Realtidsfiltrering
   - Ingen server behövs - allt i frontend!

2. **📂 Smart kategorisering**
   - 6 huvudkategorier
   - 30+ underkategorier (automatiskt genererade)
   - Artiklar grupperade efter ämne

3. **🏷️ Rik metadata**
   - **Artikeltyp**: Hur gör jag, Begrepp, Inställningar, FAQ, Funktioner
   - **Svårighetsgrad**: Nybörjare, Mellannivå, Avancerad
   - **Tags**: Automatiskt extraherade nyckelord
   - **Excerpt**: Förhandsgranskning av innehåll

4. **🎯 Relaterade artiklar**
   - AI-baserad matchning baserat på:
     - Samma kategori/underkategori
     - Delade tags
     - Liknande ämnesområde

5. **💎 Modern UI/UX**
   - Responsiv design
   - Snabb navigation
   - Visuella badges för typ och svårighetsgrad
   - Två visningslägen: Rutnät & Lista

---

### 📁 Filstruktur

```
documentation/
├── master_index.json           # Huvudindex med översikt
├── systemgemensamt/
│   ├── index.json             # Metadata för alla artiklar
│   └── *.md                   # Artiklar med rik metadata
├── time/
│   ├── index.json
│   └── *.md
├── employee/
├── payroll/
├── travel-expense/
└── plan/

index_new.html                  # Ny startsida med sökning
article.html                    # Artikelvy med relaterade artiklar
scraper_enhanced.py             # Förbättrad scraper
```

---

### 🎨 Metadata-struktur

Varje artikel i `index.json` har följande struktur:

```json
{
  "title": "Hur stämplar man sin tid i mobilen?",
  "file": "hur-stamplar-man-sin-tid-i-mobilen.md",
  "slug": "hur-stamplar-man-sin-tid-i-mobilen",
  "category": "time",
  "subcategory": "Mobil & Stämpling",
  "type": "howto",
  "difficulty": "beginner",
  "tags": ["mobil", "stämpling", "tidrapport"],
  "date": "den 19 augusti 2025",
  "url": "https://...",
  "isConfig": false,
  "excerpt": "HRM Mobile - Stämpling..."
}
```

#### Artikeltyper:
- **howto**: "Hur gör jag X"
- **concept**: Begrepp och definitioner
- **config**: Inställningar (⚙️-artiklar)
- **faq**: Vanliga frågor
- **feature**: Funktionsbeskrivningar

#### Svårighetsgrader:
- **beginner**: Enkla, grundläggande artiklar
- **intermediate**: Medelnivå
- **advanced**: Avancerade (formler, integrationer, etc)

---

### 📊 Statistik

- **369 artiklar** totalt (upp från 350!)
- **6 kategorier**
- **30+ underkategorier**
- **Automatisk taggning** av alla artiklar
- **Intelligent klassificering** av typ och svårighet

#### Fördelning per kategori:

| Kategori | Artiklar | Top underkategorier |
|----------|----------|---------------------|
| **Time** | 114 | Tidrapportering (30), Inställningar (21), Mobil & Stämpling (19) |
| **Systemgemensamt** | 80 | Användare & Behörighet (41), Mobil (13), Register (12) |
| **Employee** | 75 | Anställningshantering (60), Kompetens & Kurser (4) |
| **Payroll** | 68 | Löneberedning (35), Inställningar (12), Skatt & AGI (8) |
| **Travel & Expense** | 24 | Reseräkningar (14), Utlägg & Kvitton (4) |
| **Plan** | 8 | Schemaläggning (4), Kalender (2) |

---

### 🚀 Användning

#### 1. Kör ny skrapning:

```bash
python3 scraper_enhanced.py
```

Detta kommer att:
- Skrapa alla artiklar från knowledge.flexapplications.se
- Analysera och klassificera varje artikel
- Generera tags och underkategorier
- Skapa index.json för varje kategori
- Skapa master_index.json

#### 2. Öppna webbplatsen:

Öppna `index_new.html` i en webbläsare. Inga server behövs!

**För deployment på Vercel:**
- Byt namn på `index_new.html` till `index.html`
- Push till GitHub
- Vercel deployer automatiskt

---

### 🎯 Användningsexempel

#### Sökning:
- Sök efter "stämpling mobil" → Hittar alla artiklar om mobilstämpling
- Filtrera på kategori "Time" + typ "howto" → Alla "hur gör jag"-guider för Time

#### Navigation:
1. **Startsida** (`index_new.html`)
   - Sök och filtrera artiklar
   - Klicka på populära tags
   - Bläddra genom kategorier och underkategorier

2. **Artikelvy** (`article.html`)
   - Läs artikel med formatering
   - Se metadata (typ, svårighet, tags)
   - Upptäck relaterade artiklar
   - Länk till originalkälla

---

### 🔄 Jämförelse: Gammal vs Ny

| Feature | Gammal | Ny |
|---------|--------|-----|
| Sökning | ❌ | ✅ Full-text sökning |
| Filtrering | ❌ | ✅ Kategori, typ, svårighet |
| Underkategorier | ❌ | ✅ 30+ underkategorier |
| Tags | ❌ | ✅ Automatiska tags |
| Relaterade artiklar | ❌ | ✅ AI-baserad matchning |
| Metadata | Minimal | ✅ Rik (typ, svårighet, tags) |
| Artikelvy | Länk till extern | ✅ Egen vy med kontext |
| UI/UX | Grundläggande | ✅ Modern & responsiv |

---

### 🛠️ Tekniska detaljer

#### Frontend:
- Vanilla JavaScript (inga ramverk behövs)
- CSS med custom properties
- Responsive design
- Client-side rendering
- Debounced search för prestanda

#### Backend (Scraper):
- Python 3.9+
- Beautiful Soup för HTML parsing
- Requests för HTTP
- Intelligent klassificering via regelbaserad AI
- Automatisk taggning baserat på nyckelord

#### Dependencies:
```bash
pip install requests beautifulsoup4
```

---

### 📝 Utveckling & Underhåll

#### Uppdatera dokumentation:
```bash
# Kör scraper
python3 scraper_enhanced.py

# Verifiera
ls -lh documentation/master_index.json
```

#### Anpassa underkategorier:
Redigera `subcategory_rules` i `scraper_enhanced.py` (rad ~130)

#### Anpassa tags:
Redigera `keywords_map` i `scraper_enhanced.py` (rad ~80)

---

### 🎨 Design & Branding

#### Färgschema:
- Primary: `#667eea` (Lila/blå)
- Primary Dark: `#764ba2` (Mörkare lila)
- Success: `#10b981` (Grön)
- Warning: `#f59e0b` (Orange)
- Danger: `#ef4444` (Röd)

#### Typography:
- System font stack för snabb laddning
- Responsiva font-sizes
- Optimerad line-height för läsbarhet

---

### 📈 Prestandaoptimering

- **Lazy loading**: Artiklar laddas endast när synliga
- **Debounced search**: Sökning triggas inte vid varje tangenttryck
- **Efficient filtering**: Client-side filtrering i millisekunder
- **Minimal bundle**: Ingen JavaScript-ramverk = snabb laddning

---

### 🔮 Framtida förbättringar

- [ ] Export till PDF per kategori
- [ ] Versionshantering av artiklar
- [ ] Offline-support med Service Worker
- [ ] Analytics (mest lästa artiklar)
- [ ] Användarfeedback på artiklar
- [ ] Multi-språk support
- [ ] Dark mode

---

### 💡 Tips & Tricks

1. **Snabb navigation**: Använd Cmd/Ctrl+F för att söka direkt
2. **Filtrera smart**: Kombinera kategori + typ för bästa resultat
3. **Utforska tags**: Klicka på populära tags för att hitta relaterat innehåll
4. **Bookmark**: Spara direktlänkar till specifika artiklar

---

### 📞 Support & Frågor

För frågor om:
- **Innehåll**: Kontakta Flex Support
- **Tekniska problem**: Se GitHub issues
- **Funktionsförfrågningar**: Öppna en GitHub issue

---

### 📜 Licens

Dokumentationen tillhör Flex Applications / Visma.

**Senast uppdaterad**: 2025-12-01

---

**Made with ❤️ for better documentation**

