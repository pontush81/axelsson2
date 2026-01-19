# User creation in Azure AD with workflow orchestration node

**Källa:** https://community.efecte.com/t/83hh8wy/user-creation-in-azure-ad-with-workflow-orchestration-node
**Publicerad:** 2020-02-28T10:11:32.173Z
**Uppdaterad:** 2020-02-28T11:11:32.173000
**Författare:** 

---

User creation in Azure AD with workflow orchestration node

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            5 yrs agoFri, February 28, 2020 at 11:11 AM GMT+1
  

          2replies
        Jukka PapinahoEfecte Employee5 yrs agoTue, May 26, 2020 at 1:12 PM GMT+2
  
         Done
        

        
    
 User Story:  
 As a Administrator I want to have orchestration Activity - Create a new user to Azure AD with event based provisioning from ESM visual workflow.  
 ACs:  
 
 Provisioning Engine must have activity to create new user to Azure AD 
 The Service Management Tool has an orchestration node in the Visual Workflow Automation that can create a new user in the Azure AD 
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 ESM shall log an error in ITSM log if orchestration activity was timed out 
 If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration 

          
    
        IGA
      
    
        EPE
      
    
  
  Vote
  Follow
    
            1
