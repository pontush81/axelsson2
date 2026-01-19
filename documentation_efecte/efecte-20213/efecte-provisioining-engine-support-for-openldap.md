# Efecte Provisioining Engine support for OpenLDAP

**Källa:** https://community.efecte.com/t/h7h8pz3/efecte-provisioining-engine-support-for-openldap
**Publicerad:** 2020-08-14T11:33:15.547Z
**Uppdaterad:** 2020-08-14T13:33:15.547000
**Författare:** 

---

Efecte Provisioining Engine support for OpenLDAP

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            5 yrs agoFri, August 14, 2020 at 1:33 PM GMT+2
  

          1reply
        Jukka PapinahoEfecte Employee5 yrs agoThu, October 22, 2020 at 10:35 AM GMT+2
  
         Done
        

        
    
 User story: As a customer I want to do provisioning / de-provisioning to OpenLDAP.  
  ACs:  
 
 Efecte Provisioning Engine (EPE) must be able to read (scheduled) and write (event-based) data from and to OpenLDAP 
 Administrators are able configure connection to OpenLDAP using the admin UI 
   
   Processes can be scheduled in ESM ProvisioningTasks UI 
   Processes can be run manually from ESM Provisioining UI 
   Processes can be run event-based triggered by Visual Workflow Automation 
    
 
 Notes: Following event-based provisioning capabilities will be available in the first version: - Verification of a user request before creating a new user - Creating a new user - Update user information - Add/Remove a user to/from a group(s) - Reset user password - Update user Distinguished Name Value - Delete user 
          
    
        EPE
      
    
        IGA
      
    
  
  Vote
  Follow
