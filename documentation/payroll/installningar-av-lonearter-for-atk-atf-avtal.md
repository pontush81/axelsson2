# ⚙️Inställningar av lönearter för ATK/ATF avtal

**Datum:** den 15 december 2025  
**Kategori:** Payroll  
**Underkategori:** Inställningar  
**Typ:** config  
**Svårighetsgrad:** advanced  
**Tags:** agi, lön, löneart, pension  
**Bilder:** 32  
**URL:** https://knowledge.flexapplications.se/inst%C3%A4llningar-av-l%C3%B6nearter-f%C3%B6r-atk/atf-avtal

---

För att hantera uttag av betald ledighet, kontant ersättning, pensionsavsättning samt utbetalning av kvarvarande ledig tid när uttagsåret är slut behöver du ett antal lönearter. Du behöver också lönearter för hantering av slutlön. Nedan beskriver vi hur dessa lönearter kan sättas upp. Observera att dessa kan behöva anpassas till just ditt kollektivavtal.
Relaterade artiklar:
Inställningar av ATK/ATF avtal
Lönearter för ATK
Lönearter för ATF
Systemfasta lönearter
Lönearter för ATK
370 - Arbetstidskonto, kontant ersättning
Lönearten används för anställda som valt att få utbetalt som kontant ersättning.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_b6edd66c.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för pengar och timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_ab6c3e48.png)
Lönearten ska inte ha någon formel.
371 - Arbetstidskonto, pensionsavsättning
Lönearten används för anställda som valt att få extra avsättning till pension.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_505cab5f.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för pengar och timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_90df48e7.png)
Lönearten kan behöva en koppling till ytterligare en löneart (se exempel löneart 376) med formel om man enligt avtal ska räkna upp avsättningen till pension och önskar göra denna uppräkning i löneberedningen i samband med verkställandet.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_edb829f4.png)
372 - Arbetstidskonto, betald ledighet
Lönearten används för anställda som valt att ta ut som betald ledig tid.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_a17e8b3d.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för pengar och timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_602998ae.png)
Du behöver också lägga in en formel för beräkning av A-pris för en ledig timme. Normalt räknas timpriset som intjänade pengar delat på intjänade timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_d7b8e4fa.png)
373 - Arbetstidskonto, utbetalning
Lönearten används för anställda som inte tagit ut all betald ledig tid när uttagsperioden är slut. Vid start av ny uttagsperiod används denna löneart för utbetalning av kvarvarande pengar/timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_f16a281f.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för pengar och timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_a6fdbef7.png)
Lönearten ska inte ha någon formel.
376 – Arbetstidskonto, ATK pension uppräkning
Lönearten används för anställda som valt att få extra avsättning till pension, för att lägga till en uppräkning på intjänat belopp.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_2e5958b8.png)
Lönearten behöver inte markeras för att minska saldot för ATK/ATF och behöver inte ha någon enhet under fliken Lön.
Du behöver lägga in en formel för beräkning av uppräkningen (i nedan exempel räknas intjänat belopp från löneart 371 upp med 5,76%).
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_fcfbe593.png)
563 - Slutlön arbetstidskonto intjänandeperiod
Lönearten används för utbetalning av intjänandeperiodens intjänade belopp vid slutlön.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_f4e104e1.png)
Lönearten behöver inte markeras för att minska saldot för ATK/ATF eller ha någon formel.
564 - Slutlön arbetstidskonto uttagsperiod
Lönearten används för utbetalning av uttagsperiodens kvarvarande belopp vid slutlön.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_e5f3c097.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för pengar och timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_4087cf12.png)
Lönearten ska inte ha någon formel.
565 - Slutlön arbetstidskonto valperiod
Lönearten används för utbetalning av valperiodens intjänade belopp vid slutlön.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_770ee52d.png)
Lönearten behöver inte markeras för att minska saldot för ATK/ATF eller någon formel.
Lönearter för ATF
350 - Arbetstidsförkortning, kontant ersättning
Lönearten används för anställda som valt att få utbetalt som kontant ersättning.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_1739f0bf.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_8f43b5ef.png)
Lönearten behöver en formel för uträkning av timpris enligt kollektivavtalets beräkning. I exemplet nedan används månadslön och en divisor.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_f134c5da.png)
351 - Arbetstidsförkortning, pensionsavsättning
Lönearten används för anställda som valt att få extra avsättning till pension.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_8613b971.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_ea4ead72.png)
Lönearten behöver en formel som räknar ut hur stor pensionsavsättning som ska göras av de intjänade timmarna enligt kollektivavtalet.
352 - Arbetstidsförkortning, betald ledighet
Lönearten används för anställda som valt att ta ut som betald ledig tid.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_040ea117.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_4bd23459.png)
Lönearten behöver en formel för uträkning av timpris enligt kollektivavtalets beräkning. I exemplet nedan används månadslön och en divisor.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_10c2c4ce.png)
Tänk på att om du har månadsavlönade behöver du också en löneart för avdrag när man tar ut ATF som ledighet enlig samma princip som t.ex. sjukavdrag.
353 - Arbetstidsförkortning, utbetalning
Lönearten används för anställda som inte tagit ut all betald ledig tid när uttagsperioden är slut. Vid start av ny uttagsperiod används denna löneart för utbetalning av kvarvarande timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_695dde6d.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_9c697a90.png)
Lönearten behöver en formel för uträkning av timpris enligt kollektivavtalets beräkning. I exemplet nedan används månadslön och en divisor.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_7185ea29.png)
560 - Slutlön arbetstidsförkortning intjänandeperiod
Lönearten används för utbetalning av intjänandeperiodens intjänade timmar vid slutlön.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_8404099b.png)
Lönearten behöver inte markeras för att minska saldot för ATK/ATF eller någon formel.
561 - Slutlön arbetstidsförkortning uttagsperiod
Lönearten används för utbetalning av uttagsperiodens kvarvarande timmar vid slutlön.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_707c0522.png)
På fliken
Lön
ställer du in att lönearten ska minska saldo för timmar. Enheten på lönearten ska vara timmar.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_51869b4e.png)
Lönearten ska inte ha någon formel.
562 - Slutlön arbetstidsförkortning valperiod
Lönearten används för utbetalning av valperiodens intjänade timmar vid slutlön.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_4e183f66.png)
Lönearten behöver inte markeras för att minska saldot för ATK/ATF eller någon formel.
Systemfasta lönearter
För att systemet ska kunna generera lönetransaktioner i samband med årsskiftesrutiner samt vid slutlön behöver man ange vilka lönearter som ska användas till vad under
Administration – Inställningar – Systemfasta lönearter.
De markerade med rött nedan används för ATF, och de markerade med grönt används för ATK. Löneartsnumren i exempelbilden är de som beskrivits i föregående avsnitt.
![Bild](images/installningar-av-lonearter-for-atk-atf-avtal_3593101f.png)
