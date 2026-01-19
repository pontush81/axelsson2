# EIM searches should include wildcards automatically when searching

**Källa:** https://community.efecte.com/t/m1h3850/eim-searches-should-include-wildcards-automatically-when-searching
**Publicerad:** 2020-05-15T12:10:21.870Z
**Uppdaterad:** 2020-05-15T14:10:21.870000
**Författare:** 

---

EIM searches should include wildcards automatically when searching

      
    
          
      

        
              Eetu HeinoProduct Manager
            

            
              Eetu_Heino
            5 yrs agoFri, May 15, 2020 at 2:10 PM GMT+2
  

           Done
        

        
    
 Searches in UI will use wildcards automatically. Users do not need to enter wildcards to the search strings. Text field searches use the following logic in general. * characters are added to the beginning and and end of the string, meaning that searching for text 'rm' is converted to '*rm*' search string. Space characters are converted to * characters. If you use any * characters in the search string then the search text is not further modified. Exact search can be done by adding double quotes to the beginning and end of the text. Bare empty string is converted to *. The changes affect only the UI layer. External APIs, such as REST API are not changed. Wizard hidden option handling is not changed. 
          
    
        Identity Management
      
    
  
  Vote
  Follow

## Bilder

![Bild](images/eim-searches-should-include-wildcards-automatically-when-searching_6e06668e.png)


