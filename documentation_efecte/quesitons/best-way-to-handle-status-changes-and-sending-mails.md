# Best way to handle status changes and sending mails

**Källa:** https://community.efecte.com/t/m1y1xdy/best-way-to-handle-status-changes-and-sending-mails
**Publicerad:** 2025-08-20T08:45:11.823Z
**Uppdaterad:** 2025-08-20T10:45:11.823000
**Författare:** 

---

Best way to handle status changes and sending mails

      
    
          
      

        
              Oliver Burtscher
            

            
              Oliver_Burtscher
            4 mths agoWed, August 20, 2025 at 10:45 AM GMT+2
  

          2replies
        Oliver Burtscher4 mths agoThu, August 21, 2025 at 1:42 PM GMT+2
  
        

        
    
Hello, Community
This might be a silly question, but I'm stuck here:
Use case is:
- Customer orders something, default status is set to "Waiting for approval". - A confirmation mail to the customer should be sent (if possible, a html based mail that we already developped, it contains tables, graphics and more). - At the same time, a mail to a certain group of people (support group) should be sent to indicate that there's an pending order
- The support group then approves the order or declines it, in both cases with a mail including a comment to the customer - The support group then closed the case (manually). No further action. My problem:
Maybe I could realize this using mail events that are checking for a status change to "approved" or "declined". So far, so good.
But what, if someone changes the status back from maybe "closed" to "approved"? Or from "Declined" to "approved"?
The mail event then would again send out its mail, which would be wrong. And I cannot check, if a status already has been selected earlier in the lifetime of an order.
What would you suggest to prevent this scenario? Do I need a presave listener to check the current status and the new one and then decide, if that's ok to do? To prevent a support member to change the status back from closed to approved and so on?
How would such a listener look like?:
- Don't allow status change from approved to declined - Don't allow status change from declined to approved - Don't allow status change from closed to either approved or declined or wainting for approval
I hope I could explain this in a way it can be understood. This is something that probably is a common use case. By the way: In a workflow, I can send a mail, even a html mail. But it won't send that mail containing complex html with tables and so on.
 
THANKS to all!
Oli
          
    
        Administration
      
    
  
  Like
  Follow

## Bilder

![Bild](images/best-way-to-handle-status-changes-and-sending-mails_8b8d52fb.png)


