# Switching quickly between views might cause data from other views to be shown

**Källa:** https://community.efecte.com/t/m1hdj9y/switching-quickly-between-views-might-cause-data-from-other-views-to-be-shown
**Publicerad:** 2022-05-24T06:41:31.570Z
**Uppdaterad:** 2022-05-24T08:41:31.570000
**Författare:** 

---

Switching quickly between views might cause data from other views to be shown

      
    
          
      

        
              Jonne KaukoProduct Manager
            

            Senior Product Manager & Product Lead, M42 Core & Pro
              Jonne_Kauko
            3 yrs agoTue, May 24, 2022 at 8:41 AM GMT+2
  

          

        
    
 Detected in version: ESM 2022.2.0.1  
 Description: An issue with loading "large" views in certain scenarios has been identified in version 2022.2.0.1. The issue might appear in cases when the user switches to another view of the same type, while ESM is still loading the content for the view, which was initially opened.    
 
 Applies only to cases with the same view type (e.g. switching from a list view to another list view, or from a graph to another graph) 
 Applies to list views and graphs 
 Applies only to "large" views, which are loaded for a while 
 
 Mitigation: The correct data is loaded when reloading the browser page.   
 The root cause will be sorted out once the other parts of the UI (such as the list views and graphs) are renewed later. However, our teams are working on finding a workaround.   
          
    
        Known Error
      
    
  
  Vote
  Follow
    
            1
