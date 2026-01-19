# ESS2: Field Validation with RegEx

**Källa:** https://community.efecte.com/t/x2yfgt5/ess2-field-validation-with-regex
**Publicerad:** 2025-03-27T14:51:40.820Z
**Uppdaterad:** 2025-03-27T15:51:40.820000
**Författare:** 

---

ESS2: Field Validation with RegEx

      
    
          
      

        
              Aki YlivarviModerator
            

            
              Aki_Ylivarvi
            9 mths agoThu, March 27, 2025 at 3:51 PM GMT+1
  

          

        
    
Problem statement
There are no ways to validate short text inputs from the end user to ensure that the service management tool or the agent can proceed more quickly with given data.
 
Short description
Administrators should be able to configure RegEx validation to short text fields on field configuration with the validation message for cases when the validation doesn’t match.
 
Use case details
This story introduces the use of Regular Expressions to help provide Admins with the ability to validate data entered by their users, to ensure it’s accuracy. 
 
ACs

 When adding or editing a Short Text Field (string), the admin can choose to add data validation (Regular expression)
 In the end-user portal, the associated string input should be validated when focused is moved out of the field and if data has been entered by the user and an error with text provided by admin should be shown in case of validation fails 
 If a field is not required, data is not validated if user provides no input when the form is submitted.
 When the submit button is pressed, default validation occurs, along with validation on fields with RegEx. Request cannot be submitted when RegEx validation fails. 

          
    
        Self-Service Portal
      
    
        ESS2
      
    
  
  Vote
  Follow
