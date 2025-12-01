# Automatisk hantering vid borttag av Visma Connect-koppling

**Datum:** den 21 november 2025  
**Kategori:** Systemgemensamt  
**Underkategori:** Mobil  
**Typ:** other  
**Svårighetsgrad:** intermediate  
**Tags:** användare, mobil, säkerhet  
**Bilder:** 0  
**URL:** https://knowledge.flexapplications.se/automatisk-hantering-borttag-visma-connect

---

När en anställd slutar i företaget tas kopplingen till Visma Connect bort automatiskt. Artikeln beskriver hur den här funktionen fungerar i Flex HRM.
Inloggning till Flex HRM och HRM Mobile sker via
Visma Connect
. För att en användare ska kunna logga in måste hen vara kopplad till Visma Connect med en e-postadress.
När anställningen avslutas tas kopplingen till Visma Connect bort.
Så fungerar den automatiska borttagningen
Funktionen är kopplad till den befintliga säkerhetsinställningen
Inaktivera konto x dagar efter avslutad anställning
. När en anställds anställningsdatum har passerat och antalet dagar för inaktivering har uppnåtts, kommer systemet automatiskt att ta bort kopplingen till Visma Connect.
Processen sker via ett bakgrundsjobb, vilket innebär att borttagningen inte sker omedelbart, utan när bakgrundsjobbet körs nästa gång.
Vad behöver du göra?
För att ni ska kunna dra nytta av denna automatisering så smidigt som möjligt har vi gjort det enkelt för er.
Om du redan använder automatisk inaktivering:
Du behöver inte göra någonting. Processen sköts helt automatiskt. Systemets standardinställning är att ett konto inaktiveras fem dagar efter avslutad anställning. Om ni har angett ett annat antal dagar, i
säkerhetsinställningen
eller i
användarmallar
, så är det de inställningarna som gäller.
För redan inaktiverade användare:
Användare vars konton redan var inaktiverade när funktionen lanserades påverkas inte automatiskt. För dessa behöver du ta bort kopplingen manuellt i användarregistret.
Vid manuell inaktivering:
Om du manuellt inaktiverar en användare direkt i användarregistret kommer kopplingen till Visma Connect inte att tas bort automatiskt. I dessa fall behöver du använda knappen
Ta bort koppling
för att avsluta åtkomsten manuellt.
Ett tips för återkommande anställningar
Har du medarbetare som återkommer med jämna mellanrum? Då kan det vara praktiskt att skapa en separat användarmall för dessa användare. I mallen anger du ett högre antal dagar för inaktivering, så att användaren behåller sin Visma Connect-koppling en längre tid mellan anställningarna och ni slipper återaktivera den manuellt.
