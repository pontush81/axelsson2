# ⚙️Hur fungerar Faktureringslogiken i HRM Time?

**Datum:** den 29 september 2025  
**Kategori:** Time  
**Underkategori:** Inställningar  
**Typ:** config  
**Svårighetsgrad:** intermediate  
**Tags:** hrm-time  
**Bilder:** 0  
**URL:** https://knowledge.flexhrm.com/hur-fungerar-faktureringslogiken-i-hrm-time

---

Hur fungerar funktureringslogiken i HRM Time avseende inställningarna Ja, Ja, Alltid, Nej, Nej Aldrig.
Faktureringslogik per tidrad:
1. Om inga konteringar finns registrerade ska fakturering aldrig ske.
2. Om någon kontering har värdet ”Nej Aldrig” ska fakturering aldrig ske, oavsett övriga värden.
3. Om någon kontering har värdet ”Ja Alltid” ska fakturering alltid ske, oavsett övriga värden.
4. Om någon kontering har värdet ”Ja” ska denna användas för fakturering.
5. Om inget av ovanstående är uppfyllt ska fakturering inte ske (”Nej”).
Tips! Om du vill läsa mer om Fakturering
Klicka här
