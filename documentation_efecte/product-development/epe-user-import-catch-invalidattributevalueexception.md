# EPE: User Import catch InValidAttributeValueException

**Källa:** https://community.efecte.com/t/60yk4yc/epe-user-import-catch-invalidattributevalueexception
**Publicerad:** 2025-07-31T08:17:14.307Z
**Uppdaterad:** 2025-07-31T10:17:14.307000
**Författare:** 

---

EPE: User Import catch InValidAttributeValueException

      
    
          
      

        
              Martin Kasper
            

            
              Martin_Kasper.3
            5 mths agoThu, July 31, 2025 at 10:17 AM GMT+2
  

          1reply
        Riku NieminenModerator5 mths agoMon, August 4, 2025 at 8:34 AM GMT+2
  
        

        
    
With the user import there is that point when IGA ccount is copied to person, see: Error while parsing script expression. Template name: Person. Attribute All Accounts.
That Expression - due to jython script failure - leads to next Exception: ValidatingEntityXMLImporter|ERROR|2025-07-31 03:25:57,314|http-nio-8080-exec-1|[POST /ws/dataCardImport.ws, provisioning]|Import of data card failed. Entity(no=1, name=some unexperienced admin, id=12980744) Template(code=account, name=IGA Account, id=2844647) Folder(code=accounts, name=Accounts, id=6249408) com.bitmount.boas.exception.PersistenceException: javax.persistence.PersistenceException: org.hibernate.exception.ConstraintViolationException: could not execute statement and finally here: Caused by: org.postgresql.util.PSQLException: ERROR: null value in column "es_value" of relation "entitydata_string" violates not-null constraint   Detail: Failing row contains (12980825, 12980807, 888623, null). In the end, the Import brakes and the search beginns. The Improvement would be to catch that java SQL exception somehow in a way, that the import would not brake and a direct hint to jython script to ease teh debudding. Once the jython script is found it is way easier to debugg...
And with an import not breaking, one would save time and trust in the product, mostly for new customers would become stronger.
          
    
        EPE
      
    
  
  Vote
  Follow

## Bilder

![Bild](images/epe-user-import-catch-invalidattributevalueexception_65a988cc.png)


