# ESM: Multi-Language Support for Static Values of String Attributes

**Källa:** https://community.efecte.com/t/m1hm8t9/esm-multi-language-support-for-static-values-of-string-attributes
**Publicerad:** 2020-11-02T11:18:23.717Z
**Uppdaterad:** 2020-11-02T12:18:23.717000
**Författare:** 

---

ESM: Multi-Language Support for Static Values of String Attributes

      
    
          
      

        
              Peter Schneider
            

            Chief Evangelist / Storyteller
              Peter_Schneider
            5 yrs agoMon, November 2, 2020 at 12:18 PM GMT+1
  

          2replies
        Peter Schneider5 yrs agoMon, November 9, 2020 at 1:49 PM GMT+1
  
         Done
        

        
    
ContentsUser story:ACs:User story: 
 As a system administrator, I want to be able to translate the static values of attributes for different languages in order to use one tool across borders.  
ACs: 
 
 Static values shall also be listed in the translation table directly after the related attribute (one row for each static value) 
   
   Order of attribute-related translations: attribute name, help text, header, footer, button texts if any, static value 1 ... static value n 
   Static values are indented to show they belong to the attribute above 
   Static values are illustrated with the glyphicons-basic-101-text icon 
   Translations should be included in the template import and export, in template-wide as well as system-wide exports/imports as well dedicated translation table downloads 
    
 Translations should be shown to the users on the list view and detail datacard view according to their selected language 
   
   Admin side (system configuration) & automation should always use the system value 
    
 
 Note: Graphs, Calendar View, Kanban Board, and Visual Analyser do not need to display static values in translated form.  
 Note: Condition filters may be translated as part of this story if it does not need additional development, but it is out of the scope of this story. 
          
    
        Service Management Tool
      
    
  
  Vote
  Follow
