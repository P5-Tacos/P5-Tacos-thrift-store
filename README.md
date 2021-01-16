# P5-Tacos-thrift-store

|Name|	Github   | |
|--|--|--|
|Colin Szeto  |  colin-szeto| Pair 1|
|Samuel Mahjouri  | iBraskyy | Pair 1|
| Andrew Zhang | Ketherbug | Pair 2|
|Brayden Basinger  |  BraydenBasinger| Pair 2|

#### Link to scrum board: https://github.com/orgs/P5-Tacos/projects/1
#### Link to project plan and requirements: https://docs.google.com/document/d/1KfMvlYYCx5RgCIgN95gB9F38R15c6u2dG-cIQ-A9-oY/edit

#### when downloading need to execute:
```pip install -r requirements.txt```

## Changes Log

![ASCII UI](https://media.giphy.com/media/FQYsVKJOJkP3kWrVNc/giphy.gif)


![Game Board](images/game_screen.JPG)

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
