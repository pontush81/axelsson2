# ESM: Improvements to email connection mechanisms for mitigating oAuth throttling issues

**Källa:** https://community.efecte.com/t/83yqln3/esm-improvements-to-email-connection-mechanisms-for-mitigating-oauth-throttling-issues
**Publicerad:** 2023-09-01T14:39:36.227Z
**Uppdaterad:** 2023-11-29T09:02:28.387000
**Författare:** 

---

ESM: Improvements to email connection mechanisms for mitigating oAuth throttling issues

      
    
          
      

        
              Jonne KaukoProduct Manager
            

            Senior Product Manager & Product Lead, M42 Core & Pro
              Jonne_Kauko
            updated 2 yrs agoWed, November 29, 2023 at 9:02 AM GMT+1
  

           Done
        

        
    
Problem Statement
In some ESM environments with substantial email traffic volumes, issues related to sending emails are encountered, leading to failures in sending emails through M365. These problems include throttling issues and occasional connection failures due to OAuth token-related issues.
Proposed Solution
To enhance the email functionalities' reliability, we plan to implement a solution with improved token caching and a retry mechanism for the connection. 
Use Case Details
We are planning to implement improvements in two key areas:

 Improved Token Caching: We are planning to optimize the caching of oAuth tokens to prevent throttling issues. This intends to improve the reliability of sending and receiving emails. 
 Retry Mechanism: We're planning to introduce a retry mechanism that automatically attempts to reconnect if a connection fails due to token issues.
  
   Note1: Please note that this improvement does not introduce queuing for email sending - the implementation scope covers a retry mechanism for the connection.  
   Note2! This improvement is related only to sending emails from ESM. Receiving emails with MailTask is not affected by this improvement.  
  

          
  Vote
  Follow
    
            2
