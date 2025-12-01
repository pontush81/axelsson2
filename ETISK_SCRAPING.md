# 🤝 Etisk Scraping - Policy & Compliance

## ✅ VÅR POLICY

Vi följer **etiska scraping-principer** enligt branschstandard och respekterar källan (knowledge.flexapplications.se).

---

## 📋 COMPLIANCE CHECKLIST

### ✅ Robots.txt Compliance

**Status:** ✅ **FÖLJER**

```
Källans robots.txt:
- User-agent: *
- Disallow: /_hcms/preview/
- Disallow: /hs/manage-preferences/
- Disallow: /hs/preferences-center/
- Ingen Disallow för /time, /employee, /payroll etc.
```

**Vår implementation:**
- ✅ Skrapar ENDAST dokumentationssidor
- ✅ Skrapar INTE admin/preview-sidor
- ✅ Respekterar alla Disallow-direktiv

---

### ✅ User-Agent Identification

**Status:** ✅ **IMPLEMENTERAT**

```python
User-Agent: AxelssonDocBot/1.0 (github.com/pontush81/axelsson2; pontus.horberg@example.com)
```

**Vad detta betyder:**
- ✅ Site owner kan identifiera vår bot
- ✅ Kontaktinfo tillgänglig om problem uppstår
- ✅ Transparent om vem vi är

**VIKTIGT:** Uppdatera email-adressen till din riktiga kontakt!

---

### ✅ Rate Limiting & Server Respect

**Status:** ✅ **IMPLEMENTERAT**

| Parameter | Värde | Standard | Status |
|-----------|-------|----------|--------|
| Delay mellan requests | 1 sekund | 0.5-2s | ✅ BRA |
| Request timeout | 30 sekunder | 10-30s | ✅ BRA |
| Frekvens | 1x/dag kl 02:00 | Varies | ✅ EXCELLENT |
| Concurrent requests | 1 (sekventiell) | 1-5 | ✅ SÄKRAST |
| Max retries vid fel | 0 (fail gracefully) | 2-3 | ✅ RESPEKTFULLT |

**Beräkning av server-belastning:**

```
Scenario: 369 artiklar, 10% ändrade = 37 requests
Tid: 37 requests × 1 sekund = 37 sekunder
Belastning: 37 sekunder per dag = 0.04% av dygnets kapacitet
Risk för DoS: NEGLIGERBAR
```

---

### ✅ Off-Peak Timing

**Status:** ✅ **IMPLEMENTERAT**

```yaml
schedule:
  - cron: '0 1 * * *'  # 02:00 svensk tid (01:00 UTC)
```

**Varför 02:00?**
- ✅ Minimal user traffic (minst serverlast)
- ✅ Typisk backup/maintenance-tid
- ✅ Minimal risk att störa användare

---

### ✅ Incremental Scraping

**Status:** ✅ **IMPLEMENTERAT**

**Full vs Incremental:**

```
Full scraping (Före):
- 369 artiklar × 30 sekunder = ~3 timmar
- ~100 MB data transfer
- Hög server-belastning

Incremental scraping (Nu):
- Bara ändrade (typiskt ~5-10 artiklar/dag)
- 10-30 sekunder total tid
- ~1-2 MB data transfer
- Minimal server-påverkan
```

**Implementation:**
1. Ladda befintlig data
2. Hämta artikellista från källan
3. Jämför (slug + datum)
4. Skrapa ENDAST nya/ändrade
5. Ta bort raderade

---

### ⚠️ Terms of Service Review

**Status:** ⚠️ **MÅSTE KOLLAS**

**ACTION REQUIRED:**
1. Läs https://knowledge.flexapplications.se/ Terms of Service
2. Sök efter "automated access", "bots", "scraping"
3. Om förbjudet → Kontakta Flex Applications för tillstånd

**Om ToS förbjuder scraping:**
- ❌ Stoppa scraping omedelbart
- 📧 Kontakta: info@flexapplications.se
- 🤝 Begär explicit tillstånd eller API-access

---

