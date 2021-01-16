# P5-Tacos-thrift-store

|Name|	Github   | |
|--|--|--|
|Colin Szeto  |  colin-szeto| Pair 1|
|Samuel Mahjouri  | iBraskyy | Pair 1|
| Andrew Zhang | Ketherbug | Pair 2|
|Brayden Basinger  |  BraydenBasinger| Pair 2|

```diff
- \/ Link to the scrum board below \/
```
#### Link to scrum board: https://github.com/orgs/P5-Tacos/projects/1
#### Link to project plan and requirements: https://docs.google.com/document/d/1KfMvlYYCx5RgCIgN95gB9F38R15c6u2dG-cIQ-A9-oY/edit

#### when downloading need to execute:
```pip install -r requirements.txt```

## Changes Log


Week 4
Sam: [link to ticket](https://github.com/orgs/P5-Tacos/projects/1#card-52847756)
- [link to tangible on website](http://76.167.66.16/storefront)
	- [Link to CSS + Jinja - front end](https://github.com/P5-Tacos/P5-Tacos-thrift-store/edit/main/templates/storefront.html)
	- [Link to storing the data -backend](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/websitecards.py)

Andrew: [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52179958)
- completed Database [see it on the live site](http://76.167.66.16/database)
	- procedure on how to test it: Navigate to the database tab, can enter in values for fields, be sure to enter in string, string, float, no error handling implemented
		- Database Initialization: Completed. The database is fully functional and currently stored 60 + test items. Also started trying to implement Filefield of Flask-WTF (error handeling is work in progress)
			- [see the code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/216c69ab1f7143c00dce36adf9464aeb3d3eb1d3/app.py#L84-L95)
		- Data visualization: Completed. Use a list to append all the data from the database and display it through the HTML table. The loop outside displays all the items, the dictionary inside help display new data appended to the database. 

Colin: [ticket link - collaborated with Andrew](https://github.com/orgs/P5-Tacos/projects/1#card-52179958)
- contributed Delete of CRUD see it on the [live site](http://76.167.66.16/database)
	- Guide on how to use: click the remove button on the right column to delete the items within the database, 
```diff
- do not edit the values within the number fields
```

- these numbers correspond to the id of the item, have not figured out away to automatically assign a value in a form when there was no user input.		
	- see the code of displaying the delete buttons [front end](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/216c69ab1f7143c00dce36adf9464aeb3d3eb1d3/templates/Database%20test.html#L82)
- we are getting the id of the selection, in this case there are auto filled number fields,have not figured out away to automatically assign a value in a form when there was no user input, we then select the submit button to route the input into the backend
	- see the code of deleting [back end of the deletion](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/216c69ab1f7143c00dce36adf9464aeb3d3eb1d3/app.py#L98-L130)
		- we recieve the values submitted by the user slecting the delete button, we first delete the row in the data base that corresponds with the item ID that the user selected, we then delete the dictonary within the list that the user sees (this list is itterated through in the front end using jinja to display all of the valuse in a table)

Brayden:
- further templated out what the site should look like, a stand alone MVP to be show to induvidual stores[here](https://docs.google.com/presentation/d/1xVco3WgpxcF6dC8JizWmhM1jISvFez5Wo6U4juvPNSQ/edit?usp=sharing) 
	- see [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52868251)
- [Completed Email](https://docs.google.com/document/d/1aYkOOmSYxCDvK-U_GJuIXZrs0-8BRxPiIlRUJOzCSfM/edit?usp=sharing) The Thrift shops do not have an email but I am planning on calling them when we have the appropriate code and asking for their email address. 	
	- see [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52397885)
- Proving knowledge of Jinja through preview of all items in stock on the home page
	- see card [ticket link](https://github.com/orgs/P5-Tacos/projects/1#card-52772529)
	- see the [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/35b21300c67817de0f51292b0db6db9e7778f1f5/templates/home.html#L33-L45)
	- see it on the [live website](http://76.167.66.16/)

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
- started to look into implmentation of database by deploying Nighthawk Coding Society page onto pi

Week 0 
- created readme
- created scrumboard
- creating preliminary issues (assignments)

#### Resources used 
- [How to Scrape and Download ALL images from a webpage with Python](https://www.youtube.com/watch?v=stIxEKR7o-c)
- [images for products](https://www.etsy.com/market/vintage_t_shirt)

### Summary
Thrift store inventory and sale system. Creating a web based storefront for users to see what hot stock(top 50 items per week) is within the store and potentially purchase items from the thrift shop.

The website application would need to differentiate between user and employee. The user could use the site to browse the items available without purchasing them online. The user would have to sign in with their personal information to purchase items online. The employee would sign into the website to identify what items need to be picked out to ship off to the customer as well as an interface to upload images to corresponding identifying numbers.

# Ideation 
here were the intial ideas for the project. see in depth big ticket items description here: https://docs.google.com/document/d/1KfMvlYYCx5RgCIgN95gB9F38R15c6u2dG-cIQ-A9-oY/edit

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
