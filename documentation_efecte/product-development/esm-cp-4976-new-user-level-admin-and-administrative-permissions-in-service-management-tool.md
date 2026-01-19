# ESM: CP-4976: New user level Admin and administrative permissions in service management tool

**Källa:** https://community.efecte.com/t/y7nfh3/esm-cp-4976-new-user-level-admin-and-administrative-permissions-in-service-management-tool
**Publicerad:** 2019-02-28T08:42:00.000Z
**Uppdaterad:** 2021-11-11T10:24:07.527000
**Författare:** 

---

ESM: CP-4976: New user level Admin and administrative permissions in service management tool

      
    
          
      

        
              Aki Koivukoski
            

            R&D
              Aki_Koivukoski
            updated 4 yrs agoThu, November 11, 2021 at 10:24 AM GMT+1
  

          16replies
        Tuija Länsisalmi1 mth agoWed, December 10, 2025 at 7:13 AM GMT+1
  
        

        
    
ContentsUser story:ACs:User story: 
 As a business owner I want to be sure that permissions can only be set by a very limited amount of people, even less than root users, in order to ensure data integrity and information security.  
ACs: 
 
 A new user level called “Admin” shall be created (roles in order: Root, Admin, Normal, Read-Only) 
 Managing permissions shall be limited to users with user level Root OR users with user level Admin with administrative permission "Edit users" 
   
   enabling administrative permissions to "Edit users" for any role shall only be visible and possible for Root level users 
   creating and editing roles is limited to Root only (can be disabled with a platform setting) 
    
 Managing licenses shall be limited to users with level Root OR users with user level Admin with administrative permission "Manage licenses" 
 It must not be possible to access any content of the Permissions tab by any other means unless the user has been granted the rights (URL bookmark, guessing URL, etc.) 
 Changing of permissions shall be possible as before through SAML2-based authentication 
   
   the new user level Admin must be supported also in SAML2-based permission and role management 
    
 Access to system folder is limited to Root level  
 Attribute permission management should be possible only through the UI path from the Permissions tab. 
   
   cannot be done from template/attribute configuration UI path 
   cannot be done from Select Module UI path 
   cannot be set from the User Preferences UI path 
    
 Elevated User Permissions (EUP) can only be set by users with user level Root 
 For the transition, all existing Normal users that have administrative rights will be promoted to Admin user level by a script in the update and proper administrative rights are set by the script 

          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            12
