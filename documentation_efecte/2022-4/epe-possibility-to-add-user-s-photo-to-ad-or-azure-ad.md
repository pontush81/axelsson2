# EPE: possibility to add user's photo to AD or Azure AD

**Källa:** https://community.efecte.com/t/x2hn8sq/epe-possibility-to-add-users-photo-to-ad-or-azure-ad
**Publicerad:** 2022-08-12T07:06:44.760Z
**Uppdaterad:** 2022-08-12T09:06:44.760000
**Författare:** 

---

EPE: possibility to add user's photo to AD or Azure AD

      
    
          
      

        
              Tuija Länsisalmi
            

            
              Tuija_Lansisalmi
            3 yrs agoFri, August 12, 2022 at 9:06 AM GMT+2
  

           Done
        

        
    
 Story:  
 As a IGA owner I want to have orchestration node for adding photo for the users, when creating/updating a user to directory.  
  
 ACs:  
 
 ESM Visual Workflow Automation have Orchestration node for adding photo for the users. 
 Orchestration node must have Provisioning Engine-related activity: Add picture for the user 
   
   from the orchestration workflow node admins are able to configure the attribute which will be used to store user's photo 
   if the chosen field in the template doesn't have photo, then there should be error message shown: Photo doesn't exists in the chosen template 
    
 Workflow designers must be able to select Orchestration node from the activities palette 
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 ESM shall log an error in ITSM log if orchestration activity was timed out 
 If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration 

          
    
        EPE
      
    
        IGA
      
    
  
  Vote
  Follow
