# Removing a Template Permission from a Role breaks the Global Search

**Källa:** https://community.efecte.com/t/60hfsnm/removing-a-template-permission-from-a-role-breaks-the-global-search
**Publicerad:** 2021-05-26T05:18:21.613Z
**Uppdaterad:** 2021-05-26T07:18:21.613000
**Författare:** 

---

Removing a Template Permission from a Role breaks the Global Search

      
    
          
      

        
              Kirstin MykkänenEfecte Employee
            

            Customer support coordinator
              Kirstin_Mykkanen
            4 yrs agoWed, May 26, 2021 at 7:18 AM GMT+2
  

          

        
    
 The following bug (CP-6283) has been identified in release ESM 2021.1. and 2021.2. : When an admin user revokes the permission to a certain template from a role, the Global Search functionality breaks. It returns the following error  "A REQUEST FOR RESOURCES/SEARCH/QUICK COULD NOT BE PROCESSED Reason: Unauthorized operation" The problem gets fixed if you run the function 'Reload Permissions' at the ESM admin side under Maintenance -> Other actions. Depending on the customer, this function might be performance-intensive. It is advised to either first try it out in your test environment or reload the permissions out of normal working hours. 
          
    
        Known Error
      
    
        Service Management Tool
      
    
  
  Vote
  Follow
