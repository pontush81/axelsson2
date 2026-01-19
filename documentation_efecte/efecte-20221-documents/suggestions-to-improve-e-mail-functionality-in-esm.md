# Suggestions to improve e-mail functionality in ESM

**Källa:** https://community.efecte.com/t/h44anq
**Publicerad:** 2019-10-23T18:31:43.267Z
**Uppdaterad:** 2019-10-23T21:00:32.750000
**Författare:** 

---

Suggestions to improve e-mail functionality in ESM

      
    
          
      

        
              Fredrik Liljeblad
            

            KTH Royal Institute of Technology
              Fredrik_Liljeblad
            updated 6 yrs agoWed, October 23, 2019 at 9:00 PM GMT+2
  

          29replies
        Peter Scheffczyk6 days agoMon, January 12, 2026 at 5:29 PM GMT+1
  
        

        
    
Contents1         E-mail user interface1.1        The e-mail component embedded in a data card (EntityStateMail)1.1.1        In view mode1.1.2        In edit mode1.2        The e-mail component in the expanded e-mail window1.2.1        Viewing e-mails1.2.2        Editing e-mails2         Functionality2.1        Information in mails2.1.1        Display names and addresses2.1.2        Who has written an e-mail in an incident?2.1.3        Show bcc for sent e-mail2.1.4        Show full e-mail headers and raw e-mail2.2        E-mail functionality2.2.1        Spell checking of e-mails2.2.2        Printing e-mails2.2.3        Merge of e-mail/tickets2.2.4        Preserve inline images in replies and forwards2.2.5        Personal signatures in e-mail2.2.6        Including attachments in e-mails2.2.7        Reloading of new mails3         Technology3.1        E-mail headers3.1.1        Reply-To3.1.2        In-Reply-To and References3.2        E-mail transport etc.3.2.1        Sending mails3.2.2        API E-mail access4         E-mail, testing, and quality assurance Our organization (KTH) is entirely e-mail driven, most of our doings are handled via e-mail discussions, both internally between functions and also with our students.  
 The Incident template in Efece ESM is rapidly becoming our primary communication tool and, therefore, also falls under extensive scrutiny.  
 This post contains some of the improvements to the systems e-mail communication we would like to suggest.  
 The suggestions are divided into areas concerning User Interface, Functionality, and Technology.  
1         E-mail user interface 
1.1        The e-mail component embedded in a data card (EntityStateMail) 
1.1.1        In view mode 
 The area reserved for reading and composing email in the data card is very small but at the same time, takes up much space.  
 When viewing the body of an e-mail, the part of the conversation the agent can see is very small, and much scrolling is needed to read an e.mail. The size of the email component cannot be resized to list more emails or for easier reading of mail.  
 Expanding an e-mail in reading mode makes all the other mails disappear outside the container view.  
 The view cannot be expanded or configured in size.  
 
 We suggest that the size of the e-mail component is configurable in the attribute settings and that the user should be able to resize the component. 
 We suggest that the system remembers the users' last size and uses that as the default size. 
 
1.1.2        In edit mode 
 When editing an e-mail, the useful area is very limited. The text shown is of quite large font, and the signature takes up most of the space. Here the text box can be resized but must be done so every time.  
 
 We suggest that the size of the text box is configurable in the attribute settings. 
 We suggest that the system remembers the users' last size and uses that as the default size. 
 
1.2        The e-mail component in the expanded e-mail window 
1.2.1        Viewing e-mails 
 The list of mails in the panel on the left only displays the latest five mails, regardless of how much vertical space is available. Instead, a “more” button is displayed to show additional mails in the conversation.  
 
 We suggest that the listing of mails on the left always shows all e-mails in a conversation. So that the user can scroll to the right mail. 
 
 or  
 
 We suggest that the listing of mails on the left shows as many mails as can fit in the space available. 
 
1.2.2        Editing e-mails 
 In editing e-mails in the expanded e-mail window, the size of the edit text-box does not follow the size of the window. The user then has to resize the text-box manually every time to edit mails.  
 
 We suggest that the size of the edit text-box follow the size of the window for the expanded e-mail view. 
 
