# 📤 Export Guide - Få ut alla artiklar

## 🎯 Du kan exportera till 3 format:

1. **📄 Word (.docx)** - Med inbäddade bilder
2. **📊 Excel (.xlsx)** - Med länkar till bilder  
3. **📦 ZIP** - Komplett med alla filer och bilder

---

## 🚀 Snabbstart (2 minuter)

### Steg 1: Installera dependencies

```bash
pip install python-docx openpyxl
```

### Steg 2: Kör export

```bash
python3 export_with_images.py
```

### Steg 3: Klart!

Du får 3 filer:
```
✅ flex_hrm_dokumentation_20251201.docx  (~5-10 MB med bilder)
✅ flex_hrm_dokumentation_20251201.xlsx  (~1 MB)
✅ flex_hrm_complete_20251201.zip         (~50-100 MB allt)
```

---

## 📄 WORD Export (MED bilder)

**Innehåll:**
- ✅ Alla 369 artiklar
- ✅ Formaterade rubriker
- ✅ Metadata (datum, URL, antal bilder)
- ✅ **Inbäddade bilder** (max 5 per artikel)
- ✅ Sidbrytningar mellan kategorier

**Användning:**
- Öppna i Microsoft Word
- Öppna i Google Docs (Fil → Öppna → Ladda upp)
- Öppna i Pages (Mac)

**Bra för:**
- Läsa offline
- Dela med kollegor
- Skriva ut
- Redigera och annotera

---

## 📊 EXCEL Export (med bildlänkar)

**Innehåll:**
- ✅ Alla 369 artiklar i tabellformat
- ✅ Kolumner: Kategori | Titel | Datum | URL | Innehåll | Antal bilder | Bildmapp
- ✅ Formaterade headers
- ✅ Auto-anpassade kolumnbredder

**Användning:**
- Öppna i Microsoft Excel
- Öppna i Google Sheets
- Öppna i Numbers (Mac)

**Bra för:**
- Filtrera och sortera
- Skapa pivottabeller
- Analysera data
- Import till andra system

---

## 📦 ZIP Export (komplett)

**Innehåll:**
- ✅ Alla markdown-filer
- ✅ Alla JSON-filer  
- ✅ **ALLA 2,096 bilder**
- ✅ Exakt kopia av documentation/-mappen

**Storlek:** ~50-100 MB

**Användning:**
- Extrahera ZIP
- Få tillgång till alla originalfiler
- Perfekt för backup
- Perfekt för offline-access

**Bra för:**
- Backup
- Offline-arkiv
- Dela hela dokumentationen
- Import till annat system

---

## 🎨 Endast befintliga exports (UTAN bilder):

### CSV Export:
```bash
python3 export_all.py
```
Skapar: `alla_artiklar.csv` (~1.2 MB)

### Markdown Export:
```bash
python3 export_all.py
```
Skapar: `alla_artiklar.md` (~1.2 MB)

### Word (utan bilder):
```bash
python3 export_docx.py
```
Skapar: `alla_artiklar.docx` (~0.3 MB)

---

## 🔄 Uppdatera exports automatiskt

### Lägg till i GitHub Actions:

```yaml
- name: 📤 Generera exports
  run: |
    pip install python-docx openpyxl
    python3 export_with_images.py
    
- name: 📦 Spara exports som artifacts
  uses: actions/upload-artifact@v3
  with:
    name: exports
    path: |
      *.docx
      *.xlsx
      *.zip
```

**Då får du:**
- Automatisk export varje natt
- Ladda ner från GitHub Actions
- Alltid färsk data

---

## 💡 Tips:

### För stora dokument:

**Word blir för stort?**
```python
# I export_with_images.py, ändra:
excerpt[:1000]  # till
excerpt[:200]   # För kortare utdrag
```

**För många bilder?**
```python
article_images[:5]  # till
article_images[:2]  # Max 2 bilder per artikel
```

### För snabbare export:

```bash
# Endast en kategori:
python3 export_with_images.py --category time

# Utan bilder (snabbt):
python3 export_all.py
```

---

## 📊 Storlekar (uppskattade):

| Format | Utan bilder | Med bilder |
|--------|-------------|------------|
| Word | ~0.3 MB | ~5-10 MB |
| Excel | ~0.5 MB | ~1 MB (länkar) |
| CSV | ~1.2 MB | N/A |
| Markdown | ~1.2 MB | N/A |
| ZIP | ~2 MB | ~50-100 MB |

---

## ⚡ Kör nu:

```bash
# Installera (engångs)
pip install python-docx openpyxl

# Exportera!
python3 export_with_images.py

# Vänta ~2-3 minuter (med bilder tar tid)
# Klart! Du har nu alla filer.
```

🎉 Njut av din dokumentation offline!

