# ⚙️Hur ställer man in ett dagschema?

**Datum:** den 26 september 2025  
**Kategori:** Time  
**Underkategori:** Tidrapportering  
**Typ:** config  
**Svårighetsgrad:** advanced  
**Tags:** frånvaro, schema, stämpling, tidkod, tidrapport, övertid  
**Bilder:** 1  
**URL:** https://knowledge.flexhrm.com/sv/schema-dagsschema-hur-st%C3%A4ller-man-in-ett-dagsschema

---

En förklaring av dagschemats inställningar.
Att bygga scheman i HRM
Alla personer bör ha ett schema kopplat till sig. Det kan vara ett publikt eller ett personligt schema. Schemat kan innehålla tider eller vara tomt (endast lediga dagar).
Processen för att bygga scheman i HRM startar med
dagscheman
som du sedan kopplar ihop till ett
personligt
eller
publikt schema
.
Publika scheman
skapas för att förenkla schemaprocessen om många har samma typ av schema. Ett publikt schema kan t.ex. vara heltid 07:00-16:00.
I det publika schemat bygger du ett grundschema som sedan rullar på under året. Detta kan vara en cykel på 1-2 veckor eller mer. Du kan bygga flera grundscheman och byta dessa under året i det publika schemat.
Du behöver inte skapa nya dagscheman för varje pass. Du kan återanvända dagscheman och justera arbetstiderna direkt i det publika/personliga schemat.
Inställningar för ett dagschema
Dagscheman ställs in per tidgrupp. Dagschemat sätter reglerna för hur tidrapporten ska behandla registrerad arbetstid.
Alla scheman bygger på att man i grunden har ett dagschema för arbetsdag och ett dagschema för ledig dag.
![Bild](images/hur-staller-man-in-ett-dagschema_e66232f9.png)
Dagscheman har följande inställningar:
Kod
Namn
Dagschemat är aktivt
Normal arbetstid
Tidkod för normal arbetstid.
Denna tidkod faller ut om du inte anger någon tidkod i tidrapporten samt vid stämpling av tid. Utelämnas tidkod för normal arbetstid på dagschemat tas den istället från tidgruppens standardtidkod för arbetstid.
Flexfönster schemastart och Flexfönster schemaslut.
Här anges tillåtet intervall för flextid. Lämna blankt om flextid inte ska användas.
Fast värde.
Används om flexramarna ska vara låsta till angivna klockslag.
Exempel
:
Ett dagschema har arbetstid 8-17 och flexfönster vid schemastart 7-9. I det publika schemat använder jag dagschemat, men ändrar starttiden till kl 8:30. Utan bock i "Fast värde" förskjuts flexramen med arbetstiden, och sätts till 7:30-9:30. Med bock i "Fast värde" är flexramen 7-9, trots att arbetstiden ändrats.
Minsta arbetstid och Max arbetstid.
Används för att sätta gränser för hur mycket tid som behöver registreras när dagschemat används. Det kan t.ex. användas för dagscheman med stora flexramar, där man vill att ett minsta antal timmar arbetstid ska registreras.
Fast värde.
Används om minsta/max arbetstid ska vara låst, och inte korrigeras om man ändrar arbetstiden när dagschemat används.
Raster.
Raster kan läggas in på fasta klockslag, en viss tid efter schemats starttid eller en viss tid efter instämpling.
Exempel
:
Bilden ovan visar en rastregel. Den säger att rast kan registreras mellan kl 11 och 14. Om man inte registrerar rast kommer 60 minuter rast läggas ut kl 12-13, pga Föreslå-inställningarna. Registrerar man t.ex. 20 min rast kommer 10 min till att läggas ut, pga Min-inställningen (minsta antal minuter). Registrerar man mer än 60 minuter rast genereras en avvikelse för avvikande rast (pga Max-inställningen).
Generera ospecificerad tid.
Tidrapporten visar ospecad närvaro/frånvaro om man bryter mot dagschemats regler. Det kan handla om tid som registrerats utanför arbetstid och flexramar. Det markeras som ospecad närvaro, som en påminnelse om att tiden behöver specas, t.ex. som övertid. Bockar man ur denna inställning kan man bryta mot dagschemats regler utan att tidrapporten visar ospecad tid.
Händelser
. Används för att ange en formel som ska gälla när dagschemat används, t.ex. att en extra ersättning ska utfalla.
Stämplingstoleranser
. Används för att stämplad tid ska avrundas till schematid, eller till flexramen om man använder flextid.
Läs mer om stämplingstoleranser.
Relaterade artiklar
Hur skapar man ett publikt schema?
Hur skapar man ett personligt schema?
