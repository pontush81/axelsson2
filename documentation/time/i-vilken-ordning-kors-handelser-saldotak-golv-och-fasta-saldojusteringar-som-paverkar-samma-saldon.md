# ⚙️I vilken ordning körs händelser, saldotak/-golv och fasta saldojusteringar som påverkar samma saldon?

**Datum:** den 26 september 2025  
**Kategori:** Time  
**Underkategori:** Saldon & Beräkning  
**Typ:** config  
**Svårighetsgrad:** intermediate  
**Tags:** ob, saldo, tidrapport  
**Bilder:** 0  
**URL:** https://knowledge.flexapplications.se/i-vilken-ordning-k%C3%B6rs-h%C3%A4ndelser-saldotak/-golv-och-fasta-saldojusteringar-som-p%C3%A5verkar-samma-saldon

---

I HRM Time finns det en bestämd ordning för hur händelser, saldotak/-golv och fasta saldojusteringar körs, vilket är viktigt om de påverkar samma saldon. Ordningen ser ut så här:
Fasta saldojusteringar
körs först.
Händelser
körs sedan.
Saldotak/-golv
körs sist.
Observera
Med
fasta saldojusteringar
menas allt som ställs in i vyn
Fasta saldojusteringar.
Med
saldotak/-golv
menas det som ställs in under knappen
Saldotak/-golv
under
Tidrapporter
,
Tidgrupper
eller
Anställda
.
Exempel
För
es
täll dig att du har en händelse som lägger till intjänad ATF (arbetstidsförkortning) varje månad, och dessutom en fast saldojustering som begränsar ATF-saldot till max 100 timmar i slutet av december.
I december tjänar du in 5,2 timmar ATF. Både intjänandet och justeringen ska ske den 31 december.
Eftersom den fasta saldojusteringen körs först, blir ditt utgående saldo 105,2 timmar istället för 100 (om du var över taket). Om du istället vill att saldot ska vara max 100 timmar vid årsskiftet, är det bättre att ställa in så att den fasta saldojusteringen utförs i början av januari.
Relaterade artiklar
Hur fungerar fasta saldojusteringar?
Saldotak/-golv - Hur sätter man gränser för saldovärden?
Hur använder man Händelser i HRM Time?
