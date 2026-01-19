# Transporting views from one to another environment

**Källa:** https://community.efecte.com/t/63am7g/transporting-views-from-one-to-another-environment
**Publicerad:** 2019-07-11T06:58:27.163Z
**Uppdaterad:** 2019-07-11T08:58:27.163000
**Författare:** 

---

Transporting views from one to another environment

      
    
          
      

        
              Peter Schneider
            

            Chief Evangelist / Storyteller
              Peter_Schneider
            6 yrs agoThu, July 11, 2019 at 8:58 AM GMT+2
  

          3replies
        Aki Koivukoski5 yrs agoThu, May 28, 2020 at 2:00 PM GMT+2
  
         Done
        

        
    
ContentsDescriptionAcceptance CriteriaDescription 
 As an Efecte administrator, I want to build all views to test environment first and then safely import them to production environment by using export and import functionalities.  
Acceptance Criteria 
 
 admin shall be able to export and import any kind of views from the Administration UI (graphical, calendar, and list views) 
 exports can be initiated from the Views tab in the Administration UI by selecting the desired view of one role in the navigation panel and then selecting "Export" from drop down menu 
 export feature shall export selected view to XML file 
   
   name of the file shall be <view name>_<date>_<time>.xml  
   the translations shall be included when exporting view 
   the exporting should fail if attributes used in the view does not have attribute code 
   failed export shall be notified by notification which must be dismissed by admin 
    
 the view export must be logged in the ITSM configuration log 
 admin shall be able to import views to another ESM environment in the administration UI by selecting "Import" from the drop down menu 
   
   a pop up dialog for field selection shall be displayed to user 
   imported views shall be always created as new views 
   import shall fail with error notification if matching role name is not found 
   import shall fail with error notification if all attributes in the imported view are not found in corresponding template 
   successful import shall be confirmed by temporary notification 
   failed import shall be notified by notification which must be dismissed by admin 
     
     notification shall inform the reason why the import failed 
      
   if view name and role matches, the existing view shall be renamed in a way (_old) that admin can either rename or delete the old one after the import is completed 
   if a reference data card or a value of static attribute is not available in the target system 
     
     import shall be successful with warning,  
     condition values are pointing to "all" 
      
    
 the view import must be logged in the ITSM configuration log 
 
 Note:  
 
 exporting and importing of multiple views shall not be supported 
 old views shall basically remain as they are in order to ensure ability to add views during service hours without impacting user experience 
 new views shall be displayed to user after reloading the browser 

          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            2
