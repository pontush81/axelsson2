# 🔒 SÄKERHETSGUIDE - Uppdateringsfunktion

## ✅ SÄKER IMPLEMENTATION (Nuvarande)

Vi använder **INTE** synliga API-nycklar i frontend! Istället har vi **3 säkerhetslager**:

---

## 🛡️ Säkerhetslager

### Layer 1: IP-Whitelist (Valfritt men rekommenderat)

**Endast tillåtna IP-adresser kan uppdatera**

```bash
# Sätt i Vercel environment
vercel env add ALLOWED_UPDATE_IPS

# Ange dina IPs (komma-separerade):
192.168.1.100,203.0.113.5
```

**Hur hitta din IP:**
```bash
curl ifconfig.me
```

✅ **Fördelar:**
- Bara ditt kontor/hem kan uppdatera
- Fungerar utan inloggning

❌ **Nackdelar:**
- Fungerar inte med dynamiska IPs
- Problem vid VPN-byte

---

### Layer 2: Token-baserad Auth (Standard)

**Säkra, tidsbegränsade tokens som genereras av backend**

#### Hur det fungerar:

```
1. Frontend → [GET /api/get_token] → Backend
2. Backend → Genererar token (HMAC-signerad med secret)
3. Backend → Returnerar token till frontend
4. Frontend → [POST /api/update med token] → Backend
5. Backend → Verifierar token (korrekt + inte utgången)
6. Backend → ✓ Kör scraping
```

#### Tokens är:
- ✅ **IP-bundna** - Fungerar bara från samma IP som begärde den
- ✅ **Tidsbegränsade** - Giltig i 1 timme
- ✅ **HMAC-signerade** - Kan inte förfalskas utan secret key
- ✅ **Inte synliga i källkod** - Genereras vid runtime

#### Token-format:
```
timestamp:hmac_hash
1733058240:a7f3b2c9d4e5f6a7b8c9d0e1f2a3b4c5...
```

---

### Layer 3: Rate Limiting + Queue

**Förhindrar spam och överbelastning**

```python
✅ Max 3 updates per timme (per IP)
✅ Min 5 minuter mellan updates
✅ Endast 1 update åt gången (queue system)
✅ 10 minuters timeout för hängande updates
```

---

## 🔑 Hemlig nyckel (Backend Only)

**UPDATE_API_KEY används för:**
- ✅ Signera tokens (HMAC)
- ✅ Verifiera tokens
- ❌ INTE synlig i frontend!

### Sätt API-nyckeln:

```bash
# 1. Generera stark nyckel
openssl rand -hex 32

# Exempel output:
# a3f7b2c9d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1

# 2. Sätt i Vercel (ENDAST här!)
vercel env add UPDATE_API_KEY production

# 3. Klistra in nyckeln när promptad
```

**⚠️ VIKTIGT:**
- Nyckeln finns BARA på servern
- Nyckeln finns INTE i frontend-koden
- Nyckeln finns INTE i Git

---

## 🚀 Setup för Produktion

### Minimal Setup (Fungerar direkt):

```bash
# 1. Sätt hemlig nyckel
vercel env add UPDATE_API_KEY production
# Ange: [din genererade 32-tecken nyckel]

# 2. Deploy
vercel --prod

# 3. Klart! 
# IP-whitelist är valfri (disabled som default)
```

### Rekommenderad Setup (Med IP-whitelist):

```bash
# 1. Sätt hemlig nyckel
vercel env add UPDATE_API_KEY production

# 2. Hitta dina IPs
curl ifconfig.me  # Din nuvarande IP

# 3. Sätt IP-whitelist
vercel env add ALLOWED_UPDATE_IPS production
# Ange: 203.0.113.5,198.51.100.10
# (Komma-separerad lista)

# 4. Deploy
vercel --prod
```

---

## 🔐 Hur systemet skyddar dig:

### Scenario 1: Hacker försöker uppdatera

```
1. Hacker → [GET /api/get_token]
2. Backend → Kollar IP
3. Backend → ❌ IP inte i whitelist
4. Hacker → Får 403 Forbidden
5. Hacker → Kan INTE uppdatera
```

### Scenario 2: Hacker kopierar token från Network tab

```
1. Hacker → Kopierar din token
2. Hacker → Försöker använda från annan IP
3. Backend → Token är IP-bunden
4. Backend → ❌ IP matchar inte
5. Hacker → Får 401 Unauthorized
```

### Scenario 3: Hacker väntar och använder gammal token

