# P5-Tacos-thrift-store

|Name|	Github   | |
|--|--|--|
|Colin Szeto  |  kolinbilly| Pair 1|
|Samuel Mahjouri  | iBraskyy | Pair 1|
| Andrew Zhang | Ketherbug | Pair 2|
|Brayden Basinger  |  BraydenBasinger| Pair 2|

#### Link to scrum board: https://github.com/orgs/P5-Tacos/projects/1
#### Link to project plan and requirements: https://docs.google.com/document/d/1KfMvlYYCx5RgCIgN95gB9F38R15c6u2dG-cIQ-A9-oY/edit

## Changes Log

Week 1
- completed the project plan/schedule
- started to look into implmentation of database by deploying Nighthawk Coding Society page onto pi

Week 0 
- created readme
- created scrumboard
- creating preliminary issues (assignments)

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