### ✅ Error Handling & Graceful Failure

**Status:** ✅ **IMPLEMENTERAT**

```python
try:
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 429:
        logger.error("Rate limited! Väntar 60 sekunder...")
        time.sleep(60)  # Extra väntetid
    else:
        logger.error(f"HTTP error {e.response.status_code}")
        return None  # Fail gracefully
except requests.exceptions.Timeout:
    logger.error("Timeout - servern svarar långsamt")
    return None  # Hoppa över denna artikel
```

**Vid fel:**
- ✅ Loggar felet (audit trail)
- ✅ Stoppar inte hela scraping
- ✅ Väntar extra vid 429 (rate limit)
- ✅ Skyddar servern

---

### ✅ Logging & Audit Trail

**Status:** ✅ **IMPLEMENTERAT**

**Loggfiler:**
- `scraper.log` - Alla scraping-aktiviteter
- GitHub Actions logs - Permanent historik

**Vad loggas:**
```
2025-12-01 02:00:01 - INFO - 🔄 INKREMENTELL SCRAPING STARTAR
2025-12-01 02:00:02 - INFO - 📂 Kategori: Time
2025-12-01 02:00:03 - INFO - Hämtar artikellista från https://...
2025-12-01 02:00:05 - INFO - 🆕 NY: Hur använder jag nya funktionen?
2025-12-01 02:00:06 - INFO -    ✓ Sparad
2025-12-01 02:00:45 - INFO - ✓ 3 nya, 2 uppdaterade
```

**Retention:**
- GitHub Actions: 90 dagar (default)
- scraper.log: Sparas i repo (permanent)

---

## 🛡️ SÄKERHETSÅTGÄRDER

### Mot DoS (Denial of Service):

| Åtgärd | Implementation | Effekt |
|--------|----------------|--------|
| Request delays | 1 sekund | ✅ Förhindrar burst |
| Off-peak timing | 02:00 | ✅ Minimal påverkan |
| Sequential requests | En åt gången | ✅ Ingen concurrent load |
| Timeout limits | 30 sekunder | ✅ Frigör connections |
| Error backoff | 60s vid 429 | ✅ Respekterar rate limits |
| Incremental only | Bara ändringar | ✅ Minimal traffic |

**Maximal teoretisk belastning:**

```
Worst case: Alla 369 artiklar ändrade
Tid: 369 × 1 sekund = ~6 minuter
Peak requests/second: 1 req/s
Jämfört med typisk site: 100-1000 req/s
Påverkan: <1% av normal kapacitet
```

---

### Mot oavsiktlig skada:

1. **Fail gracefully** ✅
   - Fel på en artikel ≠ stopp på allt
   - Fortsätter med nästa artikel

2. **Backup före ändring** ⚠️ BÖR LÄGGAS TILL
   ```yaml
   - name: Backup innan scraping
     run: cp -r documentation documentation_backup
   ```

3. **Validering efter scraping** ⚠️ BÖR LÄGGAS TILL
   ```python
   # Verifiera att JSON är valid
   # Verifiera att antal artiklar är rimligt
   ```

4. **Rollback capability** ⚠️ BÖR LÄGGAS TILL
   ```bash
   # Om fel: återställ från backup
   git revert HEAD
   ```

---

## 📞 KONTAKT MED SITE OWNER

### Rekommenderad action:

**Skicka email till: info@flexapplications.se**

```
Ämne: Förfrågan om tillåtelse för automatisk scraping av dokumentation

Hej,

Jag har byggt ett verktyg som automatiskt hämtar och presenterar 
dokumentation från knowledge.flexapplications.se.

Tekniska detaljer:
- Körs 1 gång per dag (natt kl 02:00)
- Endast inkrementell scraping (bara nya/ändrade artiklar)
- 1 sekunds delay mellan requests
- Respekterar robots.txt
- Identifierbar User-Agent

Syfte: Förbättra tillgänglighet och sökbarhet för Flex HRM-dokumentation

Frågor:
1. Har ni något emot denna automatiska scraping?
2. Finns det ett API jag kan använda istället?
3. Finns det några preferenser för scraping-frekvens?

Tack!
[Ditt namn]
[Din kontaktinfo]
```

