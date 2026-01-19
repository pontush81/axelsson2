# EPE: Enhancements for Add / Remove User to / from Group orchestration activities

**Källa:** https://community.efecte.com/t/60ht61t/epe-enhancements-for-add-remove-user-to-from-group-orchestration-activities
**Publicerad:** 2020-12-18T05:57:52.100Z
**Uppdaterad:** 2020-12-18T06:57:52.100000
**Författare:** 

---

EPE: Enhancements for Add / Remove User to / from Group orchestration activities

      
    
          
      

        
              Jukka PapinahoEfecte Employee
            

            
              Jukka_Papinaho
            5 yrs agoFri, December 18, 2020 at 6:57 AM GMT+1
  

           Done
        

        
    
 Story:  
 As a solution owner I want to have more details available, if adding / removing user to / from group fails in some reason. Currently we have possibility to add and remove user to several groups, but missing clear visibility if action fails in some reason.  
  
 AC:  
 
 In the orchestration activity contain additional property: 
   
   Membership failures 
   This property is multi-value string  
   When this orchestration is used, it will provide all of the failed Group DN'a into the chosen data-card attribute 
     
     This will give clear result for administrators, which Groups were actually having some issues 
     Then administrators can execute any actions are required  
      
    
 If user already is a member of the group when adding, not an exception but you should know why it wasn't added to the group 
   
   Information is written in the datacard into the provisioning exception attribute 
    
 If a user is a not member of the group when removing, not an exception but you should know why it wasn't added to the group 
   
   Information is written in the datacard into the provisioning exception attribute 
    

          
    
        EPE
      
    
        IGA
      
    
  
  Vote
  Follow
