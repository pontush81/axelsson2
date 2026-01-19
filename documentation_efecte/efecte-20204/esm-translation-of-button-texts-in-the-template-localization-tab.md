# ESM: Translation of button texts in the Template Localization tab

**Källa:** https://community.efecte.com/t/x2h82lv/esm-translation-of-button-texts-in-the-template-localization-tab
**Publicerad:** 2020-08-21T08:48:46.773Z
**Uppdaterad:** 2020-08-21T10:48:46.773000
**Författare:** 

---

ESM: Translation of button texts in the Template Localization tab

      
    
          
      

        
              Aki Koivukoski
            

            R&D
              Aki_Koivukoski
            5 yrs agoFri, August 21, 2020 at 10:48 AM GMT+2
  

          1reply
        Peter Schneider5 yrs agoMon, November 2, 2020 at 12:09 PM GMT+1
  
         Done
        

        
    
 User story: As a system administrator, I want to be able to translate button texts such as "New comment" or "Reserve ticket" for different user languages in order to use one tool across borders.  
 ACs:  
 
 The button text for Handlers (Worklog, TextNote, TicketReserve) must be possible to translate in Localization Tab directly as a next row for the corresponding attribute translation. If a translation for user selected language exists in Localization Tab, it should be shown on the UI in the handler related button for that user. Otherwise the system defined value should be shown. 
 For the CategoryDropDown handler all the AC 1. rules apply if attribute metadata "Reserve: Attribute path to support person data card" is defined 
 For the Expression handler the AC 1. applies if attribute metadata "showButton" is set to true 
 The attribute metadata showButtonNewEntity and showButtonTransform button texts must be possible to translate in Localization Tab directly as a next row for the corresponding attribute translation. 
 
 NOTE!   
 ESM: Localization Support for Attributes (2020.4.) is a story that will create the Localization tab. This feature will build on it. 
          
    
        Service Management Tool
      
    
  
  Vote
  Follow
