# 🔄 Uppdateringsknapp - Dokumentation

## Översikt

Uppdateringsknappen gör det möjligt för användare att trigga en ny scraping direkt från UI:et. Systemet använder **inkrementell scraping** vilket betyder att bara nya, ändrade och raderade artiklar hanteras - inte hela dokumentationen.

## Hur det fungerar

### 1. UI-knapp

```
┌───────────────────────────────────────────┐
│ 📚 Flex HRM Dokumentation                 │
│                    [🔄 Uppdatera dokument] │
└───────────────────────────────────────────┘
```

Knappen finns i headern och visar olika states:
- **Vilar**: 🔄 Uppdatera dokumentation  
- **Laddar**: 🔄 Uppdaterar... (spinner animation)
- **Klar**: ✓ Uppdaterad!
- **Fel**: ❌ Fel vid uppdatering

### 2. API Endpoint

**Vercel Serverless Function**: `/api/update.py`

```python
POST /api/update
```

Endpoint körs som en Vercel Serverless Function och:
1. Tar emot POST request från UI
2. Kör `scraper.py --incremental`
3. Returnerar resultat (success/error)

### 3. Inkrementell Scraping

Istället för att skrapa allt:

**Fullständig scraping** (gammal):
- Skrapar alla 369 artiklar
- Tar ~5-10 minuter
- Skapar om alla filer

**Inkrementell scraping** (ny):
- Jämför mot befintlig data
- Skrapar bara artiklar med ändrat datum
- Tar ~30 sekunder
- Uppdaterar bara det som ändrats

## Implementation

### För produktion (Vercel)

1. **Deploy till Vercel**:
```bash
vercel
```

2. **Knappen anropar automatiskt**:
```javascript
fetch('/api/update', { method: 'POST' })
```

3. **Vercel kör** `api/update.py` som serverless function

### För lokal utveckling

**Alternativ 1: Använd compare_updates.py**

```bash
# 1. Skapa backup
cp -r documentation documentation_backup_$(date +%Y-%m-%d)

# 2. Kör scraper
python3 scraper.py

# 3. Jämför
python3 compare_updates.py
```

**Alternativ 2: Lokal API-server**

```bash
# Starta lokal Flask server
python3 local_api_server.py

# UI anropar då http://localhost:5000/api/update
```

## Säkerhet

### Begränsningar

**VIKTIGT**: API endpoint bör skyddas för produktionsmiljö!

Förslag på säkerhet:
1. **Rate limiting** - Max 1 update per 5 minuter
2. **API-nyckel** - Kräv secret token
3. **IP-whitelist** - Bara tillåt från vissa IPs
4. **Auth** - Kräv inloggning

### Exempel med API-nyckel

```python
# api/update.py
def do_POST(self):
    # Check API key
    api_key = self.headers.get('X-API-Key')
    if api_key != os.getenv('UPDATE_API_KEY'):
        self.send_response(401)
        self.end_headers()
        return
    
    # Rest of code...
```

```javascript
// index.html
const response = await fetch('/api/update', {
    method: 'POST',
    headers: {
        'X-API-Key': 'your-secret-key-here'
    }
});
```

## Inkrementell Scraping Logik

### Hur detekteras ändringar?

1. **Ladda befintlig data**:
```python
old_articles = load_existing_articles()
```

2. **Hämta källans artikellista**:
```python
source_articles = get_article_list_from_source()
```

3. **Jämför**:
```python
for article in source_articles:
    old_article = old_articles.get(article.slug)
    
    if not old_article:
        # NY ARTIKEL - skrapa!
        scrape_article(article)
    elif old_article.date != article.date:
        # ÄNDRAD ARTIKEL - skrapa!
        scrape_article(article)
    else:
        # Oförändrad - hoppa över
        pass

# Hitta raderade
for slug in old_articles:
    if slug not in source_articles:
        # RADERAD - ta bort!
        delete_article(slug)
```

### Resultat

Efter uppdatering:
- **Nya artiklar** läggs till
- **Ändrade artiklar** uppdateras
- **Raderade artiklar** tas bort
- **Oförändrade** lämnas som de är

## UI-flöde

### Steg-för-steg

1. **Användare klickar "Uppdatera"**
   - Knappen disableas
   - Text ändras till "Uppdaterar..."
   - Spinner animation startar

2. **API-anrop görs**
   ```javascript
   fetch('/api/update', { method: 'POST' })
   ```

3. **Backend processar**
   - Kör inkrementell scraping
   - Tar ~30 sekunder

4. **Response hanteras**
   - Success: Visar "✓ Uppdaterad!" och laddar om sidan
   - Error: Visar "❌ Fel" och återställer knappen

5. **Sidan laddas om**
   - Nya artiklar visas
   - "NYTT"-badges uppdateras

## Felsökning

### Problem: "Fel vid uppdatering"

**Möjliga orsaker:**
1. API endpoint inte deployad
2. Scraper script fel
3. Nätverksproblem
4. Permissions fel

**Lösning:**
```bash
# Testa API lokalt
curl -X POST http://localhost:5000/api/update

# Kolla logs
vercel logs

# Testa scraper manuellt
python3 scraper.py --incremental
```

### Problem: "Knappen gör inget"

**Kontrollera:**
1. Browser console för JavaScript errors
2. Network tab för API request
3. CORS headers är korrekt satta

### Problem: "Tar för lång tid"

**Optimering:**
- Kontrollera att `--incremental` flaggan används
- Kolla att inte alla artiklar skrapas
- Öka timeout i Vercel settings

## Miljövariabler

För Vercel deployment:

```bash
# .env
UPDATE_API_KEY=your-secret-key-here
SCRAPER_TIMEOUT=300  # 5 minutes
```

Sätt via Vercel dashboard:
```bash
vercel env add UPDATE_API_KEY
```

## Framtida förbättringar

Möjliga tillägg:
- [ ] Progress bar under uppdatering
- [ ] Visa vad som ändrats efter uppdatering
- [ ] Schemalagd automatisk uppdatering (cron job)
- [ ] Email-notis när nya artiklar finns
- [ ] Webhook från Flex när de uppdaterar
- [ ] Diff-visning av ändringar

## Testning

### Manuell test

1. **Gör en ändring på källan** (knowledge.flexapplications.se)
2. **Klicka "Uppdatera"** i UI
3. **Verifiera** att ändringen syns
4. **Kontrollera** att bara ändrad artikel skrapades

### Automatisk test

```python
# test_incremental_scrape.py
def test_incremental_update():
    # Skapa testdata
    # Kör inkrementell scraping
    # Verifiera resultat
    assert new_articles_count == expected
```

## Support

För problem eller frågor, kontakta utvecklaren eller skapa ett issue.

