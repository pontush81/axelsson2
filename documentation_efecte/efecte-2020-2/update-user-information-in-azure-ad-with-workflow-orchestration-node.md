# Update user information in Azure AD with workflow orchestration node

**Källa:** https://community.efecte.com/t/35hh8wx/update-user-information-in-azure-ad-with-workflow-orchestration-node
**Publicerad:** 2020-02-28T10:15:01.470Z
**Uppdaterad:** 2020-04-01T08:27:47.757000
**Författare:** 

---

Update user information in Azure AD with workflow orchestration node

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            updated 5 yrs agoWed, April 1, 2020 at 8:27 AM GMT+2
  

           Done
        

        
    
 User Story:   
 As a Administrator I want to have orchestration Activity - Update user information in Azure AD with event based provisioning from ESM visual workflow. ACs:  
 
 The administrator must be able to add an activity "Update user information in Azure AD" for the Efecte Provisioning Engine in the orchestration node of the visual workflow automation 
 Efecte Provisioning Engine have means to set/update values for the user attributes for existing users in Azure AD  
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 ESM shall log an error in ITSM log if orchestration activity was timed out 
 If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration 
 
 Note: Updating user password would be managed via own orchestration activity 
          
    
        IGA
      
    
        EPE
      
    
  
  Vote
  Follow