```
1. Hacker → Väntar 2 timmar
2. Hacker → Försöker använda gammal token
3. Backend → Token har gått ut (max 1 timme)
4. Backend → ❌ Token expired
5. Hacker → Måste ladda om sidan för ny token
```

### Scenario 4: Hacker försöker brute-force

```
1. Hacker → Försöker gissa tokens
2. Backend → Rate limiter träder in
3. Backend → ❌ För många försök
4. Hacker → Blockerad i 1 timme
```

---

## 📊 Jämförelse: Osäkert vs Säkert

### ❌ OSÄKERT (Gammal metod):

```javascript
// index.html
const apiKey = 'min-hemliga-nyckel';  // Synlig för alla!

fetch('/api/update', {
    headers: { 'X-API-Key': apiKey }
});
```

**Problem:**
- Nyckel synlig i källkod (View Source)
- Vem som helst kan kopiera och använda
- Ingen IP-validering
- Ingen token expiration

### ✅ SÄKERT (Ny metod):

```javascript
// 1. Hämta token (genereras av backend)
const tokenData = await fetch('/api/get_token');
const token = tokenData.token;  // Unik, tidsbegränsad

// 2. Använd token
fetch('/api/update', {
    headers: { 'X-Update-Token': token }
});
```

**Fördelar:**
- ✅ Ingen hemlig nyckel i frontend
- ✅ IP-verifiering (om konfigurerad)
- ✅ Token expires efter 1 timme
- ✅ HMAC-signering (kan inte förfalskas)
- ✅ Rate limiting
- ✅ Queue system

---

## 🔧 Avancerade Inställningar

### Justera token-livstid:

I `api/auth.py`, ändra:
```python
if age_seconds > 3600:  # 1 timme
```

Till:
```python
if age_seconds > 7200:  # 2 timmar
```

### Justera rate limits:

```bash
vercel env add MAX_UPDATES_PER_HOUR
# Ange: 5 (istället för 3)

vercel env add COOLDOWN_MINUTES
# Ange: 10 (istället för 5)
```

### Aktivera debug mode:

```bash
vercel env add DEBUG
# Ange: true

# Visar detaljerade error messages i responses
```

---

## 🎯 Säkerhetsnivåer

Du kan välja mellan 3 nivåer:

### Nivå 1: MINIMAL (Development)
```bash
# Ingen IP-whitelist
# Bara token-auth
# Rate limiting enabled
```
**Användning:** Lokal utveckling, staging

### Nivå 2: STANDARD (Rekommenderat)
```bash
# IP-whitelist enabled
# Token-auth
# Rate limiting + Queue
# Audit logging
```
**Användning:** Normal produktion

### Nivå 3: MAXIMAL (Högsta säkerhet)
```bash
# IP-whitelist
# Admin-panel med inloggning
# Session-baserad auth
# CAPTCHA
# Email-verification
# 2FA
```
**Användning:** Känsliga miljöer, enterprise

**Vi implementerar Nivå 2 som standard!** ✅

---

## 📋 Säkerhets-checklist

Före production:

- [x] API-nyckel INTE i frontend-kod
- [x] Token-baserad auth implementerad
- [x] HMAC-signering för tokens
- [x] IP-bunden tokens
- [x] Token expiration (1 timme)
- [x] Rate limiting (3/timme)
- [x] Cooldown (5 min)
- [x] Queue system (endast 1 åt gången)
- [x] Audit logging
- [x] HTTPS enforced (via Vercel)
- [x] Security headers (nosniff, frame-options, etc.)
- [ ] **Sätt UPDATE_API_KEY i Vercel** ⚠️
- [ ] **Sätt ALLOWED_UPDATE_IPS** (valfritt)
- [ ] Testa rate limiting
- [ ] Testa från ogiltig IP
- [ ] Testa med utgången token

---

## 🆘 Vad göra om nyckeln läcker?

Om UPDATE_API_KEY på något sätt läcker:

```bash
# 1. Generera NY nyckel omedelbart
openssl rand -hex 32

# 2. Uppdatera i Vercel
vercel env rm UPDATE_API_KEY production
vercel env add UPDATE_API_KEY production
# Ange ny nyckel

# 3. Deploy
vercel --prod

# 4. Alla gamla tokens blir ogiltiga automatiskt
```

---

## ✅ Slutsats

**Ditt system är nu säkert!** 🎉

- ✅ Ingen hemlig information i frontend
- ✅ Token-baserad auth med HMAC
- ✅ IP-bunden säkerhet
- ✅ Rate limiting och queue
- ✅ Audit logging
- ✅ Modern security headers

**Nästa steg:** Sätt UPDATE_API_KEY i Vercel och testa!

