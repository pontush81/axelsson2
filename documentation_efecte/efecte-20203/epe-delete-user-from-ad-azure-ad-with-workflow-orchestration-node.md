# EPE: Delete user from AD / Azure AD with workflow orchestration node

**Källa:** https://community.efecte.com/t/x2hx7cw/epe-delete-user-from-ad-azure-ad-with-workflow-orchestration-node
**Publicerad:** 2020-07-15T10:26:13.863Z
**Uppdaterad:** 2020-08-07T06:58:49.267000
**Författare:** 

---

EPE: Delete user from AD / Azure AD with workflow orchestration node

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            updated 5 yrs agoFri, August 7, 2020 at 6:58 AM GMT+2
  

           Done
        

        
    
 User Story:  
 As a Administrator I want to have orchestration Activity - Delete user from AD &  Azure AD with event based provisioning from ESM visual workflow.  
 ACs:  
 
 The administrator must be able to add an activity "Delete user" for the Efecte Provisioning Engine in the orchestration node of the visual workflow automation 
   
   This activity is available for datasources AD and Azure AD 
    
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 ESM shall log an error in ITSM log if orchestration activity was timed out 
 If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration 

          
    
        IGA
      
    
        EPE
      
    
  
  Vote
  Follow
