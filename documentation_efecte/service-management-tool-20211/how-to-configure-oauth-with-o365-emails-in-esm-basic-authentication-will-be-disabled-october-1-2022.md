# How to configure OAuth with O365 emails in ESM? (Basic authentication will be disabled October 1, 2022)

**Källa:** https://community.efecte.com/t/x2hzs32/how-to-configure-oauth-with-o365-emails-in-esm-basic-authentication-will-be-disabled-october-1-2022
**Publicerad:** 2021-02-19T16:52:05.820Z
**Uppdaterad:** 2022-11-02T09:23:54.467000
**Författare:** 

---

How to configure OAuth with O365 emails in ESM? (Basic authentication will be disabled October 1, 2022)

      
    

        updated 3 yrs agoWed, November 2, 2022 at 9:23 AM GMT+1
  
          12replies
        Weni Zhou2 yrs agoWed, February 8, 2023 at 1:41 PM GMT+1
  
        

        
    

  
    Using modern authentication (OAuth2) as email authentication method with O365 - 23.09.2022
  
  
   NOTICE! Actions needed before October 1, 2022!!  
 According to the communication from Microsoft, they are disabling the basic authentication on their O365 (Exchange Online) email servers starting from 1st of October 2022. All Efecte customers using O365 for emails need to configure the modern OAuth for receiving emails to ensure uninterrupted operations.  
 More details on Microsoft's documentation: https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online  
 If our customers have the basic auth configured for incoming emails, the emails will not be received in Efecte after Microsoft has disabled the basic auth.  
 Basic auth for SMTP (O365 outgoing emails) will also be disabled if it is not being used.   
 Please check the attached pdf on how to configure the OAuth for emails with Efecte.  
 
 Note 1! If copy-pasting the values for mail.oauth.scopes straight from the .pdf document, please make sure all characters are included (mainly double "/" characters in the latter SMTP scope: https://outlook.office365.com/IMAP.AccessAsUser.All,https://outlook.office365.com/SMTP.Send    
 
 Note 2! Please note that Microsoft provides a temporary opt-out option. More information here: https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-deprecation-in-exchange-online-september/ba-p/3609437
          
    
        Administration
      
    
        Service Management Tool
      
    
  
  Like
  Follow
    
            6
