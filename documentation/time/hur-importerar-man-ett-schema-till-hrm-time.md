# ⚙️Hur importerar man ett schema till HRM Time?

**Datum:** den 29 september 2025  
**Kategori:** Time  
**Underkategori:** Schema & Planering  
**Typ:** config  
**Svårighetsgrad:** intermediate  
**Tags:** frånvaro, hrm-time, ob, schema, tidkod  
**Bilder:** 7  
**URL:** https://knowledge.flexapplications.se/hur-importerar-man-ett-schema-till-hrm-time

---

Om man önskar importera scheman till anställd från annat system till HRM Time så kan man använda importmallen "Schema"
Allmänt Schemaimport
Du importerar alltså schema per anställd och datum, vilket innebär att de fälten är obligatoriska. Utöver detta finns det mängder av möjligheter till import, t.ex. att enbart importera med schemastart,schemaslut och rastlängd. Då skapas automatiskt en rast mitt i schemat.
Dock finns möjligheter att importera i stort sett allt du kan göra med en anställds schema på en dag i HRM. Nedan visas de fält som är valbara i importmallen. Observera att vissa kräver licens för HRM Plan.
Det du importerar kommer att skapa en manuell schemaändring per anställd och dag och alltså motsvara manuella ändringar gjorda här:
![Bild](images/hur-importerar-man-ett-schema-till-hrm-time_3bfd8de0.png)
Om filen innehåller två arbetspass så bör man använda "Fyll luckor med rast". Men för att det ska fungera behöver det finnas en standardtidkod för rast (frånvaro rast) i den aktuella tidgruppen, annars kommer ingen rast att skapas.
![Bild](images/hur-importerar-man-ett-schema-till-hrm-time_962f353c.png)
Observera att anställd måste vara kopplat till en tidgrupp.
Exempel på olika schemaimportmallar
schema med datum och dagschema
![Bild](images/hur-importerar-man-ett-schema-till-hrm-time_943a0141.png)
*Schema med datum och klockslag
![Bild](images/hur-importerar-man-ett-schema-till-hrm-time_ef780c34.png)
Schema utan klockslag
![Bild](images/hur-importerar-man-ett-schema-till-hrm-time_dea6cd78.png)
Schema med endast dagschema
![Bild](images/hur-importerar-man-ett-schema-till-hrm-time_3071b202.png)
Schema Quinyx
![Bild](images/hur-importerar-man-ett-schema-till-hrm-time_1c19d460.png)
