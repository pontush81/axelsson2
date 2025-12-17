# Vad kan SmartDetect varna för i Flex HRM Payroll?

**Datum:** den 14 november 2025  
**Kategori:** Payroll  
**Underkategori:** Löneberedning  
**Typ:** other  
**Svårighetsgrad:** advanced  
**Tags:** lön, löneart, semester, skatt  
**Bilder:** 0  
**URL:** https://knowledge.flexhrm.com/vad-kan-smartdetect-varna-f%C3%B6r-i-flex-hrm-payroll

---

SmartDetect kontrollerar lönedata genom att hitta avvikelser för: avvikande värden på transaktioner, osynkade saldon, ogiltig frånvaro och missade slutlöner.
Här är ett urval av de kontroller och bevakningar som SmartDetect idag utför, utöver AI-analysen:
Transaktioner och skatt
Ovanliga värden: Reagerar på transaktioner där Antal, A-pris eller Belopp är högre eller lägre än vanligt.
Saknad löneart: Varnar om en specifik löneart som en anställd brukar ha saknas.
Skatteavvikelser: Kontrollerar om skatteavdrag saknas helt eller om skatten är betydligt högre eller lägre än normalt.
Negativa värden: Flaggar för negativ brutto- eller nettolön.
Saldon och ackumulatorer i osynk
Ackumulatorer: Säkerställer att ingående värden i den nya lönekörningen stämmer överens med utgående värden från den föregående.
Semestersaldon: Jämför att semestersaldon (ingående mot föregående körning samt aktuellt saldo mot anställdaregistret) är korrekta.
ATK/ATF-saldon: Utför motsvarande kontroller för arbetstidskonto/arbetstidsförkortning.
Frånvaro och ledighet
Överuttag av semester: Varnar om fler semesterdagar har registrerats än vad den anställde har kvar.
Föräldraledighet: Kontrollerar att en registrerad föräldraledighet är kopplad till ett barn i systemet.
Felaktiga perioder: Varnar om semester- eller ATK/ATF-transaktioner sträcker sig över flera perioder/semesterår eller ligger utanför giltiga datum.
Övriga kontroller
Slutlön: Uppmärksammar om en anställd har slutat men slutlön ännu inte har markerats som utbetald.
Arbetsgivarintyg-tr
ansaktioner: Uppmärksammar transaktioner som används för arbetsgivarintyg som har datum som sträcker sig över flera månader.
Varning vid flera anställningsperioder under löneperioden
Denna varning hjälper dig att upptäcka när en anställd har haft flera korta anställningsperioder under en och samma löneperiod. Detta är särskilt viktigt för timanställda, eftersom olika anställningsvillkor eller timlöner kan gälla för olika delperioder. En varning på löneraden signalerar att du kan behöva dela upp de arbetade timmarna per delperiod för korrekt beräkning.
Regel:
En varning utlöses om det finns fler än en anställningsperiod som överlappar med datumperioden på en lönetransaktion.
Varning för transaktionsdatum utanför anställningstid
Förhindra felaktig löneberäkning orsakad av inkorrekta datum. Om ett transaktionsdatum ligger utanför en anställningsperiod kan det leda till att viktig lönedata, som till exempel månadslön, saknas för perioden. Den här kontrollen säkerställer att alla tid- och lönetransaktioner är kopplade till en aktiv anställningsperiod.
Regel:
Du får en varning om någon dag i datumperioden på en lönetransaktion ligger utanför en anställningsperiod.
Varning vid låsta lönerader som påverkar retroaktiv lön
Att manuellt låsa en lönerad innebär att du har åsidosatt systemets beräkning och tvingat in t.ex. ett specifikt belopp.
Om denna rad är underlag för retroaktiv lön, kommer den automatiska
retroberäkningen inte att bli korrekt
. Denna varning gör dig uppmärksam på dessa rader, så att du kan granska dem manuellt och säkerställa att retroaktiv lön beräknas på ett korrekt sätt.
Regel:
Varning ges på en lönerad om den är låst
och
den kopplade lönearten är markerad som underlag för retroaktiv lön.
Varning om Bankkonto Saknas
Få en tidig signal om att en anställd saknar bankkontouppgifter. Detta ger dig god tid att komplettera informationen i personregistret innan det är dags för utbetalning, vilket minskar risken för missade eller försenade utbetalningar.
Regel:
Varning utlöses i löneberedningen om bankkonto saknas på en anställd.
Så här kommer du igång
Dessa varningar är tillgängliga för alla kunder som har en aktiv licens för
SmartDetect
. Varningarna visas direkt i
Flex HRM Payroll
under löneberedningen.
Relaterade artiklar:
Hur använder man SmartDetect i Flex HRM Payroll?
Vilka inställningar krävs för att man ska kunna använda SmartDetect
i Flex HRM Payroll?
