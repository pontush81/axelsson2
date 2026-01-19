# Scandinavian letters in the attachment name break the file name in ESM

**Källa:** https://community.efecte.com/t/m1hffkz/scandinavian-letters-in-the-file-name-break-the-file-name-in-esm
**Publicerad:** 2021-05-04T13:40:27.970Z
**Uppdaterad:** 2021-05-04T15:40:27.970000
**Författare:** 

---

Scandinavian letters in the attachment name break the file name in ESM

      
    
          
      

        
              Kirstin MykkänenEfecte Employee
            

            Customer support coordinator
              Kirstin_Mykkanen
            4 yrs agoTue, May 4, 2021 at 3:40 PM GMT+2
  

          

        
    
 The following bug (CP-6271) has been identified in release ESM 2021.1. :  
 When sending messages out from ESM/itsm or reading them into ESM/itsm, the name of attachments having Scandinavian characters in the file name gets corrupt. The attachment itself is not affected. If you know what program you need to open it, you can open it without problems.   
 Workaround: Avoid attaching files to emails that have Scandinavian characters in the file name.  If such emails are coming in, please ask the end user to resend the email with an attachment without Scandinavian characters .   
          
    
        Known Error
      
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            2
