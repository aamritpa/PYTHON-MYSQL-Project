# PYTHON-MYSQL-Project Assignment7
Using Python and SQL to retrieve AIRBNB data from Cypress Server(Simon Fraser University).

INSTRUCTIONS:
BASIC REQUIREMENTS:
1) Python 3.00+
2) Libraries- pyodbc
3) Cypress Database Connection[CSIL MACHINE REQUIRED TO RUN THIS CODE]

Runnning the Code:-
1)Debug the Assignment7.py file in Virtual Studio Code or any other Editor. 
2)Do not Use any Capital Alphabets in the inputs.

-For Search and Bookings
(1) Enter 'a'
(2) For Filter -'yes/no'-[Make sure the input enter is either 'yes' or 'no']
(3) If Entered 'no' then all listings will be displayed
(4) If Entered 'yes' then 4 Types of Filters will be displayed:

[IF YOU CHOOSE A FILTER THEN YOU CANNOT LEAVE EMPTY INPUTS. SO CHOOSE YOUR FILTER WISELY],[YOU MUST ENTER DATE IN EACH FILTER]
  Filter 1- Start date,End date 
  Filter 2- Minimum price,Maximum price,Start date,End date
  Filter 3- Number of Bedrooms,Start Date,End Date 
  Filter 4- Minimum price,Maximum Price,Number of Bedrooms,Start Date, End Date.
ALL Listings will be displayed with filters. If No data found the 'Error' wiil be displayed. 

-For Reviews
(1) Enter 'b'
(2) Enter 'name'
(3) All bookings will be displayed with that name. If No data found the 'Error' wiil be displayed. 

-To Terminate Program
(1) Enter '0'


Trigger Terminating Program-
If the Review Entered without having Bookings then trigger message will be displayed and program will Terminate.
If the Review Entered before the stay_to date the trigger message will be displayed and program will Terminate.




