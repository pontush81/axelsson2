# ⚙️Hur aktiverar jag funktionen Fakturering i HRM Travel?

**Datum:** den 2 oktober 2025  
**Kategori:** Travel & Expense  
**Underkategori:** Reseräkningar  
**Typ:** config  
**Svårighetsgrad:** intermediate  
**Tags:** bil, resa, traktamente, utlägg  
**Bilder:** 14  
**URL:** https://knowledge.flexapplications.se/hur-anv%C3%A4nds-funktionen-frisl%C3%A4pp-till-fakturering-i-hrm-travel

---

Funktionen “Fakturering” eller “Frisläpp till fakturering” används antingen för att få ut faktureringsunderlag för att fakturera kunder direkt alternativt exportera utläggsbelopp, traktamentesbelopp eller bilresor (per konteringar) för uppföljning.
Inställningar - Allmänt - Fakturering - Fliken Resa
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_d87f0296.png)
Använd fakturering i resa
Använd fakturering i resa måste aktiveras för att funktionen ska fungera i Travel.
Momssats fakturerbara reseräkningar
Används endast om man önskar vidarefakturerar frisläppta timmar direkt till kund. Om man inte direktfakturerar anger man 0 %
Krävd granskningsnivå
Ange vilken granskningsnivå (Klar, projektattest, attest) som krävs för att en tidrad skall “frisläppas”. En frisläppt rad kan aldrig frisläppas på nytt (om man inte använder funktionen korrigering av fakturaunderlag)
Prissättande konteringsdimension
Här anges vilken konteringsdimension som ska användas för prissättning. Möjlighet finns även att sätta pris på andra dimensioner (register), men detta kräver att den prissättande dimensionen är satt på prisraden i fråga.
Lås granskningsnivå vid frisläpp
Markera detta fält om granskningsnivån ska låsas vid frisläpp till fakturering.
Tillåt redigering fakturabelopp
Om underlaget för fakturering ska få redigeras kan du ange detta här.
Kräv extern kommentar
Här anger du om extern kommentar ska vara obligatorisk i samband med faktureringen.
Fakturering Travel
Allmänt
I Travel är det lite klurigare att hitta vart man kopplar på dimensionen KUND och vilken dimension som ska användas för prissättning.
Det vanligaste alternativet är att använda dimensionen Artikel för att styra vilka bilersättningar, traktamenten och utlägg som ska faktureras och prissättas.
Artiklar och Kund kopplas sedan till de utlägg man vill fakturera.
Vad gäller bil- och traktamentesersättningar så kopplar man Kund och Artikel direkt på de lönearter som ska används för bilersättningar och traktamanten
Exempel Artiklar
Skapa artiklar för respektive typ som skall faktureras.
Om vissa utlägg inte ska faktureras bör man lägga upp en Artikel som aldrig kan faktureras.
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_3428807a.png)
De utlägg som ska faktureras måste också ha KUND och Artikel för att få med priset (om man inte valt att koppla kund på exempelvis ett projekt). Eftersom man oftast vill fakturera exakt det pris/belopp som anställd angivit så anger man inget fast belopp på artikel.
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_d600f63d.png)
Exempel Utlägg
Exempel utlägg Parkering - ska alltid faktureras
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_4e7f5378.png)
Exempel utlägg Kontorsmaterial - ska aldrig faktureras
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_9223d2c3.png)
Exempel Bilersättningar
Artikel MIL
Om man exempelvis vill fakturera 4 kr/km
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_8a203dd9.png)
Löneart 732 skattepliktig milersättning
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_bdf8fa2e.png)
Exempel Traktamenten
Artikel TRAKT
Om man exempelvis vill fakturera 350 kr/natt. Anger man inget pris så faktureras samma belopp som anställd får utbetalt
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_09e55e92.png)
Löneart 760 skattefritt traktamente
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_e57f1c57.png)
Exempel Reseräkning med ovanstående exempel
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_2fbfb6e7.png)
Trakt 350 kr/natt
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_dc991f8f.png)
Bilersättning 4 Kr/Km
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_18231d4d.png)
Utlägg kontorsmaterial faktureras inte (ingen fakturabock)
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_0907e1df.png)
Utlägg parkering 200 kr
![Bild](images/hur-aktiverar-jag-funktionen-fakturering-i-hrm-travel_0d5604f8.png)
Tips! Om du vill läsa mer om fakturering
Klicka här
