# EPE: New Orchestration activity - Verify Group Membership

**Källa:** https://community.efecte.com/t/m1ht61z/epe-new-orchestration-activity-verify-group-membership
**Publicerad:** 2020-12-18T05:59:37.453Z
**Uppdaterad:** 2020-12-18T06:59:37.453000
**Författare:** 

---

EPE: New Orchestration activity - Verify Group Membership

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            5 yrs agoFri, December 18, 2020 at 6:59 AM GMT+1
  

           Done
        

        
    
 Story:  
 As a solution owner I want to have orchestration node for verifying group memberships for users, when adding new groups for users  
  
 ACs:  
 
 ESM Visual Workflow Automation have Orchestration node for verifying group memberships 
 Orchestration node must have Provisioning Engine-related activity: Verify Group Membership 
   
   provisioning engine has functionality to verify if users have group membership 
   from the verification workflow node admins are able to configure the attributes which will be used to verify if users have group membership 
   group verification can be done based by multiple OUs 
   if the chosen field in the person template doesn't have mapping to target system, then there should be error message shown: Field doesn't exists in the chosen template 
   EPE Master (backend) endpoint has functionality to make the search 
    
 Workflow designers must be able to select Orchestration node from the activities palette 
 ESM shall continue workflow based on orchestration result from Provisioning Engine 
 ESM shall log an error in ITSM log if orchestration activity was timed out 
 If Provisioning Engine responds with exception, ESM must create a log entry and move to the exception branch for workflow orchestration 

          
    
        EPE
      
    
        IGA
      
    
  
  Vote
  Follow
