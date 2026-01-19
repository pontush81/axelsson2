# How do you compare "Transformation settings" across systems (TEST/PROD)?

**Källa:** https://community.efecte.com/t/g9ypt3c/how-do-you-compare-transformation-settings-across-systems-testprod
**Publicerad:** 2025-12-17T11:26:15.447Z
**Uppdaterad:** 2025-12-17T12:26:15.447000
**Författare:** 

---

How do you compare "Transformation settings" across systems (TEST/PROD)?

      
    
          
      

        
              Peter Scheffczyk
            

            Advisory Solution Consultant
              Peter_Scheffczyk.1
            1 mth agoWed, December 17, 2025 at 12:26 PM GMT+1
  

          

        
    
Currently, the ctt does not include comparing "transformation configurations", i.e. when I transform a ticket into a problem, is there maybe more or less attributes configured to get copied on my TEST vs. my PROD system? 
Are there any best practices around finding differences in transformation configuration settings and resolving them? In the configuration export, they are included with the "internal ID" instead of "speaking names" for attributes (probably a reason why they are not included in ctt...?), like this:
<entity-transformation>         <entity-transformation-target-template name="Service request" code="ServiceRequest" id="76241"/>         <entity-transformation-target-folder name="Request Fulfilment" code="ServiceRequests" id="1052067"/>         <rule>             <target>16563765</target>             <string>$138653187_1078906$</string>         </rule>         <rule>             <target>16563428</target>             <string>$138653187_16563473$</string>         </rule>         <rule>             <target>16570626</target>             <string>$138653187_16570583$</string>         </rule>         <rule>             <target>76291</target>             <string>$138653187_16563245$</string>         </rule>         <rule>             <target>76270</target>             <string>$138653187_1078834$</string>         </rule>
...
          
  Like
  Follow
