# Hur beräknas underlaget för lönestrukturstatistik för privat sektor (SLP)?

**Datum:** den 7 oktober 2025  
**Kategori:** Payroll  
**Underkategori:** Löneberedning  
**Typ:** howto  
**Svårighetsgrad:** advanced  
**Tags:** lön, löneart, semester  
**Bilder:** 0  
**URL:** https://knowledge.flexhrm.com/hur-skapas-underlaget-f%C3%B6r-l%C3%B6nestrukturstatistik-f%C3%B6r-privat-sektor-slp

---

I denna artikel beskrivs beräkningen av underlaget för Lönestrukturstatistik (SLP), vilka anställda som ingår, fältberäkningar och hantering av avvikelser.
Vilka anställda tas med i underlaget?
Beräkning fält för fält
För dig med bruten redovisningsperiod
Avvikelser och tillägg för olika branscher
Vilka anställda tas med i underlaget?
Vilka som ska tas med i redovisningen framgår av instruktionerna från SCB/SN. Det gäller i stort sett alla anställda förutom ägare och VD.
Följande anställda tas med i Flex HRM Payroll:
personer i åldern 18 - 69 år (räknat från månaden man fyller)
anställda markerade som arbetare eller tjänsteman
anställda som haft arbetad tid under rapporteringsmånaden
Beräkning fält för fält
Nedan följer en detaljerad beskrivning av hur respektive fält beräknas.
Personnummer
Hämtas från anställdaregistret, fliken
Personuppgifter
.
Personalkategori
Hämtas från anställdaregistret, fliken
Lönestatistik
.
Arbetstidsart
Hämtas från anställdaregistret, fliken
Lönestatistik
.
Jobbstatus (gäller endast SN)
Hämtas från anställdaregistret, fliken
Lönestatistik
.
Yrkeskod (SSYK/NYK)
Hämtas från anställdaregistret, fliken
Lönestatistik
. Beroende på om man ska rapportera till SCB eller SN är det olika yrkeskoder som ska användas. Vid rapportering till SCB är det yrkeskoder enligt SSYK 2012 som ska läggas in. Vid redovisning till SN är det istället motsvarigheten NYK14 som ska användas.
Förbundsnummer (gäller endast SN)
Hämtas från anställdaregistret, fliken Lönestatistik. Finns inget angivet på personen hämtas det som angetts under
Administration > Inställningar > Lön > Lönestatistik
.
Avtalskod (gäller endast SN)
Hämtas från anställdaregistret, fliken Lönestatistik. Finns inget angivet på personen hämtas det som angetts under
Administration > Inställningar > Lön > Lönestatistik
.
Arbetsplatsnummer (gäller endast SN)
Fältet avser arbetsplatsnummer som företaget har hos Svenskt Näringsliv och hämtas från anställdaregistret, fliken Lönestatistik. Finns inget angivet på personen hämtas det som angetts under
Administration > Inställningar > Lön > Lönestatistik
.
Arbetsställe (CFAR)
Fältet avser arbetsställenummer som företaget har hos SCB och hämtas från anställdaregistret, fliken Lönestatistik. Finns inget angivet på personen hämtas det som angetts under
Administration > Inställningar > Lön > Lönestatistik
.
Anställningsform
1 = Tillsvidareanställd, 2 = Tidsbegränsad anställning. Uppgiften hämtas från anställningsformens typ i Flex HRM. Typen tillsvidareanställning och provanställning räknas som en tillsvidareanställning, övriga räknas som en tidsbegränsad anställning.
Löneform
Hämtas från anställdaregistret, fliken
Lön
.
Fast månads-, vecko- eller timlön
För anställda med löneformen månadslön hämtas den faktiska månadslönen (med hänsyn till sysselsättningsgrad) samt fasta lönetillägg som gällde under rapporteringsmånaden. Lönetilläggen hämtas från de egna numeriska fält som är markerade som lönetillägg. För anställda med löneformen timlön hämtas timlönen.
Arbetad tid
Summerar antal timmar från lönearter med kryss i löneartsregistrets fält ”Lönestrukturstatistik (SLP) - Arbetad tid” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Veckoarbetstid faktisk
Hämtas från anställdaregistret, fliken
Anställning
.
Veckoarbetstid heltid
Hämtas från anställdaregistret, fliken
Anställning
.
Mer- och övertidstimmar
Summerar antal timmar från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) - Mer- och övertidstimmar” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Övertidstillägg
Summerar belopp från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) - Övertidstillägg” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Övertidsersättning
Summerar belopp från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) - Övertidsersättning” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Tillägg vid skift, OB, förskjuten arbetstid
Summerar belopp från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) – Tillägg vid skift, OB, förskjuten arbetstid” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Jour, beredskap och förmåner
Summerar belopp från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) - Jour, beredskap och förmåner” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Därav förmåner
Summerar belopp från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) - Jour, beredskap och förmåner” och av typen Förmån som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Tillägg för speciella arbetsförhållanden
Summerar belopp från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) - Tillägg för speciella arbetsförhållanden” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Prestationslön, provision
Summerar belopp från lönearter med kryss i lönartsregistrets fält ”Lönestrukturstatistik (SLP) - Prestationslön, provision” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Semesterdagar
Avser semesterrätt och hämtas från anställdaregistret, fliken
Semester
.
För dig med bruten redovisningsperiod
Om du har en bruten redovisningsperiod som t.ex. för utbetalningen i oktober har arbetade timmar och avvikelser för perioden 15 september till 14 oktober kommer dessa transaktioner med i redovisningen för september på grund av att systemet hämtar alla transaktioner som har ett fr.o.m.-datum under redovisningsperioden.
Avvikelser och tillägg för olika branscher
För dig som lämnar in statistiken via en arbetsgivarorganisation finns det ofta lite olika avvikelser jämfört med den lagstadgade insamlingen till SCB som vi beskriver i detalj nedan.
Svenskt Näringsliv (SN) – FAO (MO 48)
För dig som tillhör Försäkringsbranschens arbetsgivarorganisation (FAO) och redovisar via SN behöver lägga in branschens egna befattningskoder, VY-koden, på varje anställd. Detta gör du i anställdaregistret, fliken
Lönestatistik
.
Svenskt Näringsliv (SN) – Installatörsföretagen (MO 25)
Här finns en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Svenskt Näringsliv (SN) – Biltrafikens arbetsgivarförbund (MO 31)
OB och skiftformstillägg fördelas även på följande tre delkomponenter:
Enkelt OB
Kvalificerat OB
Skiftformstillägg
Belopp för dessa tre delkomponenter summeras på lönearter med kryss för motsvarande fält som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Här finns också en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Svenskt Näringsliv (SN) – Grafiska Företagens Förbund (MO 38)
Här finns en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Svenskt Näringsliv (SN) – Plåtslageriernas Riksförbund (MO 42)
Här finns en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Svenskt Näringsliv (SN) – Industriarbetsgivarna - sågverksindustrier (MO 56 001)
Post- och ställningsersättning redovisas i ett separat fält. Summerar belopp från lönearter med kryss i fältet ”Lönestrukturstatistik (SLP) - Post- och ställningsersättning (Sågverksindustrin)” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Här finns också en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Denna medlemsorganisation har avvikande arbetstidsarter.
Svenskt Näringsliv (SN) – Industriarbetsgivarna - massa och pappersindustrier (MO 56 002)
Här finns en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Denna medlemsorganisation har avvikande arbetstidsarter.
Svenskt Näringsliv (SN) – Industriarbetsgivarna - gruvindustri (MO 56 003)
Här finns en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Denna medlemsorganisation har avvikande arbetstidsarter.
Svenskt Näringsliv (SN) – Industriarbetsgivarna - svets mekaniska avtalet (MO 56 004)
Här finns en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Denna medlemsorganisation har avvikande arbetstidsarter.
Svenskt Näringsliv (SN) – Industriarbetsgivarna - stål och metall (MO 56 005006)
Skiftformstillägg redovisas i ett separat fält. Summerar belopp från lönearter med kryss i löneartsregistret i fältet ”Lönestrukturstatistik (SLP) - Skiftformstillägg (Stål- och Metallförbundet)” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Här finns också en speciell hantering gällande överenskommen veckoarbetstid för anställda med arbetstidsarten Tvåskift. Anställda med veckoarbetstid 40 timmar redovisas som 38 timmar.
Svenskt Näringsliv (SN) – Kompetensföretagen (MO 87)
Här finns två förbundsspecifika fält:
Garantilön
Summerar belopp från lönearter med kryss i fältet ”Lönestrukturstatistik (SLP) - Garantilön (Kompetensföretagen)” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Utbokad tid
Summerar antal timmar från lönearter med kryss i fältet ”Lönestrukturstatistik (SLP) – Utbokad tid (Kompetensföretagen)” som har transaktionens fr.o.m.-datum under redovisningsmånaden. Transaktioner utan datum räknas tillhöra lönekörningens avvikelseperiods fr.o.m.-datum.
Denna medlemsorganisation har avvikande personalkategorier.
Sobona (tidigare KFS)
Alla över 18 år tas med i redovisningen till Sobona.
Relaterade artiklar:
Vilka inställningar krävs för att jag ska kunna rapportera statistik för
Lönestrukturstatistik för privat sektor (SLP) i Flex HRM Payroll?
Lönestrukturstatistik för privat sektor (SLP) - Hur tar jag fram statistik för
SLP i HRM Payroll?
