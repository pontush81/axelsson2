# ESM: Multivalue support for servlet.auth.user.ad.group and servlet.auth.admin.ad.group settings

**Källa:** https://community.efecte.com/t/p8yql5z/esm-multivalue-support-for-servlet-auth-user-ad-group-and-servlet-auth-admin-ad-group-settings
**Publicerad:** 2023-09-01T12:15:06.927Z
**Uppdaterad:** 2023-09-01T16:16:57.470000
**Författare:** 

---

ESM: Multivalue support for servlet.auth.user.ad.group and servlet.auth.admin.ad.group settings

      
    
          
      

        
              Jonne KaukoProduct Manager
            

            Senior Product Manager & Product Lead, M42 Core & Pro
              Jonne_Kauko
            updated 2 yrs agoFri, September 1, 2023 at 4:16 PM GMT+2
  

           Done
        

        
    
 Problem Statement:  
 In certain scenarios, organizations maintain multiple LDAP directories, such as Active Directories, for the provisioning of organizational data and authentication purposes. The challenge arises because the servlet.auth.user.ad.group and servlet.auth.admin.ad.group settings currently accept only single values. This limitation complicates handling situations where there is a need to accommodate more than one Active Directory or multiple Active Directory groups that grant access to ESM.  
 Proposed Solution:  
 To address this challenge, we propose an enhancement. We are planning an improvement to allow administrators to specify multiple values in the servlet.auth.user.ad.group and servlet.auth.admin.ad.group platform settings, providing them with greater flexibility in configuring access to ESM.  
 Use Case Details:  
 The improvement to the servlet.auth.user.ad.group and servlet.auth.admin.ad.group settings will enable the acceptance of multiple values, which must be provided in a comma-separated list. This enhancement ensures that organizations can efficiently manage access across multiple LDAP directories and groups, streamlining their authentication and access control processes.  
   
   
          
  Vote
  Follow

## Bilder

![Bild](images/esm-multivalue-support-for-servlet-auth-user-ad-group-and-servlet-auth-admin-ad-group-settings_95d71fbf.png)

![Bild](images/esm-multivalue-support-for-servlet-auth-user-ad-group-and-servlet-auth-admin-ad-group-settings_a156b6ad.png)


