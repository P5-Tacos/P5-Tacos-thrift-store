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

## Changes Log
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

