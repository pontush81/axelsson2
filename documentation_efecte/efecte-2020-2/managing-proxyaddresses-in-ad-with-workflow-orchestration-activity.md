# Managing proxyaddresses in AD with workflow orchestration activity

**Källa:** https://community.efecte.com/t/p8h3fct/managing-proxyaddresses-in-ad-with-workflow-orchestration-activity
**Publicerad:** 2020-05-22T05:47:13.110Z
**Uppdaterad:** 2020-05-22T07:47:13.110000
**Författare:** 

---

Managing proxyaddresses in AD with workflow orchestration activity

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            5 yrs agoFri, May 22, 2020 at 7:47 AM GMT+2
  

           Done
        

        
    
 User Story:  
  As a IGA administrator, I want to have own dedicated orchestration activity to manage proxyaddresses, because current functionality (using Update User orchestration activity) require complex configuration in the ESM side.  
 ACs:  
 - The administrator must be able to add an activity "Update / Set / Remove ProxyAddress" for the Efecte Provisioning Engine in the orchestration node of the visual workflow automation - Efecte Provisioning Engine have means to update/set/remove email address to proxyaddress values for the existing users in AD  - Efecte Provisioning Engine have means to identify correct user for executing the chosen activity - ESM shall continue workflow based on orchestration result from Provisioning Engine - ESM shall log an error in ITSM log if orchestration activity was timed out - If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration  
 Note: It's also possible to manage proxyaddresses with "Update user" orchestration activity,  but with this own activity we are able to handle project-specific use-case, which previously required more complicated Workflow solution. 
          
    
        IGA
      
    
        EPE
      
    
  
  Vote
  Follow
