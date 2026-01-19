# ESM: AI-Powered Category Suggestions

**Källa:** https://community.efecte.com/t/y4h6njy/esm-ai-powered-category-suggestions
**Publicerad:** 2020-10-15T04:16:45.600Z
**Uppdaterad:** 2020-10-15T06:31:25.097000
**Författare:** 

---

ESM: AI-Powered Category Suggestions

      
    
          
      

        
              Peter Schneider
            

            Chief Evangelist / Storyteller
              Peter_Schneider
            updated 5 yrs agoThu, October 15, 2020 at 6:31 AM GMT+2
  

          1reply
        Aki Koivukoski4 yrs agoWed, February 10, 2021 at 12:20 PM GMT+1
  
         Done
        

        
    
ContentsUser StoryAcceptance CriteriaUser Story 
 As a service desk agent,  
 I want to  automate the categorization of issues from similar issues  
 because it helps me to focus on strategic initiatives while speeding up the recording and resolving of issues.   
 NOTE: This is a licensable feature due to the additional hardware and operational requirements for the Artificial Intelligence  Component in a dedicated Docker container. Please contact your Efecte sales representative to inquire about information on the activation of this capability.  
 NOTE2: Activation of this capability requires curated historic issues data of at least 10.000 records and training of the model which requires a professional service from an Efecte consultant.  
 Note3: All data necessary for this functionality will stay in the Efecte cloud environment in the AIC container with the current production cloud. No external service is used in the deployment.  
 Note4: Currently, one language can be supported for each issue (template) including initially Finnish, Swedish, English, or German. For more languages, please discuss this with your Efecte contact.  
Acceptance Criteria 
 
 ESM requests from the Artificial Intelligence Component (AIC) which categories exist in the trained model for the current issue 
   
   a support agent opens an issue such as an incident in edit mode 
   the service management tool sends a request to the Artificial Intelligence Component (AIC) for related content when the subject (a short description) of the issue has been entered 
   the AIC analyses the intent of the subject and returns category suggestions that have been identified 
   the service management tool displays the suggested categories with a confidence rating on the right-hand side of the Detail Datacard View, the so-called Supplementary Information Area 
   the support agent can check the details of the suggested categories from the reference in a new window 
   the support agent can select one of the suggested categories with a mouse click 
   the category value is copied to the category attribute of the issue 
    
 An Efecte consultant can modify the training frequency, confidence rate sensitivity, and content to be trained in the AIC.  

          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            1
