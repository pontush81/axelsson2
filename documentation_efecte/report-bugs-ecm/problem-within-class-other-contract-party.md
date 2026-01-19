# Problem within class "other contract party"

**Källa:** https://community.efecte.com/t/60hfgl0/problem-within-class-other-contract-party
**Publicerad:** 2021-05-10T09:13:06.353Z
**Uppdaterad:** 2021-05-10T11:13:06.353000
**Författare:** 

---

Problem within class "other contract party"

      
    
          
      

        
              Martin KasperEfecte Employee
            

            ITSM Consultant
              Martin_Kasper.1
            4 yrs agoMon, May 10, 2021 at 11:13 AM GMT+2
  

          

        
    
 Within class "other contract party" there is a reference on attribute "Other contract party" whith two EQL Filter:  
 
 select _entity from com.efecte.datamodel.Entity _entity  where $internal_party$ = #referrer:intracompany_agreement# and _entity.template.code = 'company' 
 select _entity from com.efecte.datamodel.Entity _entity  where $internal_party_in_external$ = #referrer:intracompany_agreement# and _entity.template.code = 'external_party' 
 
 In case 1 I would expect to get a field "internal_party" in template Organization and in case 2 I would hope to find a tempalte with code "external_party". In both cases, I would assume, that "other contract party" aims  at the beneficiary of the contract and its information stored as "external party" in Orgnazation template  
 Is that correct?  
 I did not find any information in the Factsheet or documentation.  
 Is there any relation to a service intended? That would help with supplier management and underpinnuing contracts, a process efecte is certified for... 
          
  Vote
  Follow
