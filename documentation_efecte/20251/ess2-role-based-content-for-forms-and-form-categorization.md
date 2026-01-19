# ESS2: Role-based content for forms and form categorization

**Källa:** https://community.efecte.com/t/q6yzxs2/ess2-role-based-content-for-forms-and-form-categorization
**Publicerad:** 2024-10-16T14:39:13.150Z
**Uppdaterad:** 2024-10-16T16:39:13.150000
**Författare:** 

---

ESS2: Role-based content for forms and form categorization

      
    
          
      

        
              Aki YlivarviModerator
            

            
              Aki_Ylivarvi
            1 yr agoWed, October 16, 2024 at 4:39 PM GMT+2
  

           In Progress
        

        
    
Problem statement
The ESS2 shows all content the same way to all end users, so the supported use cases to collect different issues are limited. End users shall see only forms defined to their business roles or locations, as the ESS2 currently shows all content similarly to everyone.
 
Short description
To better meet business process requirements with ESS2, the self-service solution should be capable of configuring role-based access. This would allow end users to report only cases relevant to their specific business roles. The self-service administrator should be able to specify access groups for forms, panels, panel groups, and URLs. This would enable the restriction of business process visibility to different user groups.
 
Use case details
As an admin, I want to define groups of my users so that I can limit what forms, panels, panel groups, or URLs they see.
 
AC:

 In ESS2 admin, introduce a new section under Settings - “Access Groups”
 When the Admin is on the Access Groups page, they will see a list of Access groups
 Admin can add a new group


 
  
   Admin can define the condition that determines which logged-in users are associated with the group
   Admin can select an attribute from a searchable list of reference attributes of the target template
   Admin must select an appropriate value from a list of drop-down of reference values
   On the Access Group definition, the admin can configure multiple conditions for the group
  
 When creating or editing an Access Group, admin can specify what Forms or links are available to the Access Group
 If Access groups are enabled when a user logs into the Self-Service Portal, the system checks if they meet the definition of any existing Access Groups 
  
   If they do not meet any of the definitions, they don’t see any forms
   If they do meet any of the definitions, they see all content for every Access Group they are associated with.
  
 Access groups definitions are not applied to ESM root-level users

          
    
        ESS2
      
    
        Self-Service Portal
      
    
  
  Vote
  Follow
    
            1