2         Functionality 
2.1        Information in mails 
2.1.1        Display names and addresses 
 Mails sent from the system listed in the e-mail container shows the From -address as an e-mail address, But received mails are shown with the From -address as the display name.  
 According to 3.4 in RFC 5322 Internet Message Format the To:/From: field in an e-mail is composed of a “display name” and an “addr-spec”. For example, “Fredrik Liljeblad <fli@kth.se>" contains the display name “Fredrik Liljeblad” and the addr-spec/e-mail address “fli@kth.se”.  
 EMS cannot (to my knowledge) handle sending addresses on the correct format that contains both the display name and e-mail address. It only sends e-mails with the plain e-mail address.  
 In our case, our customers get e-mails from “it-support@kth.se” and not from “KTH IT-Support”. This looks bad and unprofessional.  
 
 We suggest that ESM implements support for correctly formed To:/From:-addresses that contains the display name as well as the e-mail address. 
 We suggest that ESM shows the display name for outgoing e-mails instead of the e-mail address. 
 
2.1.2        Who has written an e-mail in an incident? 
 When an agent working in ESM communicates via an e-mail, only the support group's e-mail address is shown in the From-field in the e-mail and the listing of emails. This means that another agent cannot quickly see who has communicated what in an incident.  
 Also, the customer has a hard time knowing which service agent they have communicated with. Most other systems we have looked at use a method of modifying the display name part of the From -field. For example, if I replied to an email, the From -field would be: “Fredrik Liljeblad on behalf of KTH IT-Support <it-support@kth.se” or “Fredrik Liljeblad via IT-Support <it-support@kth.se>".  
 ESM could then list “Fredrik Liljeblad via IT-Support” as the sender of the e-mail, and the customer would know with which service agent they had interacted.  
 
 We suggest that ESM implements a feature that enables service agents to see what other service agents have sent what e-mail in an incident. 
 We suggest that ESM implements a feature that uses the display name part of a From -field to let a customer know with which service agent they have communicated. 
 
2.1.3        Show bcc for sent e-mail 
 When sending an e-mail from ESM and using the bcc:-field. The e-mail that is saved in the system for later viewing does not show the information that it was sent as bcc to another recipient. This means that data is lost about who the mail has been sent to.  
 
 We suggest that the bcc:-field is shown in the e-mail view when displaying an email message, but not included when replying/forwarding the same mail. 
 
2.1.4        Show full e-mail headers and raw e-mail 
 Sometimes an agent needs to check how an e-mail was routed, why it took so long to arrive, or if the sender is verified or not. This requires access to the headers of an e-mail. Also, an agent sometimes needs to see if there is a missing attachment or alike in an e-mail. This requires access to the raw e-mail.  
 In the ESM widget, there is no way to view the headers or the raw e-mail.  
 
 We suggest that the ESM widget adds functionality to view the e-mail headers and the raw e-mail. 
 
2.2        E-mail functionality 
2.2.1        Spell checking of e-mails 
 When writing an e-mail in the mail editor, the browser's spell check is disabled by the system. This is a basic function when composing e-mail and should be available.  
 
 We suggest that browser spell checking is allowed when composing e-mails. 
 
2.2.2        Printing e-mails 
 The ESM system has a function to print a data card, but it is impossible to print e-mails received into the system. There are numerous reasons why the printing of e-mails are required.  
 
 We suggest that ESM implements a function for printing e-mails stored in an incident ticket. 
 
2.2.3        Merge of e-mail/tickets 
 When a customer sends an e-mail to a recipient in ESM and also cc:s several other people in the original e-mail. All responses from third parties to the mail creates a new incident. Usually, this happens when a user is asking something and cc: someone for confirmation.  
 The reply from the third party should be included in the ticket but is now only available if the service agent reviewing the reply notices it and links it as a child incident. The result is also that the ticket is hard to review.  
 A function that allows for the “merging” of incidents is needed. It should copy the e-mails contained in the “from” ticket to the list of mails in the “to” ticket, and also update timestamps and alike. The “from” tickets Incident-ID should act as an alias for the “to” tickets Incident-ID so that further communication identified by the previous ID should be included in the new ticket. The “from” ticket should be deleted.  
 
 We suggest that ESM implement a function to “merge” incident tickets. 
 
