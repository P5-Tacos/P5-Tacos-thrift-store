# P5-Tacos-thrift-store

|Name|	Github   | |
|--|--|--|
|Colin Szeto  |  colin-szeto| Pair 1|
|Samuel Mahjouri  | iBraskyy | Pair 1|
| Andrew Zhang | Ketherbug | Pair 2|
|Brayden Basinger  |  BraydenBasinger| Pair 2|

```diff
@@\/ Link to the scrum board below \/@@
```
#### Link to scrum board: https://github.com/orgs/P5-Tacos/projects/1
#### Link to project plan and requirements: https://docs.google.com/document/d/1KfMvlYYCx5RgCIgN95gB9F38R15c6u2dG-cIQ-A9-oY/edit
#### Link to easter egg: http://timetothrift.cf/easter_egg_college/

## Overview
##Wow 
As there are multiple systems embedded in the same project it was important for the team to organize all user information in separate table for each system

- [module.py](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/module.py) contains all of the database's setup. This file was created to allow for tracking of users across multiple projects.
- [userDN](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L45-L58) contains all of the users. The contents of the database can be found [here](http://delnorteeats.cf/easter_egg/admin) in the admin page of Del Norte Eats.
- [userEE](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L78-L88) is represented by “Users Del Norte Eats” [table](http://delnorteeats.cf/easter_egg/admin)
- [userRR](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L90-L100) is represented by “Runners Del Norte Eats” [table](http://delnorteeats.cf/easter_egg/admin)
- [orderEE](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L60-L76) is represented by “Orders” [table](http://delnorteeats.cf/easter_egg/admin)

[userTT](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L15-L30) is represented in the Admin page in Time to Thrift [table](http://delnorteeats.cf/time_to_thrift/admin)
Highlights of the admin pages is that the passwords are represented by asterisks for each character in the table. On hover the asterisks are replaced with the actual characters of the password. [Here is the front end of the logic](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L50-L56)
#### Front end Viewing data

## Changes Log
#### Week 10 
- Andrew
- 	- Finshed the Login system user experience [update](http://timetothrift.cf/admin)
- 	- Started Login differentiation. 
- Colin 
	- enable website usage as guest [ticket](https://github.com/orgs/P5-Tacos/projects/1#card-55469455)
		- [refrence](https://flask-login.readthedocs.io/en/latest/#anonymous-users)

	- created [read functionality](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/f99db669d9521fac7bbfae77843a075a68be326b/app.py#L221-L234) for shopping cart from database
	- embedded collegeboard [requirement reflection](http://timetothrift.cf/easter_egg_college/AP_CSP_Requirements) on live site
	- added in js for the [snack form](http://timetothrift.cf/easter_egg/singlepage_form) [ticket](https://github.com/orgs/P5-Tacos/projects/1#card-55471330)
		- highlighting the total cost through js
		- the dynamic options opend based on specific selection 

- Brayden
	- This week I included some CSS into my reaction test game. I did this to make the game more fun for the user. 
	- I included a color changing shape to tap because thi would make the UI more appealing
	- I used some CSS [here](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/15731442800c96308670211066674ada679fc715/templates/reactiontest.html#L11)

- Sam
	- This week I worked on adding more CSS into our DelNorteEats site 
	- I worked on experimenting with creating a new way (for me) to loop [Link to template that will be defined with the values from the list](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/templates/clothes_info.html) [link to app route where the list will be called upon -- lines 247 to 257](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/app.py)
	- I also worked with Brayden on putting some CSS into his game. 

#### Week 9

[AP Requirement Doc](https://docs.google.com/document/d/13WzGAZ40KE8HZguGc2O9igHdUENnmVyBys2u7PRZuns/edit)

- Andrew
	- This week I mainly worked on finishing up the login session with Colin. [link to the user system](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/app.py) and [link to logged in page](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/templates/logged_in.html). The login system allows the program to recognize the logged in users.  
	- 1. Ability to clearly review tickets and suggestions 5pts
	After our crossovers from last week, we decided to improve our login system to add in a session. As the database for the items is fixed, I decided to work on session with Colin and make the login system working. 
	- 2. College Board and Crossover visibility in project 4pts
	We improved the asthetics for the project and added in more control over the user systems which align for the college board requirements on data and visuals. I added in more algorithms and data management into the project. I can do these things with a more timely fashion, so I will deduct one poing from me. 

### Colin Contributions demo: https://youtu.be/EViKxyIv7CE
- I am currently unable to get post working on the rpi and have recorded a demo of the features on my local machine
- Colin 
	- [link to ticket](https://github.com/orgs/P5-Tacos/projects/1#card-55258546)
	- [Link to admin page](http://timetothrift.cf/admin) where all user information is stored
	- This week I was focused in making the add to cart system work:
		- procedure:
			- open up [Link to admin page](http://timetothrift.cf/admin)in parrallel window to see the saved shopping list update when you eventutaly save shopping list to database
			- slected any item from the gallery pages to add to cart 
				- [Thrifty Threads](http://timetothrift.cf/thriftythreads)
				- [Barbarella](http://timetothrift.cf/barbarella)
			- navigate to [shoping cart icon](http://timetothrift.cf/logged_in) at right side of nav bar to see the items in shopping cart
			- remove item from shopping cart with the remove from cart button 
			- press the save shopping list button, notice how the admin page will now update it's final column to reflect the information in the current shopping cart
			- log out to log out and see that the items are contianed within the database
		- implmenting a system to track where was the location the user was on the page(to get rid of needing to scroll back down to where you were last at)
			- [to protect scroll position in reloading the page](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/templates/gallery.html#L70-L78)
			- [to set the scroll position when the page is loaded](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/templates/gallery.html#L83-L88)
			- [to measure where the current position of the scroll bar](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/templates/gallery.html#L92-L99) this measurement is connected to a [global variable](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/app.py#L254-L255) when the corresponding gallery page is reopened the user is placed where they last were
				- notice as we need to pass this global variable into a javascript function, we are passing this variable in through a [son format](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/app.py#L303)
		- implmenting a system to track which item was added to cart [hidden feild connected to add to cart button](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/app.py#L247)
		- system to redirect user to page they selected item from [hidden feild connected to add to cart button](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/app.py#L246)
		- system to display items in cart
			- we store information about each item in a [itonary which is appended onto a list](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/app.py#L263-L264)
			- this information is passed into the [ser profile page](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/app.py#L229)
		- system to save the items in cart to data base	[using jinja to display contents of database](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/dc1b1e125df824cd88d04e18acb7bf7a92efbaa8/app.py#L318-L320)
		- I am still working on the R part of CRUD to automatically populate the shopping cart with previous data stored in the JSON file in the data base

- Sam [runtime link](http://timetothrift.cf/easter_egg/multipage_form) type in giberish for the first two feilds and press next
	- This week I mainly worked on finishing up our multi page form. [link to image directory](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/static/images/delnorteeatsfood). The link takes you to the image directory which contains all the images i used for our multipage form. Besides that, I worked on creating another table for the form and was able to incorporate buttons: which i plan on connecting to an actual system that will work as a cart where users can "buy now". I also helped out Brayden a bit with his project. 
	- 1. Ability to clearly review tickets and suggestions 5pts
	After our crossovers from last week, we were suggested to improve our UI. That has been the focus for this week as I have now incorporated images with a loop. Also, the ticket from this week was for me to do that very thing --improve UI-- which is what I have somewhat done using buttons and loops for images. 
	- 2. College Board and Crossover visibility in project 3pts
	I learned how to use another type of loop through the help of colin. In this case, the loop that colin taught me was much quicker for me to use rather than what I had previously known. I demonstrated meeting the criteria of CB requirements by simply uisng more jinja. However, I did not do everything I had wanted to for this week, so that is why I am deducting 2 points off myself.
	
- Brayden [run time](http://timetothrift.cf/reactiontest)
	- This week I worked on making a reaction test game [link to code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/76136fb252475a2090279eff1f0d395f0f9e92c3/templates/reactiontest.html#L1) since we already were happy with our website. 
	- 1. Ability to clearly review tickets and suggestions 5pts
	On the README I elaborated on why I did this reaction test. There are also explanations on how to play the game on the actual page. My ticket this week was to do the 	reaction test, and I did that.
	- 2. College Board and Crossover visibility in project 5pts
	I learned many functions that are on the college board requirements. I also learned how to do more jinja and passing data, etc… One of the College Board requirements I met was the Big Idea 1 - Creative Development. I did this when I developed my code with my group members and added functions like get random color that I did not know about before. I also learned how to add tabs on a NavBar from the crossover group that did that. I incorporated that into our project by adding the tab ReactionTest
	- 3. Mini code Review focus on tickets and project.
	(Self explanatory) Look at what I made. Also look at the README on GitHub and there are directions on how to work the reaction test and how to start it on the page. For example, when I game is over I had a pop up that said “CTRL + R” to play again. This will reload the page



#### Week 8 
- Andrew 
	- worked on uploading images to the [database](http://timetothrift.cf/database)
	- [link to code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/69e606a41f10d1dcab6fa717f2e94fce20958995/app.py#L124-L126)
	
- Colin 
	- worked on multi [page form](http://timetothrift.cf/easter_egg/multipage_form)
	- [link to code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg/templates/easter_egg/multipage_form.html)
		- [link to view](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/69e606a41f10d1dcab6fa717f2e94fce20958995/views/easter_egg/templates/easter_egg/multipage_form.html#L30-L47) of the code, itterating to display the avalible food options for the user 
		- [link to model](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg/food.py) storing all of the information for all of the food items

#### Week 7 

- Andrew [Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53785119)
	- Worked on the login and the [sign-in page](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg/view.py) of the Del Norte Eats
	- Started constructing the order histories for the [Customers](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg/templates/easter_egg/auth_user.html)

- Sam [Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53785634)
	- I worked on adding to user flow so I could begin implementing jinja into our project. [Link to User flow page](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg/templates/easter_egg/ordernow.html); I also used CSS. Then after that I created a contactus form [Link to contact form](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg/templates/easter_egg/newcontactus.html)

- Colin [Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53784984)
	- started the week off storyboarding the next project out, see [embedded google slide](http://timetothrift.cf/easter_egg/) 
	- utilized [Image Map Generator](https://www.image-map.net/) to create a [rough image map](http://timetothrift.cf/easter_egg/image_map_dnhs) of buttons grouping specific buildings togehter (a, p, d buildings etc)
		- click the administration building and a dialog box will appear to denote that the map reacted to the selection 
		- [link to code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg/templates/easter_egg/image_map_dnhs.html)
	- was able to construct the [Who am I page](http://timetothrift.cf/easter_egg_college/who_am_i) 
	- [link to code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/views/easter_egg_college/templates/easter_egg_college/who_am_i.html)
		- sources [How To Cleanly Export From Google Docs To HTML](https://www.techjunkie.com/google-docs-to-html/)
			- this will allow the user to maintain image locations throughout the doucument, however it was unable to preserve all of my hyper links
		- specifically used [HTML Cleaner](https://html-cleaner.com/)
			- this allowed me to copy and paste the contents of the team's google docs into the feild to then convert them into html to paste into the project
	- placed in the [college board requirements](http://timetothrift.cf/easter_egg_college/college_board_requirements) that our Makeup Project Satisfied utilized [HTML Cleaner](https://html-cleaner.com/)
	- was able to utilize [blueprints](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views) to better section off the code for easier debugging and maintenece 
		- allowed the team to create diffrent nav bars for the two easter eggs within the project

- Brayden [Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53786010)
	- I worked on  Image maps [here](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/50954ea9ae2594d6aa3cf8ec3cac23e95bf3c855/views/easter_egg/templates/easter_egg/home.html#L26) so that the person selecting the location can better see where they are picking their food.

#### Week 6

- [implemented DOM to allow for preview of form editing](http://timetothrift.cf/database_form)
	- [link to code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/e2775f155fb96bf5845f93b70c25a9c17dbe5707/templates/database_form.html#L128-L158) implemented listener to allow for the card to be populated with what the user entered into the form fields
- [easter egg link](http://timetothrift.cf/easter_egg)

Tickets for week 7:
- [Colin Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53784984)
- [Andrew Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53785119)
- [Sam Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53785634)
- [Brayden Ticket](https://github.com/orgs/P5-Tacos/projects/1#card-53786010)

#### Week 5 

Implemented API as WOW factor

#### Week 4

Scrum Master Overview  (17/20): The team created progress in the C and D aspects of  CRUD [databases](https://github.com/orgs/P5-Tacos/projects/1#card-52179958). The team has also been able to practice [usage of jinja in storefront application](https://github.com/orgs/P5-Tacos/projects/1#card-52847756) and [usage of jinja in displaying stock](https://github.com/orgs/P5-Tacos/projects/1#card-52772529). [Link to the live website](http://timetothrift.cf/). Please see instructions down below to understand the testing for each contribution as well as the corresponding code. The team has yet to implement the provided JS error handling into the forms or yet to get an API key to more efficiently input more values into the code. However we were able to make good progress where we did

Sam: [link to ticket](https://github.com/orgs/P5-Tacos/projects/1#card-52847756) **procedure of running code** clicking the name of each store redirects the user to the corresponding gallery of what is in stock in the store, the location redirects user to google maps
- [link to tangible on website](http://timetothrift.cf/storefront)
	- [Link to CSS + Jinja - front end](https://github.com/P5-Tacos/P5-Tacos-thrift-store/edit/main/templates/storefront.html)
	- [Link to storing the data -backend](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/websitecards.py)

Andrew: [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52179958)
- completed Database [see it on the live site](http://timetothrift.cf/database)
	- **procedure on how to test it:** Navigate to the database tab, can enter in values for fields, be sure to enter in string, string, float, no error handling implemented
		- Database Initialization: Completed. The database is fully functional and currently stores 60 + test items. Also started trying to implement Filefield of Flask-WTF (error handling is work in progress)
			- [see the code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/216c69ab1f7143c00dce36adf9464aeb3d3eb1d3/app.py#L84-L95)
		- Data visualization: Completed. Use a list to append all the data from the database and display it through the HTML table. The loop outside displays all the items, the dictionary inside helps display new data appended to the database. 

Colin: [ticket link - collaborated with Andrew](https://github.com/orgs/P5-Tacos/projects/1#card-52179958)
- contributed Delete of CRUD see it on the [live site](http://timetothrift.cf/database)
	- **Guide on how to use:** click the remove button on the right column to delete the items within the database,**do not edit the values within the number fields** these numbers correspond to the id of the item, have not figured out a way to automatically assign a value in a form when there was no user input. The row containing the information about that item will disappear off the page		
		- see the code of displaying the delete buttons [front end](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/216c69ab1f7143c00dce36adf9464aeb3d3eb1d3/templates/Database%20test.html#L82)
			- we are getting the id of the selection, in this case there are auto filled number fields,have not figured out away to automatically assign a value in a form when there was no user input, we then select the submit button to route the input into the backend
		- see the code of deleting [back end of the deletion](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/216c69ab1f7143c00dce36adf9464aeb3d3eb1d3/app.py#L98-L130)
			- we receive the values submitted by the user selecting the delete button, we first delete the row in the database that corresponds with the item ID that the user selected, we then delete the dictionary within the list that the user sees (this list is iterated through in the front end using jinja to display all of the values in a table)

Brayden:
- further templated out what the site should look like, a stand alone MVP to be show to individual stores[here](https://docs.google.com/presentation/d/1xVco3WgpxcF6dC8JizWmhM1jISvFez5Wo6U4juvPNSQ/edit?usp=sharing) 
	- see [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52868251)
- [Completed Email](https://docs.google.com/document/d/1aYkOOmSYxCDvK-U_GJuIXZrs0-8BRxPiIlRUJOzCSfM/edit?usp=sharing) The Thrift shops do not have an email but I am planning on calling them when we have the appropriate code and asking for their email address. 	
	- see [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52397885)
- Proving knowledge of Jinja through preview of all items in stock on the home page **Procedure of testing code** hover over each card 
	- see card [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52772529)
	- see the [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/35b21300c67817de0f51292b0db6db9e7778f1f5/templates/home.html#L33-L45)
	- see it on the [live website](http://timetothrift.cf/)

Week 3
- programed a web scraper to download all items with image tags into a specific directories
	- see the [scraper](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/env/image_downloader.py)
	- see the [images downloaded](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/env/static/images/barbarella)
- preliminary page of more clothing info, we look forward to include more information on this page, specifically embedding maps location of the storefronts for pickup
	- see [clothing info prototype](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/7b7269c4d1317a555dcb01238eb1e851054e0d0a/env/templates/clothes_info.html#L1-L52)
	
Week 2
- began on protype on the webpage
	- will use the webpage to ideate what the storyboard will be like (see what works and what doesn't)
- completed preliminary prototype of customer UI 
	- see the [gallery](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/2d13dcbbebd1e39eaefef786d938f3d0cbb0779a/env/templates/gallery.html#L1-L59) 
- preliminary designs of Data collection
	- see [database test](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/2d13dcbbebd1e39eaefef786d938f3d0cbb0779a/env/templates/Database%20test.html#L1-L22) 

Week 1
- completed the project plan/schedule
- started to look into implementation of database by deploying Nighthawk Coding Society page onto pi

Week 0 
- created readme
- created scrum board
- creating preliminary issues (assignments)

#### Resources used 
- [How to Scrape and Download ALL images from a webpage with Python](https://www.youtube.com/watch?v=stIxEKR7o-c)
- [images for products](https://www.etsy.com/market/vintage_t_shirt)

### Summary
Thrift store inventory and sale system. Creating a web based storefront for users to see what hot stock(top 50 items per week) is within the store and potentially purchase items from the thrift shop.

The website application would need to differentiate between user and employee. The user could use the site to browse the items available without purchasing them online. The user would have to sign in with their personal information to purchase items online. The employee would sign into the website to identify what items need to be picked out to ship off to the customer as well as an interface to upload images to corresponding identifying numbers.

# Ideation 
Here were the initial ideas for the project. see in depth big ticket items description here: https://docs.google.com/document/d/1KfMvlYYCx5RgCIgN95gB9F38R15c6u2dG-cIQ-A9-oY/edit

### Database implementation

Store information of username and password

users
- Store recent purchases of users
- suggested items based off recent purchases
- suggested thrift shop based off recent purchases

employee/admin
- Store items in stock that have been uploaded to show in the store front
- show per store visualization of when are the most active times

Different stores could register within the website, this would introduce an additional landing page where customers can select which store they want to browse through

  
### Dynamic Website

Take a dictionary of (query database for information of)

-   Image of product
-   Name of product
-   Unique id
-   Store
    
From the dictionary of information of each product, the website would populate cards on a screen to display to the user what items are available at the thrift store

### Data Gathering

To replace the arduous task of manually going out to a thrift store to take photos and id each clothing item, we would temporarily query the web for stock images of clothing pieces as a placeholder to fill in the database containing the stock of each store

### Things to expand to

- Using tensor flow to automatically crop images of clothing for a consistent look
- Passing information through json files to integrate app solutions for the data gathering process
- Creating a relationship with local thrift stores to implement the website with their product


#### when downloading need to execute:
```pip install -r requirements.txt```

#### Structure of code
- Databases
	- [Users Time to Thrift](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/UsersTT.db)
	- [Items in Database Time to Thrift](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/UsersTT.db)
	- [Archived items in database](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/env/items.sqlite3)
- Models
	- [Models for Time to Thrift](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/models)
		- here we have stored the python files which contains the information which populates the pages within the time to thrift store
			- [info for landing cards of the stores](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/websitecards.py)
			- [images for barbarella gallery](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/barbarelladata.py)
			- [images for thrifty threads gallery](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/thriftythreadsdata.py)
- Views
	- [app.py](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/app.py)
		- contains the CRUD logic to manage user login and the shopping cart which is tied to the Time to Thrift webpage. this logic is intertwined with the routes that enable the user to navigate around the home page. 
- Blue Prints 
	- we have many projects within the same repository, this was to provide a single location for our teacher to access all of our code and to keep track of student participation through monitoring our commits to the project 
		- we use blueprints to organize all of the files for each large section of the code [here](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views)
			- [database](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/database_items)
				- this folder contains the CRUD backend which helps supports the database page in the website. This was the first proof of concept of CRUD in the repo
			- [Del Norte Eats](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/easter_egg)
				- our second largest project on the repository, the blueprint contains its own model view control, we are working on paring it with an independent database to what we are currently using for time to thrift 	 
			- [College Board Journal](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/easter_egg_college)
				- mainly contains specialized front end focused templates to address college board specific requirements 	
			- [Demonstration of API](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/makeup_api)
				- this location contains the front end of pulling from the api of choice

#### [Refrencing Class Guide](https://github.com/nighthawkcoders/flask-idea-homesite)
#### Pull code from Github and update packages
#### In console/terminal (every update: pull code and check package dependencies)...

```pi@raspberrypi:~ $ sudo apt update; sudo apt upgrade```

```pi@raspberrypi:~ $ cd ~/P5-Tacos-thrift-store```

```pi@raspberrypi:~/P5-Tacos-thrift-store $ git pull```

```pi@raspberrypi:~/P5-Tacos-thrift-store $ source homesite/bin/activate```

In console/terminal with virtualenv activitate (every time: check and update packages)...

```(homesite) pi@raspberrypi:~/P5-Tacos-thrift-store $ sudo pip install -r requirements.txt```

In console/terminal (every time AFTER initial setup: restart gunicorn)...

```pi@raspberrypi:~ $ sudo systemctl restart homesite.service```
