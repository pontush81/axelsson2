# Efecte Self-Service (ESS2): Configure multiple single line form fields to single attribute

**Källa:** https://community.efecte.com/t/83yh3f9/efecte-self-service-ess2-configure-multiple-single-line-form-fields-to-single-attribute
**Publicerad:** 2023-09-26T06:02:49.897Z
**Uppdaterad:** 2023-09-26T08:02:49.897000
**Författare:** 

---

Efecte Self-Service (ESS2): Configure multiple single line form fields to single attribute

      
    
          
      

        
              Aki YlivarviModerator
            

            
              Aki_Ylivarvi
            2 yrs agoTue, September 26, 2023 at 8:02 AM GMT+2
  

           Done
        

        
    
 Problem statement  
 To get more accurate input from the end users, portal administrators need to define more questions to form without defining more template attributes on the ESM side.  
  Short description  
 Administrators can configure multiple single line fields to one text attribute on the target template to ask more specific customers depending on the form topic.   
  Use case details  
 As an admin user, I want to map multiple single line form fields to one target attribute, so that I can collate information into one attribute instead of multiple attributes.  
 AC:   
 
   When adding a single line text field to a form, admin can set the target as a string or text attribute   
   If the target is set to a text attribute, the admin is informed how the data will be stored (label: data)   
   Data from input form field is saved to the target attribute in the following way:  
   
     formLabel1:formData1 formLable2:formData2a, formData2b   
    
   Admin is informed which fields are targeted to the same text attribute while choosing the target attribute   
   If a text attribute is already being used as a target attribute for a multi-line text field, it will not appear in the list of available text attributes that can be used for new Multi-line text fields.   
   On multi-mapping case we only show target attribute and not source attributes when viewing detailed information of the issue on ESS2 UI   

          
    
        ESS2
      
    
        Self-Service Portal
      
    
  
  Vote
  Follow
    
            1