2.2.4        Preserve inline images in replies and forwards 
 When replying to or forwarding an e-mail that contains an inline-image. The new e-mail loses the image. Left instead of the image is an HTML reference tag (cid:). This behavior means that information is lost, and the original email cannot be forwarded to an external part. This is very problematic when forwarding an e-mail that contains several screenshots, and the forwarded mail is garbled even if the images are re-attached as separate attachments.  
 
 We suggest that the look and formatting of e-mails are not changed when forwarded or replied to. That inline images are kept intact. 
 
2.2.5        Personal signatures in e-mail 
 When composing an e-mail, a signature is usually included at the end of the text. At the moment, there is no way for the editor to detect which service agent that is composing the e-mail and include a correct signature representing the agent. The workaround of using an attribute from the data card is not reliable. For example, when another service agent replies to an e-mail without changing the “support person”-attribute, the wrong signature, and the wrong name are used.  
 
 We suggest that EMS implements a function for managing personal signatures that are used for e-mail communication. A personal signature could be created on the agent's “Person” data card or in the “Personal Settings” menu. 
 
2.2.6        Including attachments in e-mails 
 Attachments that are present in the “File attachments” attribute of an incident are not available for inclusion in outgoing e-mails. However, the attachment needs to be downloaded and re-attached to an e-mail to include it.  
 The possibility of always including all attachments in all outgoing e-mails, and de-selecting the ones that should not be included is a very error-prone solution.  
 
 We suggest that EMS implement an attachment picker that allows the sender of an e-mail to choose which attachments available in an incident should be included in the outgoing e-mail. 
 
2.2.7        Reloading of new mails 
 If a new mail arrives in an incident that an agent has open, there is no notification that new communication has arrived. It would be useful if the list of mails would auto-update when new e-mails are received.  
 
 We suggest that EMS implement an automatic refresh of the list of e-mails that are shown in an incident. 
 
3         Technology 
3.1        E-mail headers 
3.1.1        Reply-To 
 The ESM MailTask component does not respect the e-mail header “Reply-To:”, but instead address replies to the From-header.  
 
 We suggest that the ESM MailTask component gets functionality to use the “Reply-To:”-address as the e-mail address to use for correspondence. 
 
3.1.2        In-Reply-To and References 
 These headers are defined in 3.6.4 in RFC 5322 and allow for e-mail clients to identify which e-mails belong to the same thread. ESM does not respect these fields in sending either auto-replies or replying to e-mails. For clients that use e-mail treading, this means that all communication with ESM appears as a new e-mail thread.  
 
 We suggest that ESM implement e-mail headers that include In-Reply-To and References functionality. 
 
3.2        E-mail transport etc. 
3.2.1        Sending mails 
 When sending an e-mail from the ESM e-mail widget, it communicates directly with the e-mail smtp server. In most cases, this is not a problem, but if the outgoing e-mail server is not available at that exact time, the user gets a cryptic error message. Most e-mail clients store the e-mail in a queue and try to resend it later. ESM does not, so the agent is stuck with a composed mail that cannot be sent.  
 
 We suggest that ESM creates a function to save a Draft e-mail so that a composed e-mail does not get lost if the outgoing e-mail server is unavailable. 
 We suggest that ESM implements a local mail queue for outgoing e-mails that manages the sending of e-mails. 
 
3.2.2        API E-mail access 
 The web-api is a very useful tool for integrating ESM with other systems, to create automation of both ticket handling and perform actions in other systems. Attachments in an incident data card can be accessed from the api, but e-mails cannot. This means, for example, that e-mails sorted as spam in ESM cannot easily be exported to our e-mail filter for training.  
 
 We suggest adding the possibility of accessing e-mails from the web-api to ESM. 
 
4         E-mail, testing, and quality assurance 
 In each new release of ESM, new bugs have been introduced in the e-mail function. Many of them breaking how e-mail is formatted or attachments handled. This has a large impact on our day to day business since we manage much of our communication via e-mail. A broken functionality (even just in formatting) is serious.  
 
 We want to suggest that Efecte add more tests and QA controls to e-mail functionality before releasing new updates. 
 We want to suggest that Efecte add more resources to fix bugs in previously working functions so that they can be fixed in a timely manner. Waiting for the next quarter release is too long. 
 
 An example of currently open change proposals regarding e-mails bugs: CP-5412, CP-5604, CP-5628, CP-5612, CP-5654  
  
 Best Regards, Fredrik Liljeblad KTH 
          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            59
