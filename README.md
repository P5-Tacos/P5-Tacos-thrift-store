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
#### [Link to scrum board](https://github.com/orgs/P5-Tacos/projects/1)
#### [Link to project plan and requirements](https://docs.google.com/document/d/1KfMvlYYCx5RgCIgN95gB9F38R15c6u2dG-cIQ-A9-oY/edit)
#### [Link to easter egg](http://timetothrift.cf/easter_egg_college/)
#### [Link to commercial](https://www.youtube.com/watch?v=4RPEFKNqaKE)

## Overview (description)
- **Time to Thrift** Thrift store inventory and sale system. A web based storefront for users to see what hot items are within local San Diego thrift shops.
- **Del Norte Eats** A lunch ordering system and delivery system centered around the menus and building geography of Del Norte High School.

## Structure of the Website (front end)

These bullets highlight the structure of the templates (front end) of the website and what each page's function is. The inclusion of this section is to demonstrate the scale of the website. WOW items to check out are denoted by both being ***bold and italicized***. Be sure to check out our [wow section](https://github.com/P5-Tacos/P5-Tacos-thrift-store#wow) down below for more indepth explinations of each wow. ['jhon','password'] represents the username and password (many passwords are the string: 'passwords') that will need to be typed in at each login.

- [Landing page](http://delnorteeats.cf/) landing page to navigate throughout each of the 3 main sections. Notice the css on hover. Need to improve css for mobile users and assesibility guidelines
	- [Time to Thrift](http://delnorteeats.cf/time_to_thrift/) - First project landing page
		- [home page:](http://delnorteeats.cf/time_to_thrift/) (Brayden) displays all items within the system
			- clothes info: (Sam) the page after clicking on the item photos on the home page (accessible by clicking the images on the homepage) will redirect user to the shopping cart (guest dashboard)
		- [storefront:](http://delnorteeats.cf/time_to_thrift/storefront) (Sam) navigation to the gallery for each store
			- [gallery view (Thrifty Threads)](http://delnorteeats.cf/time_to_thrift/thriftythreads): (Sam) view of all items within thrifty threads data. Click 'add to cart' button to add item to shopping cart
			- [gallery view (Barbarella):](http://delnorteeats.cf/time_to_thrift/barbarella) (Sam) view of all items within Barbarella data. Click 'add to cart' button to add item to shopping cart
		- ***[Make Up](http://delnorteeats.cf/makeup_api/makeup_landing)*** (Colin) the first use of API, select any of the brands and press submit.[implementation of selecting different apis based on user input](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/28c3cfa85735787f37a18a34994a0129774a9040/views/makeup_api/view.py#L18-L20) We use [iteration](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/28c3cfa85735787f37a18a34994a0129774a9040/views/makeup_api/view.py#L42-L58) to pull out all and label all of the necessary information out of the Json file from the api
		- [reaction test:](http://delnorteeats.cf/time_to_thrift/reactiontest) (Brayden) fun game to burn time
		- [login:](http://delnorteeats.cf/time_to_thrift/login) (Andrew) Reading the userDN database to verify user input
		- [sign up:](http://delnorteeats.cf/time_to_thrift/signup) (Andrew)  Creating users in userDN and userTT table (notice the dropdown selector of which user type one can sign up as)
		- [dashboard (shopping cart):](http://delnorteeats.cf/time_to_thrift/logged_in) (Colin)  page for user to see what contents was saved to their cart. Shows the quanity in shopping cart
			- [guest:](http://delnorteeats.cf/time_to_thrift/logged_in) (Colin) a variation to manage those who have not logged in (default not logged out)
			- [user:](http://delnorteeats.cf/time_to_thrift/logged_in) (Colin) U D of CRUD of shopping cart - saves information of (signed in as ['jill', password])
				- clicking the 'save shopping list' will U (update) the items table of the database
				- clicking the 'load shopping list' will R (read) the items table of the database and map the contents into a viewable front end from the user perspective
			- [admin:](http://delnorteeats.cf/time_to_thrift/logged_in) (Andrew) a variation of the dashboard when logged in (when logged in as ['KetherBuG','12345678'], ['billy','password'], ['bob','password'], ['brayden','password'])
			  - [database:](http://delnorteeats.cf/database_items/testing_action) (Andrew) our first implementation of C and D of CRUD for the items table within the database (need to add in logic to only allow access when logged in as admin)
				- be sure to click the show gallery view to toggle with js the display of the contents of the database in a table view to a cards view
				- feel free to add in an item within the databse with the feilds at the top of the page
		- ***[admin page:](http://delnorteeats.cf/time_to_thrift/admin)*** (Colin) see the contents of the databases involved in the Time to Thrift page (hover over the asterics to see a <span><a style="color:red" href="https://github.com/P5-Tacos/P5-Tacos-thrift-store#front-end-viewing-data-within-databases-use-of-college-board-procedures---usign-java-script">WOW</a><span>)
	- [Del Norte Eats](http://delnorteeats.cf/easter_egg/) - Project team pivoted. Heavy use of Javascript and Databases
		- [User:](http://delnorteeats.cf/easter_egg/user_dashboard) (Colin) Landing page when navigating to Del norte eats
			- ***[login:](http://delnorteeats.cf/easter_egg/login)*** (Colin) Reading in userDN and userEE table (verify user input). See to see the code and read the <a href="https://github.com/P5-Tacos/P5-Tacos-thrift-store#back-end-login-management" style="color:red"> WOW </a> procedure. Sign in as ['jhon','password'] to see the progress of delivery on your items
			- [sign up:](http://delnorteeats.cf/easter_egg/signup) (Colin) Creating users in userDN and userEE table. See [below](https://github.com/P5-Tacos/P5-Tacos-thrift-store#signin-logic-c-part-of-crud) (Colin) to see the code and read logic and see future improvements
			- [dashboard:](http://delnorteeats.cf/easter_egg/user_dashboard) (Colin) Reading information that correspond to the username
			- ***[order food:](http://delnorteeats.cf/easter_egg/singlepage_form)*** (colin+Sam) Creating information in the ordersEE table [jinja+javascript](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/172d11c15206f2fb1b1b13b71db913c39a5d71f5/views/easter_egg/templates/easter_egg/singlepage_form.html#L49-L65) usage to differentiate between different items selected
		- [Runner](http://delnorteeats.cf/easter_egg/port_runner) (Colin) redirect from the user to runner page, logs out user
			- [login:](http://delnorteeats.cf/easter_egg/port_runner) (Colin) required login for all Del Norte Eats Runners
			- sign up: (need to be implemented) creating users in userDN and userRR. Sign in as ['bobby','password']
			- ***[dashboard:](http://delnorteeats.cf/easter_egg/runner_dashboard)*** (Colin) (need to be locked behind login required)updating information in the ordersEE table. [WOW](https://github.com/P5-Tacos/P5-Tacos-thrift-store#runner-dashboard-colins-contributions-runtime) down below
		- [admin page:](http://delnorteeats.cf/easter_egg/admin) (Colin) see the contents of the databases involved in the Del Norte Eats 
	- [Easter Egg](http://delnorteeats.cf/easter_egg_college/) - the section of code which contains CS P specific assignments
		- [Requirements- Thrift Shop:](http://delnorteeats.cf/easter_egg_college/college_board_requirements) (everyone) Initial description how our project (only Time to Thrift at the time) satisfied college board requirements
		- [Who am I?:](http://delnorteeats.cf/easter_egg_college/who_am_i) (everyone) Descriptions of capabilities of each teammate in P5-Tacos
		- [AP CSP requirement reflections:](http://delnorteeats.cf/easter_egg_college/AP_CSP_Requirements) (everyone) Second reflection and planning document on how the team would work towards satisfying college board requirements

## Technicals (Blue Prints/Back End)

- Models (backend)
	- [Models for Time to Thrift](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/models)
		- here we have stored the python files which contains the information which populates the pages within the time to thrift store
		- Include pages containing the initialization of the tables within the databases, where all the front end code refer to and retain information from.
		- These information are stored in forms of dictionaries or databases.
			- [info for landing cards of the stores](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/websitecards.py)
			- [Info for user management for time to thrift and del norte eats](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/module.py)
			- [images for barbarella gallery](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/barbarelladata.py)
			- [images for thrifty threads gallery](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/thriftythreadsdata.py)
			- [Logic for reaction test](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/reactiontestcode.py)
- Views (front end)
	- [app.py](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/__init__.py)
		- contains all the routes for all of the blueprints
- Blue Prints
	- we have many projects within the same repository, this was to provide a single location for our teacher to access all of our code and to keep track of student participation through monitoring our commits to the project
		- we use blueprints to organize all of the files for each large section of the code [here](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views)
			- [Database](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/database_items)
				- This folder contains the CRUD backend which helps support the database page in the website. This was the first proof of concept of CRUD in the repo
			- [Del Norte Eats](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/easter_egg)
				- our second largest project on the repository, the blueprint contains its own model view control.
			- [College Board Journal](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/easter_egg_college)
				- mainly contains specialized front end focused templates to address college board specific requirements
			- [Demonstration of API](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/makeup_api)
				- this location contains the front end of pulling from the api of choice
			- [Time to thrift](https://github.com/P5-Tacos/P5-Tacos-thrift-store/tree/main/views/time_to_thrift)
				- This location contains all of the front end of the time to thrift. This allows the team to section off the front end and the views of the of the time to thrift


## Wow 
### Login Management (Use of Databases) (Colin's Contributions)

As there are multiple systems embedded in the same project it was important for the team to organize all user information in separate table for each system

- [module.py](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/main/models/module.py) contains all of the database's setup. This file was created to allow for tracking of users across multiple projects.
- [userDN](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L45-L58) contains all of the users. The contents of the database can be found [here](http://delnorteeats.cf/easter_egg/admin) in the admin page of Del Norte Eats.
- [userEE](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L78-L88) is represented by “Users Del Norte Eats” [table](http://delnorteeats.cf/easter_egg/admin)
- [userRR](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L90-L100) is represented by “Runners Del Norte Eats” [table](http://delnorteeats.cf/easter_egg/admin)
- [orderEE](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L60-L76) is represented by “Orders” [table](http://delnorteeats.cf/easter_egg/admin)

[userTT](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/models/module.py#L15-L30) is represented in the Admin page in Time to Thrift [table](http://delnorteeats.cf/time_to_thrift/admin)
Highlights of the admin pages is that the passwords are represented by asterisks for each character in the table. On hover the asterisks are replaced with the actual characters of the password. [Here is the front end of the logic](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L50-L56)

### Front end Viewing data within Databases (Use of College Board Procedures - Using Java Script) (Colin's Contributions)

Highlights of the admin pages is that the passwords are represented by asterisks for each character in the table. On hover the asterisks are replaced with the actual characters of the password. [Here is the front end of the logic](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L50-L56) on hover for the cell, there is a javascript function called.

[There are javascript procedures (using college board diction)](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L149-L171) the arguments that are passed in are the variable iteration of the loop (which row in the table are in), and the prefix of each of the id tags. The prefixes correspond to the ids of the character representation then the actual password. The arguments are [concatenated](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L151) together to then [determine which row](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L153) was hovered over and then changes the css to display the actual characters rather than the representation of the password.

(Where the procedures are used) Using procedures was beneficial as the function can be used over and over for all of the tables as there are just different arguments passed to differentiate between rows of each table.
- [userDN](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L50)
- [userEE](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L79)
- [userRR](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/admin_page.html#L107)

#### Back End Login Management (Colin's Contributions)
Here is the bulk of the [login logic](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L123-L186)
This login logic only covers the login for the users of Del Norte eats and the Runners of Del Norte eats

###### line by line of the login logic
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L128) differentiates which login template was used
	- [front end code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/172d11c15206f2fb1b1b13b71db913c39a5d71f5/views/easter_egg/templates/easter_egg/login.html#L64) either the user (customer) login 
	- [front end code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/172d11c15206f2fb1b1b13b71db913c39a5d71f5/views/easter_egg/templates/easter_egg/runner/login_runner.html#L64) or the runner login 
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L133) storing the user input in a list format
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L142-L147) itterates through the userDN (the umbrella database) and stores all the information in a list of dictonaries (similar to JSON formatting)
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L150-L154) if the program stored with the user in userDN corresponds with the form program, append the information into a list for later refrence. This is a list of lists, the first value is the username, second value is the password. This line can be replaced with more effective validators as storing passwords as strings currently is super insecure
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L156-L159) Itterates through the list that conatins all the users which correspond to the program. Checks to see if the user input username and password correspond with username and passwords stored in the system 
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L167-L171) if the program was 'del_norte_eats_runner' then redirect the user to the runner homepage
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L173-L177) if the program was not 'del_norte_eats_runner' but was 'del_norte_eats' the redirect to the user homepage
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L178-L180) if the program was not 'del_norte_eats_runner' and was not 'del_norte_eats' the redirect to error page which will then redirect the user back to the login

###### signup logic (C part of CRUD) (Colin's Contributions)
- [Sign up as a user (code)](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L193-L217) (someone who orders food at DN)
	- Connected to this [sign up page (code)](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/SU.html#L61)
- [Sign up as a runner (code)](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L219-L243) (someone who delivers food at DN )
	- Connected to this [sign up page (code)](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/runner/SU.html#L61)
	
[Here](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/templates/easter_egg/SU.html#L70) is a feature to expand onto where the signup page would be differentiated by a hidden input and only reference one sign up manager.
- This input would differentiate what databases that the data would be uploaded in
	- Current each function is tied each [database](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/b3a01738d759423fb11f9530b7bd88ba6266c19a/views/easter_egg/view.py#L230-L238)
	- Users are uploaded to two databases simultaneously to keep track of them in userDN and either userTT, userEE, or userRR for time to thrift, user of Del Norte Eats, or runner of Del Norte Eats respectively
	
#### Runner Dashboard (Colin's Contributions) [runtime](http://delnorteeats.cf/easter_egg/runner_dashboard) (College Board requirements use of lists)
- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/c45e9bb54cdff3f11c4e26442d6f63190e761276/views/easter_egg/templates/easter_egg/runner/runner_dashboard.html#L52-L65) if the input is [default]((https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/c45e9bb54cdff3f11c4e26442d6f63190e761276/views/easter_egg/view.py#L331-L339)) the input for the time, picked_up, delivered are all equal to one another as default. 
  - When the runner ***updates*** 
	- [front end button](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/templates/easter_egg/runner/runner_dashboard.html#L68-L95)
		- contains hidden [input](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/templates/easter_egg/runner/runner_dashboard.html#L69) of 'order_id' to communicate for which row did the form correspond to
	- [backend picked up](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/view.py#L461-L472) updates the picked up value within row with the current time (not default configuration anymore therefore the front end will display yes) redirects to the 'runner_dashboard' function (see below for logic)
	- [backend delivered](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/view.py#L476-L487) updates the delivered value within row with the current time (not default configuration anymore therefore the front end will display yes) redirects to the 'runner_dashboard' function (see below for logic)
	- ***runner_dashboard function*** (line by line)
		- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/view.py#L355) querying the orderEE table
		- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/view.py#L358-L365) checking to see if the value within picked_up column is default, if not append 1 to button_logic_pickup if not append 0 (using data abstracting to representing the state of each step in the delivery proccess)
		- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/view.py#L366-L377) checking to see if the value within delivered column is default, if not append 1 to button_logic_delivered and defined total_time variable as current time (time when delivered button was selected) if not append 0
		- [code](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/view.py#L386-L388) passing in the values of the database values into the template with the information of button_logic_pickup, button_logic_delivered, total_time
			- (conceptual) say if we had 5 items within the orderEE table, all of them had been picked up then the list button_logic_pickup would read [1,1,1,1,1] yet if only 3 were delivered the list button_logic_delivered would read [1,0,0,1,1] . These lists can be interpreted that the orders of row 1, 3,5 have been totally completed and orders of row 2 and 3 have not yet been delivered
	- [code frontend](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/templates/easter_egg/runner/runner_dashboard.html#L67) jinja if statements read the values in the list and based off of that information display the picked up? button or delivered? or not show any 
	- [code frontend](https://github.com/P5-Tacos/P5-Tacos-thrift-store/blob/3fbe9efccde72aae2b3918b5e8ed176b3844a111/views/easter_egg/templates/easter_egg/runner/runner_dashboard.html#L99-L101) if the order has been delivered then display the time it took from user placing the order to delivering the order
	

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
