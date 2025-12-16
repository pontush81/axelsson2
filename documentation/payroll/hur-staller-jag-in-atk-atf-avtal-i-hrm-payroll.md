# ⚙️Hur ställer jag in ATK/ATF avtal i HRM Payroll?

**Datum:** den 15 december 2025  
**Kategori:** Payroll  
**Underkategori:** Löneberedning  
**Typ:** config  
**Svårighetsgrad:** advanced  
**Tags:** lön, löneart, pension  
**Bilder:** 7  
**URL:** https://knowledge.flexapplications.se/hur-st%C3%A4ller-jag-in-atk/atf-avtal-i-hrm-payroll

---

Denna artikel går igenom de inställningar som ligger till grund för hanteringen av ATK/ATF via funktionen i HRM Payroll.
Relaterade artiklar:
Inställningar av lönearter för ATK/ATF avtal
ATK/ATF – Avtal
Den första byggstenen för att sätta upp ATK/ATF är att lägga upp ett avtal som håller de grundläggande reglerna enligt ditt kollektivavtal. Du kan skapa fler olika avtal om du har olika grupper av anställda som berörs av olika regler. Inställningarna för avtalen hittar du under
Administration > Inställningar > ATK/ATF-avtal.
Det kan också vara så att du istället behöver en anpassad lösning med hjälp av tidstransaktioner, lönearter och ackumulatorer (för t.ex. avtal som har sammanfallande intjänande/uttag kan
inte
funktionen med ATK/ATF-avtal användas då dessa endast beräknar släpande intjänande.)
OBS!
Om du är osäker på hur du ska konfigurera ditt ATK- eller ATF-avtal så att det stämmer med ert kollektivavtal, rekommenderar vi att du tar hjälp av en konsult från Flex Applications.
Fliken
Allmänt
Namn
Namnge ditt avtal så det är enkelt att förstå vilka det gäller.
Beskrivning
Här kan du ange en utförlig beskrivning för avtalet.
Avtalet är aktivt
Om du inaktiverar ett avtal kommer det inte längre gå att välja detta avtal i anställdaregistret eller på personalkategorier. Om det finns anställda eller personalkategorier som redan använder detta avtal, kommer de fortsätta ha avtalet tills dess att du byter ut det mot ett annat. Du kan alltså inaktivera ett avtal som du inte vill ska användas samt avtal som du vill ska fasas ut.
Avtalstyp
Här anger du om avtalet är av typen
Arbetstidskonto (ATK)
eller
Arbetstidsförkortning (ATF).
Se första avsnittet i denna instruktion för mer info.
Intjänandeår
Det finns i dagsläget endast stöd för att välja föregående år som intjänandeår. Det innebär att de anställda först tjänar in till ATK/ATF under en 12-månadersperiod, och därefter kan börja ta ut sina intjänade pengar/timmar. Om man har ett kollektivavtal med ATF där intjänandet och uttaget ska ske löpande kan man hantera detta i Flex HRM Time. Se första avsnittet i denna instruktion för mer info.
Startdatum för intjänande
Här anger du den månad och dag som intjänandet börjar. Vanligt är 1 januari eller 1 april. Tänk på att det är kontantprincipen som tillämpas för intjänandet. Om avtalet intjänandeperiod t.ex. börjar 1 januari kommer intjänande av ATK/ATF som finns i lönekörningen med utbetalning i januari räknas in även om lön och arbetad tid avser december månad föregående år.
Startdatum för uttag
Här anger du den månad och dag som den anställde med uttag som betald ledig tid kan börja ta ut sin ledighet.
Avsättning i % (ATK)
Om avtalet är av typen ATK anger du här hur många procent av löneunderlaget som ska avsättas till arbetstidskontot.
Avsättning min/vecka
Om avtalet är av typen ATF anger du här hur många minuter per vecka en heltidsanställd tjänar in till saldot för arbetstidsförkortning. I vissa kollektivavtal anges det hur många timmar per år en heltidsanställd ska tjäna in. Då får man omvandla dessa timmar till motsvarande antal minuter per vecka. Fördelen med att arbeta med antal minuter per vecka är att man kan hantera heltidsanställda, deltidsanställda, långtidsfrånvarande och de som inte varit anställda under hela året på samma sätt. Se avsnittet för
Löpande intjänande – ATF
för mer info.
Avrundningsregel för timmar (hela året)
För avtal av typen ATF används denna för att avrunda de intjänade timmarna när ett helt intjänandeår är fullbordat och flyttas till valperiod när man kör rutinen för att påbörja en ny intjänandeperiod. För avtal av typen ATK används denna för att avrunda de beräknade timmarna vid uttag som betald ledig tid.
![Bild](images/hur-staller-jag-in-atk-atf-avtal-i-hrm-payroll_5fe2741e.png)
Du kan välja avrundning, sänkning och höjning. I rutan till höger anger du noggrannheten. Anger du ”1,00” sker avrundning till närmaste hel timme. Anger du ”0,50” sker avrundning till närmaste halvtimme. Samma princip gäller för höjning och sänkning.
Gräns för timmar beroende på heltidsarbetsmått
Här anger du den övre gränsen för antal timmar. För ATF innebär det ett tak för intjänandet som inte kan överskridas. För ATK innebär det ett tak vid beräkning av timmar. Om du tillämpar avtalet för olika grupper av anställda med olika heltidsarbetsmått kan du lägga upp olika tak i listan.
![Bild](images/hur-staller-jag-in-atk-atf-avtal-i-hrm-payroll_69b9b8d9.png)
Fliken Anställdes val
Valbara uttagsvarianter
Kryssa för ett eller flera av de typer av uttag som den anställde kan välja enligt ditt kollektivavtal. Om kollektivavtalet inte ger utrymme för valmöjlighet anger du det alternativ som ska tillämpas. Den anställde kommer då automatiskt få detta valt.
För pensionsavsättning kan du också välja för vilket åldersspann detta val ska finnas för. Det är vanligt att anställda över 65 inte får välja extra pensionsavsättning, och i vissa avtal får inte heller unga välja detta.
Tillåt att man fördelar val mellan flera uttagsvarianter (%-fördelning)
Det vanligaste är att anställda får ta ut hela sitt intjänande på samma sätt. Typ av uttag väljs då via en drop-down-lista enligt följande:
![Bild](images/hur-staller-jag-in-atk-atf-avtal-i-hrm-payroll_ed7fd2de.png)
I vissa avtal kan dock den anställde välja att fördela sitt uttag. Typ av uttag väljs då genom att man anger hur stor del man vill ta ut per typ. Nedan har man valt att ta ut hälften som kontant ersättning och hälften som betald ledig tid.
![Bild](images/hur-staller-jag-in-atk-atf-avtal-i-hrm-payroll_f99ae398.png)
Deadline för val
Här anger du när den anställde måste ha gjort sitt val som senast. Detta bör vara ett datum innan starten av uttagsperioden men absolut senast innan man ska köra rutinen för att verkställa val och påbörja ny uttagsperiod.
Standardval om den anställde inte gör ett val
Här kan du ange vad som ska hända om en anställd inte gör ett val i tid. Det kan också användas då man enligt kollektivavtalet inte kan välja, för att på så sätt slippa administrera valet för alla anställda.
Spara kvarvarande ledighet som understiger detta antal timmar till nästa uttagsperiod
I vissa avtal finns det möjlighet att spara outtagen ledighet till nästa uttagsperiod. Oftast handlar det om tid som understiger en arbetsdag. Du anger här det maximala antalet timmar som får sparas till nästkommande år (vanligtvis motsvarande en arbetsdag). Om en anställd vid uttagsperiodens slut har färre ledighetstimmar kvar kommer dessa automatiskt flyttas till den nya uttagsperioden. Om man har fler timmar kvar kommer rest-delen att flyttas till nästkommande uttagsperiod. Exempelvis om man anger ett gränsvärde på 8 timmar, och har 10 timmar kvar kommer 8 timmar betalas ut vid skiftet, och 2 timmar sparas till nästkommande uttagsperiod.
Ett villkor för att timmar får sparas är att man valt ledighet även nästkommande uttagsperiod. Annars betalas alla timmar ut vid skiftet. Vid anställning på deltid räknas gränsvärdet ner enligt sysselsättningsgraden som den anställde har vid uttagsperiodens start.
Betala ej ut kvarvarande pengar/timmar som understiger
I vissa situationer kan det bli en väldigt liten "slatt" kvar i saldot för ATK/ATF som bara känns konstig att betala ut till den anställde vid uttagsperiodens slut. Det kan ofta handla om några få ören som blir kvar då timpriset inte går exakt jämt ut på grund av öresutjämning. Man kan då använda denna nya inställning där man kan lägga in ett gränsvärde för när utbetalning ska ske.
![Bild](images/hur-staller-jag-in-atk-atf-avtal-i-hrm-payroll_05edcd06.png)
Fliken Skuldhantering
Denna används endast för avtal av typen ATF. Här anger du den formel för beräkning av timpris som ska användas vid skuldberäkning/utbetalning av slutlön av ATF-timmarna.
![Bild](images/hur-staller-jag-in-atk-atf-avtal-i-hrm-payroll_896e9a34.png)
Koppla standardavtal för ATK/ATF på Personalkategori
Under
Inställningar – Personalkategorier
kan du ange det ATK/ATF-avtal som ska gälla för alla anställda i personalkategorin.
![Bild](images/hur-staller-jag-in-atk-atf-avtal-i-hrm-payroll_fb6bb016.png)
