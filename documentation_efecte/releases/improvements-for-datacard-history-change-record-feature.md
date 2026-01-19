# Improvements for Datacard history/change record feature

**Källa:** https://community.efecte.com/t/m1ypm2l
**Publicerad:** 2025-12-16T08:52:37.660Z
**Uppdaterad:** 2025-12-16T09:59:55.733000
**Författare:** 

---

Improvements for Datacard history/change record feature

      
    
          
      

        
              Tommi Ekholm
            

            
              Tommi_Ekholm
            updated 1 mth agoTue, December 16, 2025 at 9:59 AM GMT+1
  

          1reply
        Peter Scheffczyk6 days agoMon, January 12, 2026 at 5:24 PM GMT+1
  
        

        
    
Hi,
Story:
as an Efecte admin, I want to ensure that our database doesn't get too bloated and thus affect the performance.
We get data from n+1 sources to Efecte, some of which update daily due to changes in master databases. We have 50+k user cards, 15+k computer cards, on top of other assets/datacards. Their lifespan can vary from 4 to 10 years even.
As an admin I have a an option to either opt-in or opt-out. On, Off. 
Having used Efecte for ~10 years now, the database has grown. Right now the only option is to manually delete the history cards from the database with queries. Mostly one-off deletions and/or cronjob-like automated scripts on the server (which is not very user friendly, requires manual labor and can be risky). There might be a need to keep some templates data card change history for 2 months, for some 2 years.
Suggestion:
Option to select lifespan of the history records on the template. E.g. 
"Record changes of data cards: Yes/no" (as it is now a tick box on the template)
If selected Yes
"Delete data records older than: <number field>" (in months for example)
This way the efecte admin could easily maintain the database and keep it in better shape.
          
    
        Administration
      
    
        Templates
      
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            9
