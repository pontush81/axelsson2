# Slowness in Navigation view loading and New view creation in ESM 2025.1 release

**Källa:** https://community.efecte.com/t/q6yfzyb/slowness-in-navigation-view-loading-and-new-view-creation-in-esm-2025-1-release
**Publicerad:** 2025-03-17T14:31:30.947Z
**Uppdaterad:** 2025-03-18T09:28:41.480000
**Författare:** 

---

Slowness in Navigation view loading and New view creation in ESM 2025.1 release

      
    
          
      

        
              Juha HänninenProduct Owner
            

            ESM Product Owner
              Juha_Hanninen.1
            updated 10 mths agoTue, March 18, 2025 at 9:28 AM GMT+1
  

          

        
    
The following issue (CP-10055) has been identified in ESM 2025.1:
Users may experience slow loading of the left-hand side navigation pane, which can prevent successful New view creation if initiated before all the (role/personal) views are fully loaded.
If users click the "Create a new view" button immediately after browser refresh then the "Find views" search doesn't find any templates. But if users wait for a moment until the (role/personal) views are loaded then the "Create a new view" button works normally and finds the searched template.
Workaround
Right after login, opening a new tab or refreshing your browser please wait for a few seconds until the role/personal views are fully loaded. After that you can click on the "Create a new view" button and search for the template.
Status of the issue
Team is actively investigating the root cause on "CP-10055: 'Create a new view' works incorrectly right after page is refreshed". We sincerely apologize for any inconvenience this issue might cause and we encourage you to inform all ESM users about the workaround mentioned above.
          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            1
