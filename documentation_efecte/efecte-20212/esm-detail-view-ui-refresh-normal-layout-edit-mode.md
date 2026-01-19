# ESM: Detail View UI Refresh - Normal Layout - Edit Mode

**Källa:** https://community.efecte.com/t/p8h331x/esm-detail-view-ui-refresh-normal-layout-edit-mode
**Publicerad:** 2020-05-13T06:21:54.253Z
**Uppdaterad:** 2020-08-07T06:57:53.773000
**Författare:** 

---

ESM: Detail View UI Refresh - Normal Layout - Edit Mode

      
    
          
      

        
              Peter Schneider
            

            Chief Evangelist / Storyteller
              Peter_Schneider
            updated 5 yrs agoFri, August 7, 2020 at 6:57 AM GMT+2
  

          3replies
        Aki Koivukoski4 yrs agoWed, February 10, 2021 at 12:19 PM GMT+1
  
         In Progress
        

        
    
ContentsUser story:AC's:User story: 
 As a user of Efecte's Service Management Tool (ESM) I want to enjoy a modern user interface editing a data card in order to work not only effectively but also with delight.  
AC's: 
 Common:  
 
 the usability, interoperability, technology, and layout requirements of the View mode story must be met also in Edit mode 
 
 Detail View Title Bar  
 
 the title bar must display the value of the primary attribute 
 the title bar must display the template icon 
 the title bar must display the folder of the data card 
   
   clicking on the folder name allows the user to select another valid folder for the data card from a drop-down selection 
    
 the title bar must display who is viewing and editing the data card when this capability is enabled in the platform settings (agile swarming) 
 the title bar must display the Visual Workflow status 
 the title bar must show the button for saving the changes 
 the title bar must show the button for canceling the editing of the data card 
 the title bar must allow activating editing of all classes 
 the title bar must allow collapsing/expanding of all classes 
 the title bar must allow selecting more data card actions from the More Menu 
 the interaction buttons on the title bar shall be placed below the value of the primary attribute on mobile devices 
 presentation texts must be localized according to the user's profile preferences 
 the color of the buttons must adhere to button customization capability 
 
 Detail Content Area  
 
 the background color is the blue color of the Finnish flag in 97% transparency (hexadecimal code is 002F6C) 
 the class names shall be displayed in larger, bold font in dark blue 
 the content of all classes must be shown according to the template layout editor 
   
   all content of all classes can be expanded or collapsed with the button in the title bar 
   a single class can be expanded or collapsed using by clicking on the dedicated icon beside the class name 
     
     tooltip is supported 
      
    
 the attribute name is displayed in bold font a dedicated row 
 the help text icon is displayed in the same row of the attribute name 
 the attribute value is shown below the attribute name 
 attributes which are configured to be shown in "Edit Mode Only" and "View and Edit Mode" are displayed 
 attribute names can be wrapped if necessary (comment: unlikely but supported for backward compatibility) 
 class and attribute names must support multi-language configuration support 
 the value of string attributes shall be displayed on the full width of the column 
 date, date&time, number, and decimal number values shall be displayed on the left-hand side of the column 
 text attribute values shall be shown in a field with configurable text height 
   
   text attributes must have a new data defining the height of the text box by the number of rows 
   the default value is 7 rows 
    
 reference values shall be shown in blue font color 
   
   hovering over reference values shall display the values selected for the corresponding reference template 
    
 attributes which can be edited shall have an input box with a white background and light grey outline 
   
   reference search filters buttons shall be shown inside of the input box 
    
 the attribute which is currently being edited shall be highlighted with a dark grey outline 
 the cursor shall be placed automatically in the first field which can be edited by the user 
 interaction buttons such as from TicketReserve Handler, Quickfill Handler, or Transform interactions shall be displayed in the right-hand corner under the attribute value 
 background processes such as Visual Workflow Automations, Handlers, and Listeners shall be executed as in the 2014 UI design depending on the UI interactions 
   
   an error message shall be displayed in a pop-up box when not all mandatory fields have a value when saving the record 
     
     mandatory fields missing a value shall be marked with a red background-color 
      
   validator error messages shall be displayed in a pop-up box 
     
     validated fields failing the validation shall be marked with a red background-color 
      
   listener actions leading to a user message shall be shown in a pop-up box 
   Conditional attributes shall be displayed according to the configured logic whenever values in the related attributes change 
    
 
 NOTE!: Email, tables, work logs, text notes, and other major elements are handled in dedicated stories 
          
    
        Service Management Tool
      
    
  
  Vote
  Follow
    
            3
