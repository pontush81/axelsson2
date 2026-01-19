# REST API with references

**Källa:** https://community.efecte.com/t/m1yzws1/rest-api-with-references
**Publicerad:** 2024-11-20T11:36:56.363Z
**Uppdaterad:** 2024-11-20T12:36:56.363000
**Författare:** 

---

REST API with references

      
    
          
      

        
              Erik Forsström
            

            
              Erik_Forsstrom
            1 yr agoWed, November 20, 2024 at 12:36 PM GMT+1
  

          

        
    
I'm attempting to create a solution where a third party is able to create certain datacards via RESP API. I'm running into an issue where I cannot add values to references without actually using an direct ID to a datacard.
For example, I would want to give an email address string in the payload which would be put into a field that is a reference to the persons datacard which uses the email as an identifying criteria. Apparently this could only be done as below?
 
{

    "folderCode": "ServiceRequests_TheClient",
    "data": {
        "OrderedBy": {
            "values": [
                {
                "dataCardId": "169149123"
                }
            ]
        }
        ,
        "Subject": {
            "values": [
                {
                    "value": "Subject of the ServiceRequest"
                }
            ]
        },
        "AdditionalInformation": {
            "values": [
                {
                    "value": "AdditionalInformation for the Service Request"
                }
            ]
        }
   }
}
Now while this payload works as such, in the example I am giving the direct datacard ID to the relevant person datacard. I cannot expect the third party to see be able to know this as they only have the email address available anyway.
I haven't managed to make this work using the email address itself in the payload. Are there any solutions for this other than some weird Expression/Listener thingamajig with hidden fields where I add the email as a string to a hidden field and then use some other means of delivering it to the appropriate reference field?
          
    
        IT Service Management
      
    
        Integrations
      
    
        Administration
      
    
  
  Like
  Follow
    
            7

## Bilder

![Bild](images/rest-api-with-references_6e06668e.png)


