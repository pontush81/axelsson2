# Reset user password in AD and Azure AD with workflow orchestration node

**Källa:** https://community.efecte.com/t/y4h3y28/reset-user-password-in-ad-and-azure-ad-with-workflow-orchestration-node
**Publicerad:** 2020-05-12T13:51:30.307Z
**Uppdaterad:** 2020-05-12T15:51:30.307000
**Författare:** 

---

Reset user password in AD and Azure AD with workflow orchestration node

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            5 yrs agoTue, May 12, 2020 at 3:51 PM GMT+2
  

           Done
        

        
    
 User Story:  
 As a Administrator I want to have orchestration Activity - Reset user password with event based provisioning from ESM visual workflow.  
 ACs:  
 
 Provisioning Engine must have activity to reset user password 
   
   Activity is available for both Microsoft AD and Azure AD 
    
 The Service Management Tool has an orchestration node in the Visual Workflow Automation to reset user password 
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 ESM shall log an error in ITSM log if orchestration activity was timed out 
 If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration 

          
    
        IGA
      
    
        EPE
      
    
  
  Vote
  Follow
