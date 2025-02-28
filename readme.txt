Stripe integration
     Matt Freire - https://youtu.be/722A27IoQnk?si=antWjX7mLXuBnL_1
    Michael Herman - https://testdriven.io/blog/django-stripe-tutorial/

    site map: https://www.xml-sitemaps.com/

    https://temp-mail.org/

# E-commerce website

![Main image](documentation/images/header.png)

## About

Candy Rush is an e-commerce website that allows customers to buy unique candy products. It utlizes a log in system that maintains the shopping basket data for each user.
users can see new and popular candy items on the home page that might spark their interest. Once in the 'Our Candy' section of the website, the full selection of candy products is shown, users can opt to select 'quick buy' to quickly add an item to their shpping cart. Or click the product to view more details and add multiple quanities to the basket at onece.
Once shoppers are happy with their candy selections, we have a simple checkout process, where users will be given an opertunity to make edits to the baasket and confirm, then enter their desired shipping data, this data is saved and strored for the users next perchase so the chekout process is made even more easy with auto completed shipping forms. 
at the payment screen users can see the current basket items and their total and given a selection of payemnt options to use via Stripe. Once completed a notification is displayed as well as a conformation email is sent with the order info.


The live site can be found here: [Sugar Rush](https://onehotel-764151fc8ccf.herokuapp.com/)

The github repository can be found here:[GitHub](https://github.com/csdavids519/OneHotel)

The project agile task list can be found here: [Github Projects](https://github.com/users/csdavids519/projects/2)

payment testing credit card number: 4242 4242 4242 4242
---

## UX

The website was designed with UX in mind to create a very simple to navigate store, with fun and fun color selections resembling that of a candy store. Managers have use of the backend database where they can edit product details and other important data in a profecinal looking enviroment. 


### Target Audience

This website is intended for people interested in purchasing products online, starting from bread and finishing electronics, such as TV, smartphones, or other products. It was also aimed to lure people into using this website in their daily lives. This was achieved by implementing a discount system for all customers, additional discounts for loyal customers, and a notification system that allows users to be notified when a product is available. This website may hold many products, and it is essential to make sure that the website is easy to use and navigate. 

Sugar Rush is aimed towards children without becoming off putting adults. As the candy selection is geared towards groups of all ages, its important the younger target audience also finds some joy in selecting their candy. 

### User Stories

User stories and project progress has been recorded with github 

view the kanban board here:
[github projects](hhttps://github.com/users/csdavids519/projects/4/views/1)


## Business Model

The Business Model is B2C, meaning that the company sells products to customers only.
It focuses on individual transactions only.


### A Persona Summary of the customer

Candy Rush is focused on a wide group of people of all types and ages, for this reason the store is designed to have a fun look without compromising on functionality.

### A persona summary of the store personnel

Candy Rush, although fun looking is still a serious and profeciaal compay for this reason the admin section of the web site maintains a business first style approach.

### Strategy Trade-Off

Sugar Rush creates and sells its own unique candy, offering candy products only found at Sugar Rush

- product availability;
- product quality;
- product choice;
- good user experience;

---

## Web Marketing

Facebook and other social media accounts have been created for Sugar Rush as a way to increase reach to existing and potential customers.

[WoWder Facebook Page](documentation/web_marketing/wowder_facebook_mockup.pdf)

---

## Future Development

#### Sorting products by type and taste

At Candy Rush as our product offerings selection grows we plan to implement a type and taste sorting feature so users can more quickly find what interests them regarding sweet, sour, gummy ect.

#### Third-party registration

Allowing users to use Facebook or Google accounts to signin would improve the user experience and allow for new customers to quickly sign up.

#### Monthly basket offers

This feature requires more research time to implement, as the Candy Rush store grows with the offerings we wish to impletment an option for users to subscribe to a monthly random basket of candy automatcaly shipped to their door.

#### Delivery cost calculation

A benift to our customers would be to calculate shipping cots before checkout, this feature would need to be researched before implemented and would use the already available shipping info data from the customer.

---


## Technologies used
- ### Languages:
    
    + [Python 3.11](https://www.python.org): the primary language used to develop the server-side of the website.
    + [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.

- ### Databases:

    + [SQLite](https://www.sqlite.org/): was used as a development database.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.


- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Gunicorn](https://gunicorn.org/): the web server used to run the website.
    + [Psycopg2](https://www.psycopg.org/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [Coolors](https://coolors.co/202a3c-1c2431-181f2a-0b1523-65e2d9-925cef-6b28e0-ffffff-eeeeee) was used to make a color palette for the website.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.
    + [stripe](https://stripe.com/): was used to create the payment system.
    + [Sitemap Generator](https://www.xml-sitemaps.com/) was used to create the sitemap.xml file.

         + [ERD](https://www.xml-sitemaps.com/) 
  https://www.tablesgenerator.com/markdown_tables

---

## Features


Please refer to the [FEATURES.md](FEATURES.md) file for all test-related documentation.


---
## Design

The design of the application is based on Material Design principles. The colors are chosen to be consistent with the [Material Design principles](https://www.creative-tim.com/blog/web-design/12-absolute-principles-material-design/)
The minimalistic approach was used to create something meaningful without moving out of the customer's focus. As this application is a multifunctional (provides full customer experience and business management) application and consists of many components, the decision to implement white spaces was made as it helps to create a more pleasant user experience. It also helps users, whether customers or personnel, to focus on the main content of the application.

### Color Scheme

Sugar Rush color scheme was chosen based off images of real life candy stores. This color scheme creates a fun and playful enviroment that should be expected when buying a fun treat.

  ![Color Scheme](documentation/images/coolors_pallet.png)

### Imagery

- all images on Candy Rush have been develeoped with the help of  OPEN ART
- images chosen for the main page background are to convey the message of happy children with candy to mathch the theam of the candy store.

  ![Background 1](documentation/images/kid_xl.jpg)
  ![Background 2](documentation/images/candy_girl_xl.jpg)

- all images of the candy have also been develeoped with OPEN ART  to depict a unique container of candy. 


### Wireframes

  [WoWder Wireframes](documentation/design/wowder_wireframes.pdf)

---

## Agile Methodology

### GitHub Project Management

  ![GitHub Project Management](documentation/agile/github_project_management.png)

GitHub Project Management was used to manage the project. This method keeps clear what tasks are the current most pressing to be done items.

![GitHub Project Management](documentation/agile/kanban.png)

![GitHub Project Management](documentation/agile/tasks.png)

---

## Information Architecture

### Database

* During the earliest stages of the project, the database was created using SQLite.
* The database was then migrated to PostgreSQL.

### Entity-Relationship Diagram

![ERD](documentation/my_project_visualized.png)


---
## Testing

HTML Validator (ignore errors due to Django HTML) 

| Base      | Passed  |
|-----------|---------|
| base.html | X       |
| 404.html  | X       |
| 500.html  | X       |

| Checkout      | Passed |
|---------------|--------|
| checkout.html | X      |
| payment.html  | X      |
| shipping.html | X      |
| success.html  | X      |


| Home          | Passed |
|---------------|--------|
| index.html    | X      |

| Products            | Passed |
|---------------------|--------|
| product_detail.html | X      |
| products.html       | X      |


| account                      | Passed |
|------------------------------|--------|
| account_inactive.html        | X      |
| base.html                    | X      |
| email_confirm.html           | X      |
| email.html                   | X      |
| login.html                   | X      |
| logout.html                  | X      |
| password_change.html         | X      |
| password_reset_done.html     | X      |
| password_reset_from_key_done | X      |
| password_reset.html          | X      |
| password_set.html            | X      |
| signup_closed.html           | X      |
| signup.html                  | X      |
| verification_sent.html       | X      |
| verified_email_required.html | X      |


| email                        | Passed |
|------------------------------|--------|
| purchase_confirmation.html   | X      |



## Deployment and Payment setup

- The app was deployed to [Render](https://render.com/).
- The database was deployed to [ElephantSQL](https://www.elephantsql.com/).

- The app can be reached by the [link](https://wowder.onrender.com).


Please refer to the [DEPLOYMENT.md](DEPLOYMENT.md) file for all deployment and payment-related documentation.

---

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Render](https://render.com/): for providing a free hosting.
- [jQuery](https://jquery.com/): for providing varieties of tools to make standard HTML code look appealing.
- [jQuery UI](https://jqueryui.com/): for providing varieties of tools to make standard HTML code look appealing.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [geonames](https://www.geonames.org/): for providing a free database on countries, regions, cities.
- [Multiple Video & Image Upload Plugin - jQuery Miv.js](https://www.jqueryscript.net/form/multi-video-image-upload.html): for providing a free plugin to upload multiple videos and images.
- [Stripe](https://stripe.com/): for providing a free payment gateway.
- [htmlcolorcodes.com](https://htmlcolorcodes.com/): for providing a free database on colors.
- [Very Academy Youtube Channel](https://www.youtube.com/c/veryacademy): for brilliant tutorials, which shed the light on the implementation of database with multi-values products, precise explanations of the stripe API, and many other things!
- [birme](https://www.birme.net/): for providing free service to center and crop images.
- [fontawesome](https://fontawesome.com/): for providing free icons.
- [googlefonts](https://fonts.google.com/): for providing free fonts.
- [BGJar](https://www.bgjar.com/): for the free access to the background images build tool.
- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en): for providing a free platform to test website responsiveness
- [GoFullPage](https://gofullpage.com/): for allowing to create free full web page screenshots;
- [Favicon Generator. For real.](https://realfavicongenerator.net/): for providing a free platform to generate favicons.
- [Sitemap Generator](https://www.xml-sitemaps.com/): for providing a free platform to generate sitemaps.
- [Coolors](https://coolors.co/): for providing a free platform to generate your own palette.

### Content and Images

- [unsplash](https://unsplash.com/): for providing a free products' images.
- [Icons8](https://icons8.com/): for providing free access to amazing icons and illustrations to fill out the store.
- [unsplash](https://unsplash.com/): for providing free products' images to fill out the store.
- [chrome developer tools](https://developer.chrome.com/extensions/devtools_inspector): for providing a free platform to test website.
- [adidas](https://www.adidas.com/): for providing free products' data and images to fill out the store on clothes and shoes.
- [fashionunited](https://www.fashionunited.com/): for providing content for the newsletter;
- [dell](https://www.dell.com/): for providing free products' data and images to fill out the store on computers and laptops.
- [nike](https://www.nike.com/): for providing free products' data and images to fill out the store on clothes and shoes.
- [artsaber](https://www.artsabers.com/): for providing free products' images to fill out the store on lightsabers data and images.
- [backwaterreptiles](https://www.backwaterreptiles.com/): for providing free products' images to fill out the store on tarantulas' data and images.
- [Yum Of China](https://www.yumofchina.com/chinese-beer/): for providing free data on Chinese beer.
- [lego](https://www.lego.com/): for providing free products' data and images to fill out the store with toys.
- [maggie](https://www.maggie.com/): for providing free products' data and images to fill out the store with maggie products.
- [barilla](https://www.barilla.com/): for providing free products' data and images to fill out the store with pasta.
- [LG electronics](https://www.lg.com/): for providing free products' data and images to fill out the store with electronics.
---

## Acknowledgments

- [Tim Nelson](https://github.com/TravelTimN) was a great supporter of another bold idea of mine for this project. Tim guided me through the development of the project and helped me to learn a lot of new things by challenging me to do something new.
- [Aleksei Konovalov](https://github.com/lexach91), my husband and coding partner, assisted me greatly in product values js selection control implementation and helped me to stay sane.
- [Very Academy Youtube Channel](https://www.youtube.com/c/veryacademy) provided great insight on the implementation of the database with multi-values products, precise explanations of the stripe API, and many other things! This Youtube channel has plenty of brilliant tutorials that shed light on Django's most curious and useful aspects.
