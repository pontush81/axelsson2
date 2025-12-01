# Hur genomför man rapportering till Collectum i Flex HRM Payroll?

**Datum:** den 26 september 2025  
**Kategori:** Payroll  
**Underkategori:** Löneberedning  
**Typ:** howto  
**Svårighetsgrad:** intermediate  
**Tags:** lön, pension  
**Bilder:** 14  
**URL:** https://knowledge.flexapplications.se/hur-genomf%C3%B6r-man-rapportering-till-collectum-i-flex-hrm-payroll

---

Denna artikel riktar sig till dig som omfattas av pensionsavtalet ITP och  ska lämna pensionsunderlag till Collectum, och den beskriver hur man gör den månatliga rapporteringen.
Skapa underlag
Komplettera och ta bort underlag
Kontrollera underlaget
Skapa fil för rapportering
Skicka in filen till Collectum
Löpande arbete för rapportering till Collectum
En gång per månad ska man rapportera pensionsgrundande lön samt påbörjade och avslutade anställningar för ITP1 och ITP2 till Collectum. Detta gör du i Flex HRM Payroll under
Lön > Pension
.
Läs mer om vilka inställningar som krävs för att kunna rapportera till  Collectum genom att klicka på länken:
Hur gör man inställningar för rapportering till Collectum i HRM Payroll?
Skapa underlag
Första steget i rapporteringen är att skapa ett underlag för månadens rapportering. Detta gör du genom att klicka på knappen
Ny
i knappraden.
![Bild](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_df67f65c.png)
Du väljer här Rapportering till Collectum samt datumen för den månad du vill rapportera löneunderlag för. Du kan också välja att göra urval på anställda om du skulle vilja.
![Bild visar popup-ruta för skapande av nytt underlag för Collectum med alla de urval man kan göra.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_33404fc9.png)
När du klickar på knappen
Skapa
påbörjas arbetet med att skapa underlag. När underlaget är skapat ser du underlaget med statusen satt som
Preliminär
i vyn.
![Bilden visar översikten av ett skapat underlag för Collectum.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_479d9110.png)
Komplettera och ta bort underlag
Om du hittat ett fel i underlaget kan du beräkna om underlaget för alla eller ett urval av anställda genom att klicka på knappen
Komplettera
och där göra önskat urval.
Du kan också ta bort ett underlag om du vill börja om från början eller inte längre vill ha underlaget sparat.
Kontrollera underlaget
Nästa steg är att kontrollera underlaget innan du skickar in uppgifterna till Collectum. Detta gör du genom att granska underlaget i vyn.
Överst i vyn väljer du vilken rapportering (om du har fler än Collectum) samt vilken redovisningsperiod du vill titta på. Tidigare redovisningar finns kvar och är enkelt tillgängliga.
![Bilden visar val av rapportering samt val av redovisningsperiod.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_cb40b5c3.png)
I översikten visas allt underlag som sammanställts och som kommer med i filen till Collectum. Listan är uppdelad per händelsetyp (nyanmälan, avanmälan och anmälan lön).
![Bilden visar översikten av underlaget till Collectum.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_b17e900d.png)
Ovanför översikten finns ett sökfält där du kan söka på olika uppgifter, såsom namn, personnummer, och rapporterad lön.
![Bilden visar sökfältet ovanför översikten.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_fc0fc313.png)
När underlaget är granskat markerar du underlaget som kontrollerat genom att klicka på knappen för detta i knappraden.
![Bilden visar knappen "Markera som kontrollerad".](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_cbdad67a.png)
Statusen på underlaget ändras då till
Kontrollerad
, vilket innebär att underlaget nu är låst för ändringar.  Datum, tid samt signatur för användaren som markerade underlaget som kontrollerat sparas ner på underlaget.
![Bilden visar fälten för Status, Datum och tid samt Signatur.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_6d15225b.png)
Om du hittar ett fel i ett kontrollerat underlag, kan du ta bort
![Bilden visar knappen för "Ta bort kontrollmarkering". ](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_918bdf9d.png)
kontrollmarkeringen igen. Då sätts statusen om till Preliminär, och du kan nu komplettera underlaget igen. När du därefter markerar underlaget som kontrollerat igen sätts en ny tidpunkt när underlaget blev kontrollerat för att du ska kunna se om filen som skickats in till Collectum är skapad från det senast uppdaterade underlaget.
Skapa fil för rapportering
![Bilden visar knappen "Skapa fil".](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_9cb4fb82.png)
När underlaget är markerat som kontrollerat kan du skapa filen för redovisning till Collectum. Detta gör du med knappen för
Skapa fil
i knappraden.
I dialogrutan som öppnas får du en tydlig översikt över vilken period som inkluderas i rapporteringsfilen. Under alternativet
Typ av fil
väljer du om filen ska användas för
Produktion
eller
Test
. Testfilen är särskilt användbar vid den första rapporteringen efter införandet och rekommenderas i samråd med Collectum, så att du kan säkerställa att processen fungerar korrekt innan skarp rapportering sker.
Här har du även möjlighet att välja vilken
Typ av ITP
som ska tas med i filen; du kan välja både ITP1 och ITP2, eller endast en av dem, beroende på vilka avtal som är aktuella inom företaget. Detta ger flexibilitet att anpassa rapporteringen efter din organisations specifika pensionslösningar och säkerställer korrekt information i rapporteringen till Collectum.
![Bilden visar dialogrutan för att skapa fil.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_085be1b2.png)
När filen är skapad visas information om detta högst upp på sidan. Om något fel upptäckts när filen skapades visas information om det. Du kan se mer detaljer om vad som är fel genom att öppna loggfilen. Exempel på fel är om personnummer saknas för en anställd. Du kan välja att ladda ner filen för rapportering genom att klicka på länken enligt bilden nedan.
![Bilden visar notiser med information om status samt resultatet av bearbetningen.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_e095140b.png)
Du kan också se och hämta filen för rapportering samt felloggar genom att klicka på knappen
Visa filer
i knappraden.
![Bilden visar knappen "Visa filer".](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_4488b36f.png)
Här finns filen kvar till dess att du väljer att ta bort den från listan. Filerna visas för det underlag du står på i vyn.
![Bilden visar dialogrutan för skapade filer för underlaget.](images/hur-genomfor-man-rapportering-till-collectum-i-flex-hrm-payroll_cea2c4f9.png)
Skicka in filen till Collectum
När filen är skapad i Flex HRM laddar du ner den enligt ovan och skickar in den till Collectum. Detta gör du genom att logga in på Collectums hemsida och där följa instruktionerna för rapportering via fil.
Relaterade artiklar:
Hur gör man inställningar för rapportering till Collectum i HRM Payroll?
