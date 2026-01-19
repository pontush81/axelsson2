# Offer a "StateTransition" handler (in conjunction with HiddenState)

**Källa:** https://community.efecte.com/t/m1yp1xm/offer-a-statetransition-handler-in-conjunction-with-hiddenstate
**Publicerad:** 2026-01-12T11:59:14.053Z
**Uppdaterad:** 2026-01-12T12:59:14.053000
**Författare:** 

---

Offer a "StateTransition" handler (in conjunction with HiddenState)

      
    
          
      

        
              Peter Scheffczyk
            

            Advisory Solution Consultant
              Peter_Scheffczyk.1
            7 days agoMon, January 12, 2026 at 12:59 PM GMT+1
  

          2replies
        Peter Scheffczyk7 days agoMon, January 12, 2026 at 1:55 PM GMT+1
  
        

        
    
Often customer want to restrict status transitions of process objects, examples:

 Status "closed" should never be set manually
 Status "new" should never be set manually
 Status "waiting for approval" should never be changed manually, but only through approval actions
 ...

Currently there are no out-of-the-box possibilities to control "allowed next status" for each status value.
There are a couple high-effort configuration concepts that simulate this, but they all have drawbacks (e.g. lose multi-language functionality by using references) and are high-effort maintenance.
It would be very helpful if the platform offered a "StateTransition" handler that would allow for each defined status value a comma-separated list of allowed "next status" values.
Since often on status we have a hiddenState handler, these two handlers should be combined.
E.g. in the metadata, I could configure it like this
New  //  Assigned,Solving,Waiting for customer
Assigned // Solving,Waiting for customer,Resolved
...
Logic like workflow "set value" actions should not be restricted and also expressions should not be restricted, but UI selection should be controlled by these settings.
          
  Vote
  Follow
    
            5
