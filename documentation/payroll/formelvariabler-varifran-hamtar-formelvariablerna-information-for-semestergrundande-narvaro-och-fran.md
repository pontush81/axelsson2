# Formelvariabler - Varifrån hämtar formelvariablerna information för semestergrundande närvaro och frånvaro i HRM Payroll?

**Datum:** den 24 oktober 2025  
**Kategori:** Payroll  
**Underkategori:** Semesterhantering  
**Typ:** other  
**Svårighetsgrad:** advanced  
**Tags:** lön, löneart, semester  
**Bilder:** 0  
**URL:** https://knowledge.flexhrm.com/sv/formelfunktioner

---

Artikeln förklarar varifrån Flex HRM hämtar information om närvaro och frånvaro som räknas som semestergrundande.
Formelvariabler för Närvaro/Frånvaro
Formelvariabler är de värden som används i beräkningar, till exempel hur många dagar som är semestergrundande. De hämtar sin information från olika delar av systemet, som t.ex. kalendariet eller lönearter.
Formel variabel
Hur hämtas det?
SemGrFrvDgr
Semestergrundande frånvaro från kalendariet (tar inte med ej semestergrundande tid). Tar inte med frånvaroorsaker som har bocken ”
Räkna denna frånvaro som närvaro för semesterberäkning
”. Innebär att schema krävs.
SemGrFrvKdgr
Semestergrundande frånvaro från kalendariet (tar inte med ej semestergrundande tid). Tar inte med frånvaroorsaker som har bocken ”
Räkna denna frånvaro som närvaro för semesterberäkning
”. Innebär att schema krävs. Räknar heltidfrånvaro OCH deltidsfrånvaro som hel kalenderdag. Ex: Föräldraledig 50% = 1 kalenderdag.
SemGrFrvTim
Semestergrundande frånvaro från kalendariet (tar inte med ej semestergrundande tid). Tar inte med frånvaroorsaker som har bocken ”
Räkna denna frånvaro som närvaro för semesterberäkning
”. Innebär att schema krävs.
SemGrArbTim
Timmar från alla transaktioner som har löneart med boken ”
Semestergrundande arbetstid
” i löneartsregistret + all frånvaro i kalendariet med frånvaroorsak som har bocken ”
Räkna denna frånvaro som närvaro för semesterberäkning
”. Schema krävs endast för att lägga på frånvaro från kalendariet.
Bock på lönearten krävs för att få med t.ex. övertid som inte finns som schematid.
SemGrArbDgr
Alla dagar med schematid - All frånvaro i kalendariet med frånvaroorsak som inte har bocken ”
Räkna denna frånvaro som närvaro för semesterberäkning
”. Innebär att schema krävs.
Hänsyn tas till omfattning
Om man har 2 stycken olika frånvarotillfällen på en hel dag. Den första är semestergrundande 50% och den andra ej semestergrundande 50%, tas det hänsyn till omfattning, d.v.s. semestergrundande frånvarodagar blir 0.5.
