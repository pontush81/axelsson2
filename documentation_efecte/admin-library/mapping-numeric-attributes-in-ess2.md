# Mapping numeric attributes in ESS2

**Källa:** https://community.efecte.com/t/y4ypztr
**Publicerad:** 2025-12-22T15:05:45.897Z
**Uppdaterad:** 2025-12-22T16:05:45.897000
**Författare:** 

---

Mapping numeric attributes in ESS2

      
    
          
      

        
              Oliver Burtscher
            

            
              Oliver_Burtscher
            4 wk agoMon, December 22, 2025 at 4:05 PM GMT+1
  

          5replies
        Aki YlivarviModerator3 days agoFri, January 16, 2026 at 4:38 PM GMT+1
  
        

        
    
Hi all
As an admin, I just wanted to create a field in an ESS2 form that is mapped to an attribute with datatype "numeric" in the template. But.... it seems it can't. No numeric attribut is shown in the destination field dropdown.
Why not? It seems to be quite common to have forms that require to enter numbers, right?
Does anyone have a hint - or a workaround?
I could change that attribute to type "static string", they can be mapped in ESS2. But as the name already says, they are strings. In addition, the user then only could use numbers in that static string list. Which would work in my case (only numbers from 1 to 10 are allowed). But then, after the order has been made, I need that number to calculate things. And strings are not a good choice for calculations, as we all know. So I would have to create a listener that copies that string with a formula into a number field.
This is not nice. And does only work for a given range of numbers. I could have a normal string field and ask the user to enter the number. But I then could NOT validate if the user really entered a number (or could I? Is there any kind of validation?).
Thanks for any help! I really appreciate!
          
    
        ESS2
      
    
  
  Like
  Follow
    
            1

## Bilder

![Bild](images/mapping-numeric-attributes-in-ess2_8b8d52fb.png)


