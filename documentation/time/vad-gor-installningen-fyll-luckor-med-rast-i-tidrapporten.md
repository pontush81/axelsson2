# ⚙️Vad gör inställningen “Fyll luckor med rast i tidrapporten”?

**Datum:** den 19 mars 2026  
**Kategori:** Time  
**Underkategori:** Tidrapportering  
**Typ:** config  
**Svårighetsgrad:** advanced  
**Tags:** frånvaro, schema, tidkod, tidrapport  
**Bilder:** 0  
**URL:** https://knowledge.flexhrm.com/sv/vad-g%C3%B6r-inst%C3%A4llningen-fyll-luckor-med-rast-i-tidrapporten

---

Inställningen är användbar för er som importerar tidrader via API. Importerar ni endast den arbetade tiden kan systemet lägga ut rast i luckor mellan tidraderna, om dagschemat har en rastregel som täcker samma tid.
I HRM Time kan du förenkla tidrapporteringen genom att låta systemet automatiskt fylla ut tomma tidsintervall med rast. Detta är särskilt användbart om du importerar tidrader, till exempel mellan 08:00–12:00 och 13:00–17:00. Utan den här inställningen lämnas perioden 12:00–13:00 tom, men med funktionen aktiverad skapar vi automatiskt en rad för rast i det intervallet.
Här aktiverar du inställningen
Du kan välja att aktivera funktionen för hela företaget eller för specifika tidgrupper:
För hela företaget: Gå till
Inställningar
>
Tid och Bemanning
>
Tidrapporter
.
För en specifik tidgrupp: Gå till
Inställningar
>
Tid och Bemanning
>
Tidgrupper
.
Förutsättningar för att rast ska läggas ut
För att systemet automatiskt ska fylla luckor med rast behöver följande fyra punkter vara uppfyllda:
Rutan
Fyll luckor med rast i tidrapporten
ska vara markerad.
Dagschemat behöver ha ett rastfönster som täcker den aktuella luckan.
Det måste finnas en tidrad både före och efter luckan som ligger i anslutning till ett och samma rastfönster.
Den tidkod som används för rasten måste vara av typen
Frånvaro - Rast
.
