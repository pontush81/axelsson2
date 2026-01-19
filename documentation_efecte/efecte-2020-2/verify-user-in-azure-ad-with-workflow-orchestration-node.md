# Verify user in Azure AD with workflow orchestration node

**Källa:** https://community.efecte.com/t/60hh8dv/verify-user-in-azure-ad-with-workflow-orchestration-node
**Publicerad:** 2020-02-28T10:09:40.670Z
**Uppdaterad:** 2020-02-28T11:09:40.670000
**Författare:** 

---

Verify user in Azure AD with workflow orchestration node

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            5 yrs agoFri, February 28, 2020 at 11:09 AM GMT+1
  

           Done
        

        
    
 User story:  
 As a Administrator I want to have orchestration Activity - Verify if user exists in Azure AD,  event based provisioning from ESM visual workflow.  
 ACs:  
 
 ESM Visual Workflow Automation have Orchestration node for user verification in Azure AD 
 Provisioning engine has functionality to verify if user exists or not 
   
   Attribute for making the check/verification is configurable 
   From the verification workflow node admins are able to configure the attributes which will be used to verify if the user exists or not 
    
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 ESM shall log an error in ITSM log if orchestration activity was timed out 
 If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration 

          
    
        IGA
      
    
        EPE
      
    
  
  Vote
  Follow
