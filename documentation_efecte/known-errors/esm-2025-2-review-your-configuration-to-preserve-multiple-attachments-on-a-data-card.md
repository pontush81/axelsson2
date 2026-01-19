# ESM 2025.2: REVIEW YOUR CONFIGURATION TO PRESERVE MULTIPLE ATTACHMENTS ON A DATA CARD

**Källa:** https://community.efecte.com/t/g9ykp68/esm-2025-2-review-your-configuration-to-preserve-multiple-attachments-on-a-data-card
**Publicerad:** 2025-06-13T12:55:19.110Z
**Uppdaterad:** 2025-06-13T14:55:19.110000
**Författare:** 

---

ESM 2025.2: REVIEW YOUR CONFIGURATION TO PRESERVE MULTIPLE ATTACHMENTS ON A DATA CARD

      
    
          
      

        
              Juha HänninenProduct Owner
            

            ESM Product Owner
              Juha_Hanninen.1
            7 mths agoFri, June 13, 2025 at 2:55 PM GMT+2
  

          

        
    
Background
In ESM 2025.2, we have fixed an issue that caused changes to references, back-references, and attachments made in the background to be lost if the user's data card was open. In 2025.2, only the user's changes are saved when the open data card is saved, and background changes are correctly preserved.
This fix also fixed the FileUpload handler attributes so that they respect the multi-value setting. However, we have identified that some customers have relied on past behavior where you could add multiple attachments to a single-value attribute, and fixing the bug does not allow this anymore.
Review your configuration to identify if you need reconfiguration
If you have a FileUpload handler configured in a single-value attribute, but that attribute already contains multiple values, you need to change the attribute to be multi-value if you want to preserve existing attachments when new attachments are added. Due to an older bug fixed in the latest release, adding multiple attachments to a single-value attribute with a FileUpload handler was possible. If you have relied on this behavior, those attributes must now be reconfigured to maintain the past behavior.
Step-by-step instructions:

 Export your ESM template configurations (from Maintenance -> System settings -> Export configurations) and review the configuration to find single-value attributes that use the FileUpload handler.
 If you have single-value attributes that have been used as multi-value attributes, please change those attributes to multi-value in the attribute settings.

 
Automated configuration change in planning:
We are currently working on an automated update of configurations in which attributes with the FileUpload handler are not set as multi-value. We'll inform you when this change will be implemented in test environments. We'll make the change in production environments soon afterwards.
          
    
        Service Management Tool
      
    
  
  Vote
  Follow
