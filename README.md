# SCRUMPTON Hotel Reservation System

SCRUMPTON Hotel is a final team project for CPSC 362, Software Engineering Foundations class @CSUF, Summer 24.<br> 




## Software Description

<b> Front-End: </b> <br>
Reservation System consists of multiple web pages. Different web pages allows Scrumpton Hotel guests to view hotel amenities, sign-up, log-in, view and create reservations. Scrumpton Hotel managers are able to use the same log-in page to gain access to an overview of all guest reservations and the ability  to cancel a guest’s reservation. A combination of HTML, CSS and JavaScript is used to create an easy to use UI.

<b> Back-End: </b> <br>
We used Python for the back end of our Reservation System web pages. We have a class that stores and edits our Hotel Room data, a class that stores and edits Guest data and a class that helps calculate the cost of a guest’s reservation.



## Code Layout
<b>Front-End</b>
“static” folder
“images” folder
Stores all images used on our website
activity.css
UI layout specifications for “activity.html”
calendar_payment.css
UI layout specifications for “calendar_payment.html”
 calendar_payments.js
Updates image on “calendar_payment.html” to correct example room based on user input
reservations.css
UI layout specifications for “reservations.html”
scripts.js
Toggles visibility of Sign-up/Sign-in Button
styles.css
UI layout specifications for top and bottom bars along all web pages
thankyou_page.css
UI layout specifications for “thankyou_page.html”
“templates” folder
activity.html
Web page depicting Scrumpton Hotel activities
Each different amenity has its own section with a brief description and photos
calendar_payment.html
Web page allowing guests to enter in reservation details
When a guest selects the room they would like to reserve, the photo on the right of the data entry updates to show an example room of the guest’s selection
Once reservation details are submitted will bring up payment form
Once guests complete payment they will be redirected to “thankyou_page.html”
home_page.html
Web page where guests may login or signup
Sign up button will pull up small window where guests may enter in their information to create an account
Login button will pull up small window for users to enter their account email and password
Mangers may login
manager.html
Lists all Hotel Reservations
Manager may delete a guest’s reservation
reservations.html
Lists details of all of a guest’s reservations
Button to return New Reservation page on “calendar_payment.html”
thankyou_page.html
Thanks guest for completing reservation
Button to view reservations on “reservations.html”
	<b>Back-End</b>
app.py
Links HTML and Python
Date_calculations_class.py
Calculates the total cost for a reservation (based on room size, number of guests, and number of days reserved) and ensures the reservation length is between 1 and 30 days
Functions:
room_cost_calculator()
Returns cost
no_overlap()
Checks if start and end date are valid
Guests_Class.py
Stores guest data (email, name, password, and reservation status) in a dictionary and keeps track of who is currently logged in.
Functions: 
add_user()
Adds new guest to dictionary on sign UP
sign_in()
Will check if user is Guest or Manager on sign IN
has_reservation()
Checks if guest has reservation
log_out()
Can reset who is logged in 
Room_Class.py
Keeps track of data for each hotel room (room number, size, price, check-in and check-out date, email, and reservation ID) in a 2D array and manages reservations.
Functions:
add_pending_reservation()
Adds pending room reservations while awaiting guest’s payment
add_reservation()
Secures reservations after payment is completed
get_reservations()
Returns all reservations as a list
format_reservation()
Formats a reservation when displaying in html
available_room()
Verifies room availability on given dates
delete_reservation()
Deletes room reservation from given room ID
remove_pending()
Clears pending reservation




## Conclusions and Future Work 

 #### Lessons Learned
* Not to overestimate how many functions can be included in a time-box. We had to cut out more functions from our program than anticipated.
* The importance of communicating with team members in order to complete tasks efficiently and accurately. 
* How to connect front and back ends of programs. Using different programming languages in one project was a great learning experience.
* New programming languages. Some of our members had the opportunity to learn one or more programming languages while we put together this project.

#### Software Requirement Specification (SRS) Deviations

* Guests cannot edit or cancel their reservation through our software
* Managers are still able to delete a guest’s reservation on request
* Guests cannot check in or out through our software
* Guests cannot include add-ons with their reservations.
* Guests do not receive a thank you email on completion of their reservation
* Managers cannot add on fees to guest statements

#### Future Work

* Expand our Reservation System to multiple Hotels. Currently only set up for a singular location.
* Switching Room and Guest data to an online dataset
* Allow Managers to post and edit different Hotel activities
* Have an outside tester for quality assurance
* Add in SRS deviations




<br><b>P.S.</b> The name of the hotel was inspired by the term 'Scrum', an agile project management framework that helps teams structure and manage their work through a set of values, principles, and practices. 
