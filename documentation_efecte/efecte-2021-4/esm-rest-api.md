# ESM: REST API

**Källa:** https://community.efecte.com/t/g9hf1a5/esm-rest-api
**Publicerad:** 2021-05-07T14:39:07.993Z
**Uppdaterad:** 2021-05-07T16:46:18.613000
**Författare:** 

---

ESM: REST API

      
    
          
      

        
              Aki Koivukoski
            

            R&D
              Aki_Koivukoski
            updated 4 yrs agoFri, May 7, 2021 at 4:46 PM GMT+2
  

          8replies
        Aki Koivukoski3 yrs agoThu, January 27, 2022 at 2:40 PM GMT+1
  
         Done
        

        
    
 ESM will offer new modern and easy to use integration API for third party integrations with widely utilised REST architecture style.  
 REST will provide logical way to access the ESM data structured by the data cards and templates.  
 URI syntax for v1:   
   
 User authentication will be done agains ESM local user with a JWT token.   
 Sample token looks like this  
Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJyb290IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL21pY2hhbC9hcGkvdjEvdXNlcnMvbG9naW4iLCJpYXQiOjE2MTE5MjQxNDMsImV4cCI6MTYxMTkyNTA0M30.J_F56nafWfhV8EVuj4tMCvoI-01WAkx6LIgVUPWqRhsU-x3E-qp3ysRjP0o1ToOzVWBMJzEaF0aEuLZ_o1q42A 
 New platform settings will be introduced to configure the REST API authentication.  
 
 security.external.api.token.key 
 security.external.api.token.expiration.time (default 15min) 
 
 The REST API will use JSON to pass the data to/from ESM. Example JSON for a data card:  
{
    "name": "INC-42: Incident",
    "id": "20794",
    "templateName": "Incident / Service request",
    "templateCode": "incident",
    "templateId": "1307",
    "folderName": "Incident management",
    "folderCode": "job",
    "data": {
        "static_code": {
            "name": "status",
            "type": "static-string",//-date
            "values": [
                {
                    "value": "01 - Waiting",
                    "id": "1322",
                    "code": "01_waiting"
                }
            ]
        },
        "string_code": {
            "name": "Subject",
            "type": "string",
            "values": [
                {
                    "value": "56"
                }
            ]
        },
        "number_code": {
            "name": "Number attribute",
            "type": "number",
            "values": [
                {
                    "value": 42, //Integer, Float
                }
            ]
        },
         "datetime_code": {
            "name": "Datetimeattribute",
            "type": "date",
            "values": [
                {
                    "value": "2021-03-05T11:00:00+0200", //iso-8601
                }
            ]
        },
        "reference_code": {
            "name": "Reference attribute",
            "type": "reference",
            "values": [
                {
                    "name": "00000000 | Rental Agreement for London office | Futon IT Maintenance",
                    "id": "357775",
                    "templateName": "Very general problem",
                    "templateCode": "very_general",
                    "isDeleted": false,
                    "isHidden": true,
                    "url": "/dc/very_general/data/357775
                }
            ]
        },
        "unauthorized_reference_code": {
            "name": "Reference attribute2",
            "type": "reference",
            "values": [
                   // empty value if not authorized
            ]
        },
        "extreference_code": {
            "name": "Ext reference",
            "type": "external-reference",
            "values": [
                {
                    "name": "Google",
                    "location": "https://www.google.fi"
                }
            ]
        },
        "worklog_code": {
            "name": "Worklog",
            "type": "worklog",
            "values": [
                {
                    "author": "Abraham administrator",
                    "value": "first",
                    "date": "2021-03-09T08:20:54+0000", // ISO-8601
                },
                {
                    "author": "Abraham administrator",
                    "value": "second",
                    "date": "2021-03-08T11:56:20+0000"
                }
            ]
        }
    }
} 
 Example of JSON for data card listing:   
{
    "name": "INC-42: Incident",
    "id": "20794",
    "url": api/template/data/20794

}
{

    "name": "INC-42: Incident",
    "id": "20794",
    "url": api/template/data/20794

}
{

    "name": "INC-42: Incident",
    "id": "20794",
    "url": api/template/data/20794

} 
 We have identified the following steps to develop our REST API v1:  
 
 Individual cards (GET, DELETE) 
 Data card listing (GET) 
 Data card attribute values (GET, PUT, POST, DELETE) 
 Template definitions (GET) 
 Template listing (GET) 
 Data card creation and update (POST, PUT) 
 Filtering for datacard listing 
 Asynch bulk import 
 Performance and caching 

          
    
        IT Service Management
      
    
  
  Vote
  Follow
    
            11

## Bilder

![Bild](images/esm-rest-api_5f4b4a44.png)


