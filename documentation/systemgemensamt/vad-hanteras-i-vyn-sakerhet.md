# ⚙️Vad hanteras i vyn Säkerhet?

**Datum:** den 17 oktober 2025  
**Kategori:** Systemgemensamt  
**Underkategori:** Användare & Behörighet  
**Typ:** config  
**Svårighetsgrad:** advanced  
**Tags:** användare, behörighet, integration, mobil, säkerhet  
**Bilder:** 0  
**URL:** https://knowledge.flexhrm.com/vad-hanteras-i-vyn-s%C3%A4kerhet

---

I vyn
Säkerhet
gör du inställningar som rör säkerheten för systemets användare.
Generell lösenordspolicy
Inloggning till Flex HRM och HRM Mobile sker via ett Visma Connect-konto. Det innebär att lösenordspolicyn styrs från Visma Connect. Den generella policyn i vyn
Säkerhet
gäller för intern autentisering, vilket används för HRM Timeclock och API.
I den generella policyn ställer du in regler för hur lösenord ska utformas, som längd och komplexitet, och om det ska vara möjligt att återanvända lösenord.
Inställningar för nya användare
I vyn kan du också ange standardinställningar för nyskapade användare:
Om de ska vara
Aktiva
.
Om de ska få inställningar för att aktiveras/inaktiveras i förhållande till sina anställningsdatum.
Observera
att andra inställningar för nya användare kan ärvas från en användarmall. Använder ni en sådan är det användarmallens inställningar som gäller.
API-inställningar
Under
API-inställningar
kan du ställa in om ni ska använda företagsspecifik behörighet för API och om kalenderintegrationen ska vara aktiv.
Kalenderintegration aktiv:
I Flex HRM kan du prenumerera på ditt schema och få det som en kalender i din kalenderapplikation (Google, Outlook, MacOS eller iPhone).
Eftersom anropen från kalenderapplikationerna går via HRM API, behöver du tillåta kalendrarna att anropa API:t genom att aktivera
Kalenderintegration aktiv
.
Domäninställningar för Visma Connect
Tillåtna domäner vid koppling till Visma Connect:
Denna inställning används för att styra vilka e-postadresser som får användas för
Koppling till Visma Connect
(användarregistret).
Om du anger en domän, till exempel "flexapplications.se", kan endast e-postadresser som tillhör den domänen sparas som e-post för Visma Connect.
Om ingen domän anges görs ingen sådan begränsning.
Verifierade domäner:
Här visas eventuella verifierade domäner.
Om ni har verifierade domäner skapas Visma Connect-konton automatiskt om du anger en e-postadress som tillhör domänen under
Koppling till Visma Connect
för en användare.
Har ni inte någon verifierad domän (eller om en annan e-postadress anges) skickas istället ett e-postmeddelande där användaren måste verifiera sig innan ett Visma Connect-konto skapas.
Du verifierar domäner i Visma Connect. Du ställer in vilka användare som ska ha behörighet att göra detta under
Behörigheter för autentiseringsinställningar
.
