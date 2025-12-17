# Vad är logiken bakom föreslagen kontering i dagvyn i HRM Time?

**Datum:** den 20 oktober 2025  
**Kategori:** Time  
**Underkategori:** Tidrapportering  
**Typ:** concept  
**Svårighetsgrad:** beginner  
**Tags:** frånvaro, hrm-time, mobil, ob, schema, tidkod, tidrapport  
**Bilder:** 0  
**URL:** https://knowledge.flexhrm.com/logiken-bakom-f%C3%B6reslagen-kontering-i-dagvyn-i-hrm-time

---

Här beskrivs vilka konteringar som har högst prioritet när konteringar genereras automatiskt i dagredovisningen. Manuellt angivna konteringar skrivs inte över.
Stämpelklockans konteringar
har högst prioritet och skriver över alla andra automatiskt genererade konteringar, även över föreslå senast använda kontering och över konteringar som kommer från bemanningen.
Konteringar från arbetspassen i bemanningen
skriver över alla tidigare utlagda konteringar, utom de från stämpelklockan.
Konteringar via plats i HRM Mobile
läggs ut om du använder funktionen "Föreslå konteringar via plats i HRM Mobile".
Frånvaro
kan få kontering från frånvarohanteraren.
Senast använda kontering
föreslås om du har aktiverat inställningen (
Inställningar > Tid och Bemanning > Tidrapporter
). Konteringen hämtas från den senaste tidraden där tidkoden får konteras.
Undantag:
Om du lägger ut tider enligt schema föreslås inte den senast använda konteringen för dessa rader.
Tidkodens konteringar.
Om projekt läggs ut från tidkoden har projektets konteringar högre prioritet än tidkodens övriga konteringar.
Tillfällig utlåning
gäller om ingen annan kontering (förutom hemkontering) har lagts.
Den anställdes hemkonteringar
läggs ut på de konteringsdimensioner där ingen annan kontering lagts, förutsatt att inställningen
Lägg ut hemkontering om blank
är ikryssad.
