# ESM: Multiple Language Configuration for List and Detail Datacard View

**Källa:** https://community.efecte.com/t/q6hqjfr/esm-multiple-language-configuration-for-list-and-detail-datacard-view
**Publicerad:** 2020-02-04T09:12:44.797Z
**Uppdaterad:** 2020-08-07T06:57:28.530000
**Författare:** 

---

ESM: Multiple Language Configuration for List and Detail Datacard View

      
    
          
      

        
              Peter Schneider
            

            Chief Evangelist / Storyteller
              Peter_Schneider
            updated 5 yrs agoFri, August 7, 2020 at 6:57 AM GMT+2
  

          2replies
        Peter Schneider5 yrs agoWed, September 16, 2020 at 6:26 AM GMT+2
  
         Done
        

        
    
 User story: As a administrator, I want to use Service Management tool in multiple languages because I cannot maintain the configuration data in different tenants.  
  Use case: A customer wants to run IT Service Desks in multiple European countries using the same configuration and sharing support person resources across teams based on language skills. The performance reporting of all service desks shall be possible in one service management tenant. The list views and detail dardcard views must be able to display the configuration texts in the language selected by the user. Translations of the configuration shall be context-orientated i.e. close to the configuration itself (instead of translations in an external tool) in order to achieve a high quality of translations. All existing systems shall upgrade to the new configuration translation support without customer interaction and therefore the translations shall be built as an additional layer on top of the existing configurations and automation. Hence, existing automation such as handlers and listeners will work as is even after the upgrade to the multi-language support. Only the displayed values, which are the result of the automation shall be determined according to the user language preferences. The Administration UI will remain to work in the system language only. In one possible evolution of the multi-language support, the content of the records shall be automatically translated to the support person's user language. Using an open-source translation algorithm, subject fields, description fields, and other string fields shall be translated automatically based on the support person's language or to one system language such as English, French, or German. 
          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            1
