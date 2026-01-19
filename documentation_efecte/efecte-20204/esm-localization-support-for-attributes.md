# ESM: Localization Support for Attributes

**Källa:** https://community.efecte.com/t/p8hqjfb/esm-localization-support-for-attributes
**Publicerad:** 2020-02-04T09:34:50.910Z
**Uppdaterad:** 2020-08-07T06:57:08.673000
**Författare:** 

---

ESM: Localization Support for Attributes

      
    
          
      

        
              Peter Schneider
            

            Chief Evangelist / Storyteller
              Peter_Schneider
            updated 5 yrs agoFri, August 7, 2020 at 6:57 AM GMT+2
  

           Done
        

        
    
 User story: As a system administrator, I want to be able to translate attribute names for different languages in order to use one tool across borders.  
  ACs:  
 
 the template configuration must have translation table on a "Localize" -tab beside the "Content" and "Layout" -tabs for the template name and all attributes 
 the translation table should indicate different item types for ease of usage  
 the translation table shall include all supported configuration UI languages 
 administrators can localize the template name 
 administrators can localize the class name 
 administrators shall be able to enter a localized text for each attribute name 
 changes of the system attribute name shall not be possible in the translation table 
 Help texts shall also be listed in the translation table directly after the related attribute (truncated in the UI to some 100 characters for each table cell in the viewing mode with more space when editing the text) 
 Static values shall also be listed in the translation table directly after the related attribute (one row for each static value) 
 Attribute headers and footers can be localized (if there is a value in the system configuration there shall be a corresponding row in the translation table) 
 Translated attribute and class names shall be shown in detail view (use system names if no translation exists) 
 Translated template names shall be shown in More drop-down selection for "Transform to <localized template name>" 
 Translated texts shall be shown after browser reloading 
 Activating the configuration translations on the Admin Ui shall not disrupt ongoing activities in the Workspace UI 
 when the user changes preferred language in user profile then notification shall inform the user that the new language has been activated and the user shall reload the browser to activate the new language. 

          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            1
