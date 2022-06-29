# Testing Schedule 

## Python file checker with PEP8

![PEP8 schedule](static/images/testing/testingschedule-pep8.png)  

All Python files were entered into the PEP8 online checker to find if it contained any errors. In some cases there were errors notified which was duly corrected.  A few errors were raised in the settings file, however these were default django authorisation code and could not be changed to remove the errors.

Individual screenshots for the PEP8 Validators can be found below:

#### Clean Eats Kitchen Folder
* [asgii.py](static/images/testing/asgi-pep8.png)
* [settings.py](static/images/testing/settings1-pep8.png)
* [urls.py](static/images/testing/urls1-pep8.png)
* [wsgii.py](static/images/testing/wsgii-pep8.png)

#### Recipes Folder
* [admin.py](static/images/testing/admin-pep8.png)
* [apps.py](static/images/testing/apps-pep8.png)
* [forms.py](static/images/testing/forms-pep8.png)
* [urls.py](static/images/testing/urls2-pep8.png)
* [views.py](static/images/testing/views-pep8.png)

## CSS and JavaScript Checker with W3C Online

![W3C and Jshint schedule](static/images/testing/css-js-schedule.png)  

Individual screenshots for the Validators can be found below:
* [CSS](static/images/testing/css-validator.png)

* [JS](static/images/testing/javascript-validator.png)

## HTML Checker with W3C Online

For my HTML validator I initially ran into some issues as I tried to input the text direct and the validator wouldn't recognise Jinja templating. Therefore I checked via the URI. This is the result:

![HTML](static/images/testing/html-validator.png)  
The warning related to a section within my footer however this had come from bootsraps footer tempate, therefore I have not touched this code.