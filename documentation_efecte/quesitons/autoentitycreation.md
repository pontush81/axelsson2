# AutoEntityCreation

**Källa:** https://community.efecte.com/t/60yls4r/autoentitycreation
**Publicerad:** 2025-02-13T11:02:58.827Z
**Uppdaterad:** 2025-02-13T12:02:58.827000
**Författare:** 

---

AutoEntityCreation

      
    
          
      

        
              Oliver Burtscher
            

            
              Oliver_Burtscher
            11 mths agoThu, February 13, 2025 at 12:02 PM GMT+1
  

          1reply
        Antti AholaEfecte Employee8 mths agoMon, April 28, 2025 at 3:08 PM GMT+2
  
        

        
    
Hello community
I'm trying to use a "AutoEntityCreation" handler. What I would like to do is: When I create a datacard in Template "hp_sam", I automatically want to create a datacard in template "hp_sam_log". This should only happen when I create a new hp_sam - datacard.
The datacard in "hp_sam_log" should be filled with at string value for attribute "hp_sam_log_details_short" = "New HP SAM has been created!". And it also should contain a reference to a required attribute in "hp_sam" which has the attribut name "hp_sam_basic_short_name" -> in "hp_sam_log" it's called "hp_sam_log_related_sam_app". The if I create a "hp_sam" with hp_sam_basic_short_name "ProductA", this value also should be put in the "hp_sam_log_related_sam_app".
Can anyone tell me how this AutoEntityCreation handler should look like in it's attribute metadata? Unfortenatuly, I don't understand Efecte's documentation here.
Thanks!
Oli
          
  Like
  Follow

## Bilder

![Bild](images/autoentitycreation_8b8d52fb.png)


