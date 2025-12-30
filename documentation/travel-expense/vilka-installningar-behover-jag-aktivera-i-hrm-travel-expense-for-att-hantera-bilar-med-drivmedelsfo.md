# ⚙️Vilka inställningar behöver jag aktivera i HRM Travel & Expense för att hantera bilar med Drivmedelsförmån?

**Datum:** den 29 december 2025  
**Kategori:** Travel & Expense  
**Underkategori:** Reseräkningar  
**Typ:** config  
**Svårighetsgrad:** advanced  
**Tags:** bil, resa  
**Bilder:** 19  
**URL:** https://knowledge.flexhrm.com/sv/vilka-inst%C3%A4llningar-beh%C3%B6ver-jag-aktivera-i-hrm-travel-expense-f%C3%B6r-att-hantera-bilar-med-drivmedelsf%C3%B6rm%C3%A5n

---

Förutsättningar
Definition förmånsbilar
Med förmånsbil avser vi här en tjänstebil där drivmedlet betalas av företaget och den anställde blir förmånsbeskattad på de privat körda milen med drivmedelsförmån.
Fliken Bilar i Personalregistret
Den anställde måste ha en bil som är ikryssad med ”Drivmedelsförmån”. Det är även tvingande att ange Körjournal fr.o.m, Reg-nummer samt ingående mätarställning (km).
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_8422b652.png)
För att systemet ska veta hur förmånsvärdet ska beräknas måste beräkningssätt ställas in under Inställningar – Resa – Bilresor - Generellt
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_4db9b63a.png)
Fakturabelopp
Om Fakturabelopp används kan förmånsvärdet variera lite månad för månad, beroende på inköp och antal privata mil. Däremot blir det ju alltid rätt sett ur faktisk kostnad. Med detta beräkningssätt kommer systemet att räkna ut förmånsvärdet enligt formeln Antal privata milTotal antal körda mil×Fakturabelopp x 1.2. Således krävs att fakturabeloppet för perioden har matats in innan fullständig avräkning av bilen kan göras.
Genomsnittligt pris/l
Används Genomsnittligt pris tittar systemet på de värden som är angivna för bilens förbrukning och genomsnittligt pris/l i Personalregistret.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_2ac219f2.png)
Om företaget har många tjänstebilar av samma typ med samma förbrukning kan man ange priset på respektive fordonstyp. Detta för att slippa ändra på flertalet anställda med samma biltyp. Under Inställningar – Resa – Bilresor - Fordonstyper kan man ange olika priser per månad som då slår igenom på alla anställda som är kopplade till denna fordonstyp
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_e1deb4bf.png)
Registrera körda mil
Man kan välja vart man vill registrera sina bilresor med förmånsbil. Väljer man Körjournal är det enbart i denna vy man kan registrera bilresor. Vid valet ”Transaktionsvy” är det enbart i den vanliga reseräkningsvyn man kan registrera sina bilresor. Vid valet Transaktionsvy kan man trots det se sina bilresor i vyn Körjournal men inte ändra/ta bort eller skapa en ny.
Gör valet under Inställningar – Resa - Bilresor – Generellt
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_38a3242a.png)
Transaktionsvy
Här rapporteras de körda milen som vanligt i en reseräkning. Har den anställde mer än en bil gäller det att välja rätt bil. Om det bara finns en förmånsbil angiven i personalregistret kommer den att användas som default.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_c38db7b9.png)
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_fa9aad7b.png)
När sträckan matas in ändras automatisk utgående mätarställning. Det går bra att ange utgående mätarställning i stället och då räknas sträckan fram automatiskt.
När alla månadens resor är rapporterade är det viktigt att alla reseräkningar som har körda mil i perioden är klarmarkerade innan avräkning av förmånsbil kan ske.
Separat Körjournal
I vyn Körjournal väljer man först rätt bil och sedan rätt datumintervall innan man börjar registrera en ny bilresa.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_7b749dfd.png)
Klicka på Ny för att starta registreringen av en ny bilresa. Fyll i uppgifterna och spara.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_d7a5ad38.png)
När alla månadens resor är rapporterade är det viktigt att alla reseräkningar som har körda mil i perioden är klarmarkerade innan avräkning av förmånsbil kan ske.
Avräkning
Registrera utgående mätarställning – Avräkning förmånsbil
Den anställde kan själv avräkna sin förmånsbil och klarmarkera den. Innan avräkningen sker bör fakturabeloppet ha angivits för perioden för att säkerställa att det blir ett förmånsvärde på de privata milen. Saknas fakturabeloppet går det ändå bra att klarmarkera.
Oavsett vilken vy man har registrerat sina bilresor i (transaktionsvyn eller körjournalsvyn) så görs registreringen av utgående mätarställning och avräkningen i Körjournalsvyn
Börja med att välja den bil som ska avräknas. Ange utgående mätarställning per den siste i den aktuella månaden. Spara och klarmarkera. Saknas fakturabelopp ges en varning om detta.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_3c2e361c.png)
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_73697bdc.png)
Registrera Fakturabelopp
För att färdigställa avräkningen behöver administratören ange fakturabeloppet för perioden under Bearbetningar - Registrering av drivmedelsfakturor.
Skapa en ny faktura genom att klicka på ”Mata in nya drivmedelsfakturor”.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_8e9af4aa.png)
Alla anställda med förmånsbil dyker upp i massregistreringen. Ange rätt fakturabelopp till rätt anställd och klicka på Utför.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_2a9dc482.png)
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_1503c26e.png)
Klicka Ja
Avräkningen är slutförd och en drivmedelsförmån har skapats
Förmånsbeloppen registreras mot de lönearter man angivit under Inställningar – Resa – Bilresor - Fordonstyper
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_fe018a15.png)
Attest av Körjournalen
I attestvyn syns en ikon för körjournalen för den anställde.
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_ee2c3f4e.png)
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_58cac534.png)
Klicka på ikonen för att kontrollera körjournalen. Om fakturabeloppet är inmatat ser vi nu värden i Summering. Klicka på ”Avräkning förmånsbil” för attest/godkännande alternativt gå tillbaks till attestvyn och attestera/godkänn där
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_12808f26.png)
![Bild](images/vilka-installningar-behover-jag-aktivera-i-hrm-travel-expense-for-att-hantera-bilar-med-drivmedelsfo_34a21ff4.png)
