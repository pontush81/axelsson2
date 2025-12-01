# 🚀 Setup Guide - Uppdateringsfunktion

## Snabbstart (5 minuter)

### Steg 1: Generera API-nyckel

```bash
# Generera en stark 32-tecken nyckel
openssl rand -hex 32
```

Du får något som: `a3f7b2c9d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1`

**Spara denna nyckel säkert!** ⚠️

### Steg 2: Sätt API-nyckel i Vercel

```bash
# Logga in på Vercel
vercel login

# Sätt environment variable
vercel env add UPDATE_API_KEY

# Klistra in din genererade nyckel när promptad
```

### Steg 3: Sätt API-nyckel i Frontend

Öppna `index.html` och hitta raden (~1030):

```javascript
const apiKey = window.UPDATE_API_KEY || 'dev-key-change-in-production';
```

Ändra till:

```javascript
const apiKey = 'a3f7b2c9d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1';
```

**OBS:** Använd SAMMA nyckel som du satte i Vercel!

### Steg 4: Deploy till Vercel

```bash
vercel --prod
```

### Steg 5: Testa!

1. Öppna din site (t.ex. `https://yoursite.vercel.app`)
2. Klicka på **"🔄 Uppdatera dokumentation"**
3. Du bör se antingen:
   - ✓ "X nya, Y uppdaterade" 
   - ℹ️ "Allt är uppdaterat"

---

## 🔐 Alternativ: Säkrare setup (för senare)

### Ta bort API-nyckel från frontend

Istället för att ha nyckeln i frontend-koden, kan du:

**Alternativ A: Session-baserad auth**
```javascript
// 1. Användare loggar in först
// 2. Session cookie sätts
// 3. Backend verifierar session istället för API-nyckel
```

**Alternativ B: Server-side trigger**
```bash
# Kör update direkt på servern (cron job)
0 2 * * * cd /path/to/project && python3 scraper_incremental.py --incremental
```

**Alternativ C: Admin-panel**
- Skapa separata admin-sida med login
- Endast admin kan trigga updates
- Använd JWT eller session tokens

---

## 📋 Konfigurera Rate Limiting

Standard-inställningar (i `api/rate_limiter.py`):

```python
max_requests=3       # Max 3 updates per timme
cooldown_minutes=5   # Min 5 minuter mellan updates
```

**Justera för dina behov:**

```bash
# I Vercel environment
vercel env add MAX_UPDATES_PER_HOUR
# Ange: 5 (för fler updates)

vercel env add COOLDOWN_MINUTES
# Ange: 10 (för längre cooldown)
```

---

## 🧪 Testa lokalt innan deployment

### 1. Installera dependencies

```bash
pip install requests beautifulsoup4
```

### 2. Testa inkrementell scraper

```bash
python3 scraper_incremental.py --incremental
```

Du bör se output som:

```
🔄 INKREMENTELL SCRAPING STARTAR
======================================================================

📂 Kategori: Time
  📄 Befintliga artiklar: 114
  Hämtar artikellista från https://...
  ✓ Hittade 114 artiklar i listan
  
  (ingen output = inga ändringar)

======================================================================
📊 SAMMANFATTNING
======================================================================
  🆕 Nya artiklar:        0
  ✏️  Uppdaterade artiklar: 0
  ❌ Raderade artiklar:    0
  ✓  Oförändrade artiklar: 114
  ⚠️  Fel:                 0
======================================================================

ℹ️  Inga ändringar detekterades
```

### 3. Simulera ändringar

För att testa att det fungerar:

```bash
# 1. Ta bort en artikel från index.json
# 2. Kör scraper igen
python3 scraper_incremental.py --incremental

# Du bör se:
#   🆕 NY: [artikel titel]
#   ✓ 1 nya
```

---

## 🐛 Felsökning

### Problem: "401 Ogiltig API-nyckel"

**Lösning:**
1. Kontrollera att samma nyckel finns i:
   - Vercel environment (`UPDATE_API_KEY`)
   - Frontend (`index.html`, variabel `apiKey`)
2. Deploy om efter ändring av env variables:
   ```bash
   vercel --prod
   ```

### Problem: "429 Vänta X minuter"

**Detta är normalt!** Du har nått rate limit.

**Lösning:**
- Vänta den angivna tiden
- Eller öka `MAX_UPDATES_PER_HOUR` i environment

### Problem: "En uppdatering pågår redan"

**Lösning:**
- Vänta tills den pågående uppdateringen är klar (~30-60 sekunder)
- Om den hänger sig (> 10 minuter), ta bort lock manuellt:
  ```bash
  # På Vercel server
  rm /tmp/update_lock.json
  ```

### Problem: Update tar för lång tid

**Orsaker:**
1. Källan är långsam
2. Många artiklar att skrapa
3. Network issues

**Lösning:**
- Öka timeout i `vercel.json`:
  ```json
  "maxDuration": 600  // 10 minuter
  ```

### Problem: Inga ändringar visas trots update

**Lösning:**
1. Ladda om sidan (Ctrl+Shift+R / Cmd+Shift+R)
2. Kolla browser console för errors
3. Verifiera att JSON-filer uppdaterades:
   ```bash
   ls -lt documentation/*/index.json
   ```

---

## 📊 Vercel Configuration

Uppdatera `vercel.json`:

```json
{
  "functions": {
    "api/update.py": {
      "maxDuration": 300,
      "memory": 1024
    }
  },
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "POST, OPTIONS"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "Content-Type, X-API-Key, Authorization"
        },
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        }
      ]
    }
  ]
}
```

---

## 🎓 För Nybörjare: Vad är vad?

### API-nyckel
= Hemligt lösenord som bevisar att du får använda uppdateringsfunktionen

### Rate Limiting  
= Begränsning av hur ofta du kan uppdatera (förhindrar spam)

### Queue
= Kö som säkerställer att bara EN uppdatering körs åt gången

### Incremental Scraping
= Bara hämta det som ändrats (istället för allt)

### Environment Variables
= Inställningar som lagras på servern (inte i koden)

---

## ✅ Checklist för första gången

- [ ] Generera API-nyckel
- [ ] Sätt nyckel i Vercel environment
- [ ] Sätt samma nyckel i `index.html`
- [ ] Uppdatera `vercel.json` (om den inte redan är rätt)
- [ ] Deploy: `vercel --prod`
- [ ] Testa uppdateringsfunktionen
- [ ] Verifiera att rate limiting fungerar
- [ ] Kolla audit logs: `/tmp/update_audit.log`

---

## 📞 Support

Om något inte fungerar:
1. Kolla browser console (F12)
2. Kolla Vercel logs: `vercel logs`
3. Kör scraper manuellt för debugging:
   ```bash
   python3 scraper_incremental.py --incremental
   ```

**Lycka till!** 🚀

