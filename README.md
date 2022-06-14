# Clean Eats Kitchen

Hello! This is my Fourth Project with the Code Institute and I have created a food recipe site called Clean Eats Kitchen. It has been built in Django using Python, JavaScript, CSS, and HTML, and enables users to create and share healthy recipes with other users around the world. It has been targeted toward people who want to eat healthy while allowing the meals to have a 'cheat' feel. Users are able to create their own accounts in order to share their own recipes. They can also comment and like recipes. 

This site has been centred around a centric database and allows full CRUD functionality. The site also ensures role-based permissions to separate user functionality and restrict certain content. 


---

live website link here

(Am I Responsive screenshots here)


## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Database Schema](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
---

## UX

### The Strategy Plane  

Clean eats kitchen is a friendly and social recipe sharing platform, which should help connect fellow foodies around the world. The elements and design of the website is to be attractive and enjoyable, whilst ensuring users can follow instructions in a clear and concise manner.  

#### Sites ideal user 
- Food lover looking to share their healthy recipes with others
- Food lover looking for recipe inspiration
- People with a healthy eating diet and lifestyle (e.g. Gym)
- Someone wishing to connect to foodies online
#### Site Goals
- To provide users with a website to find healthy recipes
- To provide users with a website to share their own recipes
- To provide users with a website to discover new recipes
- To provide users with a website where they can communicate with other users in a friendly environment


## The Skeleton Plane
---
### Wireframes
To create my wireframes I used Balsamiq, which is a free-to-use wireframe software. I wanted to create my basic wireframes for the three main screen widths such as Desktop, Tablet, and Mobile. In order to help my design thinking process, I created the 4 main pages for my site so I can follow a similar style for my other smaller pages. Please follow the links below to view each wireframe individually.

#### Index page:

* [Index page desktop wireframe](/assets/wireframes/desktop-index.png)
* [Index page tablet wireframe](/assets/wireframes/tablet-index.png)
* [Index page mobile wireframe](/assets/wireframes/recipe-detail-mobile.png)

My index page aims to capture the users by being visually attractive and having a clear structure. My index page aims to be simple in layout with a clear indication of what the site’s aim is. 

#### Recipes Page:

* [Recipe page desktop wireframe](assets/wireframes/desktop-recipes-overview.png)
* [Recipe tablet desktop wireframe](assets/wireframes/tablet-recipes-overview.png)
* [Recipe mobile desktop wireframe](assets/wireframes/mobile-recipe-overview.png)

My recipes page section should be clearly structured in meal time order (Breakfast, dinner, tea, treats). This should allow ease of navigation and should help users narrow their search field without needing the known the exact recipe they are after. This page should be again visually beautiful through colours and animations. 

#### Recipe instructions:

* [Individual recipe instructions page desktop wireframe](assets/wireframes/desktop-recipes-steps.png)
* [Individual recipe instructions page tablet wireframe](assets/wireframes/tablet-recipe-steps.png)
* [Individual recipe instructions page mobile wireframe](assets/wireframes/mobile-recipe-steps.png)

The recipe instructions should be again simple in design and well structured. This should include unordered bullet points for the ingredients and numbered bullet points for the instructions so user can clearly distinguish each section. Information on this page needs to be clear and concise for readability. 
#### Profile Page:

* [Profile page desktop wireframe](assets/wireframes/desktop-profilepage.png)
* [Profile page tablet wireframe](assets/wireframes/tablet-profilepage.png)
* [Profile page mobile wireframe](assets/wireframes/mobile-profilepage.png)

The profile page aims to be a hub where users can edit and delete their own profiles. This should act as a page where they can easily navigate to previous recipes they have liked and their own recipes they have added to the website. 

---

### Database Schema

To create my back end database I have used the built-in PostgreSQL from Heroku. I have designed my database using [drawSQL](https://drawsql.app/), this is a free-to-use software however quite limited, as some fields didn’t allow me to overwrite them, such as Image fields. To help with the authentication Django has a built-in user Model Allauth which helps save time creating my own Model.  

I have created my own user profile model, as this will be needed to allow users to create their own recipes. I have then split the recipe for Ingredients and Steps because a recipe could have many different steps and ingredients. To help with this logic I used [sqlservercentral](https://www.sqlservercentral.com/forums/topic/database-design-for-storing-recipes) & [dev.to](https://dev.to/amckean12/designing-a-relational-database-for-a-cookbook-4nj6).  
![Database Diagram](/assets/wireframes/database-design.png)
#### Technologies Used

* HTML
    * HTML was used as the base language for the templates created for the site. 

* CSS
    * Custom CSS style was used to create my own look and presentation of the site to avoid the site looking too much like a bootstrap site.

* Bootstrap 5.13
    * Bootstrap was used for general layout and ease of creating elements within the site with its predefined templates.

* Jinja/Django Templating
    * Jinja/Django templating language was utilised to create HTML, XML or other markup formats that are returned to the user via an HTTP response

* JavaScript
    * To create custom functionality and create responsive elements and interfaces for the user

* Python
    
* Django
    * Python Framework
    * Django AllAuth 

* Heroku
    * Was used as the cloud based platform to deploy the site.

* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.

## Credits

* A lot of my inspiration was taken from the Code Institute Django walk through project.
* [CodingEntrepeneurs](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL) YouTube walkthrough.
* [Codemy](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) YouTube walkthrough.