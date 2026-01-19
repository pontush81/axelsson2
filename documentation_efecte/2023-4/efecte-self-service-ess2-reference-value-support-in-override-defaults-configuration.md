# Efecte Self-Service (ESS2): Reference value support in Override defaults configuration

**Källa:** https://community.efecte.com/t/83yhhv0/efecte-self-service-ess2-reference-value-support-in-override-defaults-configuration
**Publicerad:** 2023-09-25T06:43:55.277Z
**Uppdaterad:** 2023-09-25T08:43:55.277000
**Författare:** 

---

Efecte Self-Service (ESS2): Reference value support in Override defaults configuration

      
    
          
      

        
              Aki YlivarviModerator
            

            
              Aki_Ylivarvi
            2 yrs agoMon, September 25, 2023 at 8:43 AM GMT+2
  

           Done
        

        
    
 Problem statement  
 Environment administrators want to assign certain kinds of support cases reported from the ESS2 to a dedicated support group (e.g., a case related to hardware issues would be automatically assigned to the hardware team). Admins want to define this in the form's 'Override defaults' configuration.  
  Administrators also would like to earmark specific types of issues directly to dedicated Service, which is defined as a reference field on the template configuration so that predefined service selection will save the agent's time when handling the issue.  
  Short description  
 With support to define reference values in the 'Override defaults' configuration, administrators can define predefined values e.g., assigning an issue to a named support group or earmarking the issue to a specific Service.   
  Use case details  
 As an admin, I can define Reference value also to the Override values so that i can define e.g. default support groups to each Form.  
AC: 
 
   Admin can select a reference attribute type (not multi-value)   
   After selection, admin can open a drop-down to see the list of available datacard names (or primary attribute   
   Admin can select from one of the options in the drop-down   
   After the form has been submitted in the Portal UI, the generated datacard will contain the stored value in the associated attribute.   
   the end user should see only the values where the permission user has an access   
   if the referred datacard is deleted, created datacards shall receive empty value to the targeted attribute   

          
    
        ESS2
      
    
        Self-Service Portal
      
    
  
  Vote
  Follow
