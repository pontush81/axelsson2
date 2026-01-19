# EPE: Group lifecycle management for AD & AAD (Verify, Create, Update, Delete)

**Källa:** https://community.efecte.com/t/60hlrdk/epe-group-lifecycle-management-for-ad-aad-verify-create-update-delete
**Publicerad:** 2021-03-26T08:54:05.390Z
**Uppdaterad:** 2021-03-26T09:54:05.390000
**Författare:** 

---

EPE: Group lifecycle management for AD & AAD (Verify, Create, Update, Delete)

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            4 yrs agoFri, March 26, 2021 at 9:54 AM GMT+1
  

           Done
        

        
    
 Story:  
 As an Administrator I want to have orchestration Activities - for verify, create, update and delete group to identity repositories by event based provisioning from ESM visual workflow.  
 ACs:  
 
 Visual Workflow Automation have Orchestration node group verification  
 Orchestration node must have Provisioning Engine-related activity: Verify Group 
   
   provisioning engine has functionality to verify if group exists or not 
   attribute for making the check/verification is configurable 
   from the verification workflow node admins are able to configure the attributes which will be used to verify if the group exists or not 
    
 The administrator must be able to add an activities 
   
   Create new group to chosen user repository 
   Update group information to chosen user repository 
   Delete group from the chosen user repository 
   for the Efecte Provisioning Engine in the orchestration node of the visual workflow automation 
    
 Efecte Provisioning Engine have means to 
   
   set values for creating new groups  
   update values for existing groups 
   delete existing groups 
    
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 If Provisioning Engine responds with exception, EPE must provide information to provisioning exception attribute in ESM 
 
  
 Note:  
 This provides technical capabilities for Efecte Provisioning Engine and we are planning to develop "Automated Entitlement Lifecycle Management" -functionalities part of the Efecte Identity Governance and Administration solution in Q3 / 2021 
          
    
        EPE
      
    
        IGA
      
    
  
  Vote
  Follow
    
            1
