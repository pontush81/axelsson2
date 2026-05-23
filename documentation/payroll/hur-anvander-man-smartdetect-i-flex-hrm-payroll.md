# Hur använder man SmartDetect i Flex HRM Payroll?

**Datum:** den 22 maj 2026  
**Kategori:** Payroll  
**Underkategori:** Löneberedning  
**Typ:** howto  
**Svårighetsgrad:** advanced  
**Tags:** lön, löneart, semester, skatt  
**Bilder:** 7  
**URL:** https://knowledge.flexhrm.com/sv/hur-anv%C3%A4nder-man-smartdetect-i-flex-hrm-payroll

---

Den här artikeln visar hur du praktiskt arbetar med SmartDetect i din dagliga löneberedning för att hitta avvikelser samt säkerställa en smidig och korrekt process.
Hitta och granska avvikelser i löneberedningen
Arbeta med avvikelser - Från varning till åtgärd
Ge feedback och gör SmartDetect smartare!
Exempel på vad SmartDetect hittar
Tips för ett effektivare arbetsflöde
Hitta och granska avvikelser i löneberedningen
SmartDetect är helt integrerat i din arbetsvy för att du snabbt ska kunna agera.
Leta efter den röda pricken: Högst upp i löneberedningen finns knappen
Avvikelser
.
![Bilden visar knappen för Avvikelser.](images/hur-anvander-man-smartdetect-i-flex-hrm-payroll_e2619698.png)
När systemet har hittat något som behöver din uppmärksamhet visas en tydlig röd prick på knappen.
SmartDetect är uppdelad i två huvudflikar:
Kontroller:
Här hittar du alla regelbaserade kontroller där systemet vet till 100 % att något sticker ut, till exempel en negativ nettolön. Dessa är beräknade kontroller som du kan åtgärda direkt i löneberedningen. För varje kontroll visas antalet anställda som behöver kontrolleras och eventuellt åtgärdas.
I listvyn för regelbaserade kontroller ser du exakt vad systemet kontrollerar. Varje kontroll visar en tydlig status:
Checkbox:
Inga fel hittades.
Gul varningstriangel:
Fel har identifierats som behöver ses över.
Du ser också direkt hur många anställda som berörs av respektive avvikelse. För kontroller med varningar kan du fälla ut en detaljerad lista som visar vilka anställda det gäller samt specifik löneart och rad om det är tillämpligt.
![Bild](images/hur-anvander-man-smartdetect-i-flex-hrm-payroll_938a29b5.png)
Potentiella fel:
I denna flik samlas de avvikelser som SmartDetects AI-funktion har hittat. Det är insikter som bygger på mönsteranalys och som hjälper dig att upptäcka "kanske-fel" som annars är lätta att missa.
Du kan klicka på en anställd direkt i SmartDetect-listan för att öppna personen i löneberedningen. När du har åtgärdat felet triggas en ny beräkning automatiskt, och panelen uppdateras så snart beräkningarna är klara.
Vyn
i
nnehåller följande kolumner:
Kryssruta:
Med de
nna funktion kan du
markera raden
i listan som hanterad och samtidigt
skicka feedback till AI-modellen som hjälper den att ge bättre
resultat nästa gång. Läs mer om hur denna fungerar
längre ned i artikeln
.
Anställd:
Här visas vilken anställd avvikelsen gäller. Klicka på namnet för att öppna personen i löneberedningen.
Rad:
Om avvikelsen är kopplad till en lönerad ser du här vilken rad det gäller
Avvikelse:
Här ser du en kortfattad beskrivning av vad avvikelsen gäller. Notera att vi här beskriver vad som avviker, och inte varför.
Löneart:
Om avvikelsen är kopplad till en löneart ser du här vilken löneart det gäller.
![Bilden visar en översikt av avvikelselistan som visar till höger i löneberedningen.](images/hur-anvander-man-smartdetect-i-flex-hrm-payroll_6610fa0e.png)
Arbeta med avvikelser
Följ dessa enkla steg för att beta av listan med Avvikelser:
Välj en avvikelse
: Klicka på den anställdes namn i listan. Personens lönebesked öppnas då direkt i huvudfönstret i löneberedningen.
Analysera:
Bedöm om avvikelsen är ett faktiskt fel eller en korrekt men ovanlig händelse (t.ex. en hög bonus).
Åtgärda:
Om det är ett fel rättar du det som vanligt. När du sparar gör SmartDetect en ny analys, och avvikelsen försvinner från listan om felet är löst.
Ge feedback och gör SmartDetect smartare!
Om en avvikelse inte beror på ett fel kan du ge feedback. Detta lär AI-motorn vad som är viktigt för dig. Markera raden i listan genom att bocka i kryssrutan i den första kolumnen och välj ett av alternativen längst ner:
En avvikelse men utan åtgärd:
Välj detta om avvikelsen var relevant, men korrekt den här gången. Du talar då om för AI:n att den ska fortsätta registrera avvikelser för liknande händelser.
Ej en avvikelse:
Välj detta om avvikelsen är irrelevant. AI:n lär sig då att tona ner liknande avvikelser i framtiden.
![Bilden visar avvikelselistan med en markerad ruta för en avvikelse samt två knappar att välja mellan för att ge feedback med.](images/hur-anvander-man-smartdetect-i-flex-hrm-payroll_f1fef6ae.png)
Efter du har markerat och valt ett av feedbackalternativen ovan, försvinner avvikelsen från listan. Men, det går att se vilka avvikelser du har hanterat genom att bocka i rutan för
Visa hanterade avvikelser
. Dessa dyker då upp i listan igen, men då är bockrutan för dem utgråad.
![Bilden visar funktionen "Visa hanterade avvikelse" och hur den kan visa dessa avvikelser i listan.](images/hur-anvander-man-smartdetect-i-flex-hrm-payroll_e17e70ce.png)
Exempel på vad SmartDetect hittar
SmartDetect kombinerar AI med fasta regler och kan varna för bland annat:
Transaktioner och skatt:
Ovanligt höga/låga belopp, saknade lönearter, felaktigt eller saknat skatteavdrag samt negativa löner.
Saldon i osynk:
Felaktiga ingångsvärden som inte stämmer överens med utgående värden från föregående lönekörning på ackumulatorer, semester- eller ATK/ATF-saldon.
Frånvaro och ledighet:
Överuttag av semesterdagar, föräldraledighet utan kopplat barn eller frånvaro som sträcker sig över felaktiga perioder.
Övrigt:
Anställda som har slutat men där slutlön inte är hanterad.
Du kan läsa mer om vilka avvikelser som SmartDetect kan hitta i artikeln
Vad kan SmartDetect varna för i Flex HRM Payroll?
Tips för ett effektivare arbetsflöde
Sortera:
Klicka på kolumnrubrikerna för att sortera listan, till exempel per anställd.
![Bilden visar kolumnrubrikerna i avvikelselistan och hur man kan tryck apå någon av dem för att sortera listan.](images/hur-anvander-man-smartdetect-i-flex-hrm-payroll_1d6f2f82.png)
Sök:
Använd sökfältet för att snabbt hitta en specifik anställd, löneart eller varning.
![Bilden visar sökfunktionen i avvikelselistan.](images/hur-anvander-man-smartdetect-i-flex-hrm-payroll_630f3cb4.png)
Relaterade artiklar:
Vilka inställningar krävs för att man ska kunna använda SmartDetect
i Flex HRM Payroll?
Vad kan SmartDetect varna för i Flex HRM Payroll?
