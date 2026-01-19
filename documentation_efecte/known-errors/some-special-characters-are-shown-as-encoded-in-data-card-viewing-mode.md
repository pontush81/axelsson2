# Some special characters are shown as encoded in data card viewing mode

**Källa:** https://community.efecte.com/t/p8hsdyc/some-special-characters-are-shown-as-encoded-in-data-card-viewing-mode
**Publicerad:** 2022-11-28T11:07:33.653Z
**Uppdaterad:** 2022-12-07T09:52:38.737000
**Författare:** 

---

Some special characters are shown as encoded in data card viewing mode

      
    
          
      

        
              Katriina PassilaEfecte Employee
            

            
              Katriina_Passila
            updated 3 yrs agoWed, December 7, 2022 at 9:52 AM GMT+1
  

          2replies
        Jonne KaukoProduct Manager2 yrs agoMon, May 22, 2023 at 12:43 PM GMT+2
  
         Fixed
        

        
    

      
          

    
        
        
        
      

    

   The following bugs have been identified in ESM 2022.4 release: CP-7143: Character & is encoded in data card viewing mode to '& amp' When using the '&' character on any data card, it will show as '&amp;' in viewing mode. CP-7184: ESM fails to recognize scandinavian special letters from Gateway messages Comments that originate from Gateway otherwise get sent to ESM fine except Scandinavian special letters do not. The letter 'ä' for example gets replaced with '&#228;'  
 These bugs are targeted to be fixed in the ESM 2023.1 release. 
          
    
        Known Error
      
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            2

## Bilder

![Bild](images/some-special-characters-are-shown-as-encoded-in-data-card-viewing-mode_01d7e2db.jpg)