**Fördelar med att fråga:**
- ✅ Visar respekt
- ✅ Kan få bättre lösning (API)
- ✅ Undviker legala problem
- ✅ Bygger relation

---

## ⚖️ LEGAL COMPLIANCE

### GDPR
- ✅ Ingen personlig data skrapas
- ✅ Endast public dokumentation
- ✅ Ingen tracking av användare

### Copyright
- ⚠️ Dokumentationen ägs av Flex Applications
- ⚠️ Du måste respektera deras copyright
- ⚠️ Inkludera attribution: "Källa: knowledge.flexapplications.se"

### Data Storage
- ✅ Lagrar endast i GitHub (ditt privata repo)
- ⚠️ Om public repo → Credit källan tydligt

---

## 🎯 PERPLEXITY REKOMMENDATIONER - STATUS

| Rekommendation | Status | Action |
|----------------|--------|--------|
| **User-Agent med kontakt** | ✅ Implementerat | Uppdatera email |
| **Respektera robots.txt** | ✅ Verifierat | Inga ändringar |
| **Rate limiting** | ✅ 1s delay | OK |
| **Off-peak timing** | ✅ 02:00 | OK |
| **Error handling** | ✅ HTTPError, Timeout | OK |
| **Logging/audit** | ✅ Logging implementerat | OK |
| **Kontakta site owner** | ⚠️ Ej gjort | **REKOMMENDERAT** |
| **Review ToS** | ⚠️ Ej gjort | **MÅSTE GÖRAS** |
| **Start small** | ⚠️ Full scraping direkt | Överväg test först |
| **429 handling** | ✅ 60s backoff | OK |

---

## 🚦 RISK-ASSESSMENT

### Risk för DoS: 🟢 **MYCKET LÅG**

```
✅ 1 request/sekund = negligerbar belastning
✅ 1 gång per dag = sustainable
✅ Off-peak timing = minimal conflict
✅ Incremental = bara nödvändiga requests
✅ Graceful failures = ingen cascade

Bedömning: SÄKER
```

### Risk för legal issues: 🟡 **MEDEL**

```
⚠️ ToS ej granskad = okänd risk
⚠️ Ingen explicit tillåtelse = grey area
✅ Public data = lägre risk
✅ robots.txt följs = bra

Bedömning: LÅGINFORMATION
Action: KONTAKTA SITE OWNER för klarhet
```

### Risk för tekniska problem: 🟢 **LÅG**

```
✅ Error handling = robust
✅ Timeouts = inga hängande requests
✅ Logging = detekterbar problem
✅ GitHub Actions = reliable platform

Bedömning: SÄKER
```

---

## ✅ SLUTSATS

**Din implementation är:**

✅ **Tekniskt säker** - Ingen risk för DoS eller överbelastning
✅ **Etiskt ansvarsfull** - Respekterar robots.txt, delays, off-peak
✅ **Väl implementerad** - Error handling, logging, incremental

**Men:**

⚠️ **Kontakta Flex Applications** för explicit tillåtelse
⚠️ **Läs deras ToS** för automated access policies
⚠️ **Uppdatera email** i User-Agent till din riktiga kontakt

---

## 🎯 NÄSTA STEG

**Före du kör i produktion:**

1. **Uppdatera User-Agent email** till din riktiga adress
2. **Läs Terms of Service** på knowledge.flexapplications.se
3. **Skicka email** till Flex Applications (se mall ovan)
4. **Vänta på svar** (eller fortsätt efter 1 vecka om inget svar)

**Efter tillstånd:**
5. **Kör första scraping manuellt** via GitHub Actions UI
6. **Verifiera att allt fungerar**
7. **Låt automatisk schemaläggning ta över**

---

**Sammanfattning:** Din lösning är **säker och ansvarsfull**, men **kontakta site owner** för att vara 100% säker. 🤝

