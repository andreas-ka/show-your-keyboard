# Show your Keyboard

I've included for you below all my tests on this project.
_____________________________________________________________________________

## Content:
- ### HTML, CSS and Contrast
    - [W3 validator](#w3-html-checker)
    - [W3 CSS](#w3-css-checker)
    - [Contrast](#contrast-checker)
- ### Lighthouse
    - [Mobile](#mobile)
    - [Desktop](#desktop)
- ### Rensponsiveness and testing
    - [Rensponsiveness](#rensponsiveness-and-further-testing)
- ### Kanban board with bugs
    - [Kanban board](#full-project-board-with-bugs-link)
- ### PEP8
    - [PEP8](#pep8-1)


_____________________________________________________________________________


### W3 HTML Checker
Done by choosing "View Page Source" and past in on the W3 HTML checker.    

Index.html.    
![Screenshot](./static/images/w3_html_index.png)    

Posts view.        
![Screenshot](./static/images/w3_html_posts.png)

Postdetails   
![Screenshot](./static/images/w3_html_postdetail.png)    

Profile   
![Screenshot](./static/images/w3_html_profile.png)  

Create post  
![Screenshot](./static/images/w3_html_create_post.png)  

Register (shows 4 errors but thats code directly from django's form, see image below)   
![Screenshot](./static/images/w3_html_postdetail.png)  
![Screenshot](./static/images/w3_html_register_code.png)    

Login.     
![Screenshot](./static/images/w3_html_login.png)    

Error 403.     
![Screenshot](./static/images/w3_html_403.png)  

Error 404.    
![Screenshot](./static/images/w3_html_404.png)  

Error 500.    
![Screenshot](./static/images/w3_html_500.png)  

_____________________________________________________________________________


### W3 CSS Checker
![CSS checker](http://jigsaw.w3.org/css-validator/images/vcss)
![CSS checker](http://jigsaw.w3.org/css-validator/images/vcss-blue)

_____________________________________________________________________________


### Contrast Checker
Used a11ys Color contrast validator [Link](https://color.a11y.com)   
![Screenshot](./static/images/contrast-readme.png)    

WAVE Web Accessibility Evaluation Tool.   
(Contrast warnings noted, I have decided to keep it due to aesthetics)   
Lighthouse shows accessibility very high, and that contradicts this.     
![Screenshot](./static/images/wave_tool.png)
_____________________________________________________________________________

### Lighthouse
Scores from googles Lighthouse are below.     
Much of the low performance seem to be due to the host heroku, nothing i can fix myself. 
Result using Chrome and inkognito mode displays an increase in performence significantly.

#### Mobile
Index.html.    
![Screenshot](./static/images/mobile_lighthouse_index.png)     

Posts.    
![Screenshot](./static/images/mobile_lighthouse_posts.png)    

Post details.     
![Screenshot](./static/images/mobile_lighthouse_postdetail.png)    

Login.        
![Screenshot](./static/images/mobile_lighthouse_login.png) 

Profile.       
![Screenshot](./static/images/mobile_lighthouse_profile.png) 

Register.        
![Screenshot](./static/images/mobile_lighthouse_register.png) 

_____________________________________________________________________________

#### Desktop
Index.html.     
![Screenshot](./static/images/desktop_lighthouse_index.png)

Posts.   
![Screenshot](./static/images/dekstop_lighthouse_posts.png)     

Post details.    
![Screenshot](./static/images/desktop_lighthouse_postdetails.png)    

Register.   
![Screenshot](./static/images/desktop_lighthouse_register.png)     

Profile.    
![Screenshot](./static/images/desktop_lighthouse_profile.png)    

Login.       
![Screenshot](./static/images/desktop_lighthouse_login.png) 

_____________________________________________________________________________

### Rensponsiveness and further testing

- All done and registered in my Google todo docs, bugs also logged in my Kanban board under projects on Git Hub.   
Below is a screenshot snippet from the google docs, please click the link to see the entire document.   
[Link to google docs](https://docs.google.com/spreadsheets/d/1s44J9bTQyVY0vnPAtlb3FIwGDRyj-bNHVxq4E8CToME/edit?usp=sharing)    
![Screenshot](./static/images/testing_docs_readme.png)    

_____________________________________________________________________________


### Full project board with bugs [Link](https://github.com/users/andreas-ka/projects/6/views/1)     
![Screenshot](./static/images/kanban_board_bugs.png)   


_____________________________________________________________________________

### PEP8
### home app
home forms.py.    
![Screenshot](./static/images/python_linter_home_forms.png)     
home models.py.   
![Screenshot](./static/images/python_linter_home_models.png)     
home views.py.   
![Screenshot](./static/images/python_linter_home_views.png)   
home urls.py.  
![Screenshot](./static/images/python_linter_home_urls.png)    
_____________________________________________________________________________

#### Project
Project settings.py (note that some lines need to remain to long)    
![Screenshot](./static/images/python_linter_project_settings.png)    
Project urls.py.  
![Screenshot](./static/images/python_linter_project_urls.png)    
Project views.py.   
![Screenshot](./static/images/python_linter_project_views.png)    
_____________________________________________________________________________

#### users app
Users forms.py.    
![Screenshot](./static/images/python_linter_users_forms.png)   
Users models.py.     
![Screenshot](./static/images/python_linter_users_model.png)     
Users urls.py.    
![Screenshot](./static/images/python_linter_users_urls.png)    
Users views.py.   
![Screenshot](./static/images/python_linter_users_views.png)   

[Back to Readme](README.md)