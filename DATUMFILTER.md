# 📅 Datumfilter - Dokumentation

## Översikt

Datumfiltret gör det möjligt att filtrera artiklar baserat på när de senast uppdaterades. Det finns både fördefinierade snabbfilter och möjlighet att välja ett anpassat datumintervall.

## Features

### ✨ Snabbfilter

- **Alla artiklar** - Visar alla artiklar (standard)
- **Senaste månaden** - Artiklar uppdaterade senaste 30 dagarna
  - Visar en badge med antal nya artiklar
- **Senaste 3 månaderna** - Artiklar uppdaterade senaste 90 dagarna
- **Senaste 6 månaderna** - Artiklar uppdaterade senaste 180 dagarna

### 🎯 Anpassat datumintervall

Välj exakt vilka datum du vill filtrera på:
- **Från-datum** - Visa artiklar från och med detta datum
- **Till-datum** - Visa artiklar till och med detta datum
- Båda fälten är valfria - du kan använda bara ett eller båda

### 🆕 NYT-badge

Artiklar uppdaterade senaste 30 dagarna får en grön "NYT"-badge för att synas extra tydligt.

## Hur det fungerar

### Datumformat

Källan (knowledge.flexapplications.se) använder svenska datum i formatet:
```
"den 21 november 2025"
```

Systemet parsar automatiskt dessa datum och konverterar dem till JavaScript Date-objekt för jämförelse.

### Filtrering

Filtret kan kombineras med:
- **Kategori-filter** - Visa endast artiklar från viss modul (Time, Employee, etc.)
- **Sökfält** - Sök i titel, utdrag och taggar

## Användning

### För användare

1. Öppna `index.html` i en webbläsare
2. Scrolla ner till datumfiltret under sökfältet
3. Välj önskat filter:
   - Klicka på en av de fördefinierade alternativen
   - Eller välj "Anpassat datumintervall" och ange datum
4. Artiklarna filtreras automatiskt

### För utvecklare

**Viktiga funktioner:**

```javascript
// Parse svenskt datum till Date-objekt
parseSwedishDate("den 21 november 2025") 
// Returns: Date object

// Uppdatera badge-räknare
updateNewBadge()
// Räknar och visar antal artiklar från senaste 30 dagarna

// Filtrera artiklar (automatiskt anropas vid ändring)
filterArticles()
```

**Event listeners:**

```javascript
// Radio buttons för fördefinierade filter
document.querySelectorAll('input[name="dateFilter"]')

// Anpassade datumfält
document.getElementById('dateFrom')
document.getElementById('dateTo')
```

## Exempel

### Exempel 1: Hitta nya artiklar om tidrapportering

1. Välj kategori: "Time"
2. Välj datum: "Senaste månaden"
3. Resultat: Alla artiklar i Time-kategorin från senaste 30 dagarna

### Exempel 2: Se vad som ändrats under Q4 2024

1. Välj "Anpassat datumintervall"
2. Från: `2024-10-01`
3. Till: `2024-12-31`
4. Resultat: Alla artiklar uppdaterade under oktober-december 2024

### Exempel 3: Hitta äldsta artiklarna

För att hitta artiklar som inte uppdaterats på länge, kan du:
1. Sortera alla artiklar efter datum
2. De utan "NYT"-badge är äldre än 30 dagar

## Tekniska detaljer

### Datumkonvertering

Svenska månadsnamn mappas till JavaScript-månadsindex (0-11):

```javascript
{
    'januari': 0, 'februari': 1, 'mars': 2, 'april': 3,
    'maj': 4, 'juni': 5, 'juli': 6, 'augusti': 7,
    'september': 8, 'oktober': 9, 'november': 10, 'december': 11
}
```

### Filtreringslogik

1. **Alla artiklar** - Ingen filtrering
2. **Fördefinierade** (30/90/180 dagar):
   ```javascript
   const daysAgo = parseInt(dateFilterValue);
   const filterDate = new Date(now.getTime() - (daysAgo * 24 * 60 * 60 * 1000));
   articleDate >= filterDate
   ```
3. **Anpassat intervall**:
   - Om "Från" anges: `articleDate >= fromDate`
   - Om "Till" anges: `articleDate <= toDate` (inkluderar hela dagen)

### Prestanda

- Datumparser körs endast en gång per artikel
- Filtrering sker i minnet (inga API-anrop)
- Debounce används för sökning men inte för datumfilter (omedelbar respons)

## Framtida förbättringar

Möjliga tillägg:
- [ ] Sortering efter datum (nyaste/äldsta först)
- [ ] "Visa ändringshistorik" knapp
- [ ] Exportera filtrerade resultat
- [ ] Spara favorit-filter i localStorage
- [ ] Visuell tidslinje över uppdateringar

## Felsökning

**Problem:** Datumfiltret visar inga resultat

**Lösning:** Kontrollera att:
1. Artiklarnas datumfält följer formatet "den DD månad YYYY"
2. Månadsnamnet är på svenska
3. Custom-datumfält har giltiga värden

**Problem:** "NYT"-badge visar fel antal

**Lösning:** 
- Badgen uppdateras när sidan laddas
- Ladda om sidan för att få rätt antal

## Support

För frågor eller buggrapporter, kontakta utvecklaren eller skapa ett issue i projektet.

