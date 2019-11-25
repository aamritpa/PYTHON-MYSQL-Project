#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pyodbc
import pandas as pd
import sys
import datetime
import tkinter as tk
connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=cypress.csil.sfu.ca;Trusted_Connection=yes;',autocommit=True)
cursor = connection.cursor()


# In[147]:


print("PLEASE DONT USE ANY CAPITAL ALPHABET IN INPUT COMMANDS. THANKS\n")
print('Search Started\n')
filter_or_not= input("Do you want to filter the search: yes/no:\n")

if filter_or_not==('yes'):
    
    terminate=1
    while terminate==1:
        print('For min and max price Enter - a\n')
        print('For number of bedrooms Enter- b\n')
        print('For StartDate and EndDate Enter- c\n')
        print('For min and max and number of bedrooms Enter- ab\n')
        print('For min and max and Dates- ac\n')
        print('For number of bedrooms and Dates Enter- bc\n')
        print('For all filters Enter- abc\n')
        command= input('Please Enter From these types\n')
    
    
        
        if command=='a':
            minimum= int(input('Please enter minimum price\n'))
            maximum= int(input('Please enter maximum price\n'))
            query="SELECT DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price e FROM Listings,Calendar WHERE Calendar.price>=? and Calendar.price<=? and Listings.id =Calendar.listing_id"
            cursor.execute(query,minimum,maximum)
   
        if command=='b':
            noOfBedrooms= int(input("Please Enter Number of Bedrooms:\n"))
            query="Select DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price  FROM Listings,Calendar WHERE number_of_bedrooms=? and Listings.id=Calendar.listing_id"
            cursor.execute(query,noOfBedrooms)
        
        if command=='c':
            startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
            endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
            query="Select DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price  FROM Listings,Calendar WHERE Calendar.date>=? and Calendar.date<? and Listings.id=Calendar.listing_id"
            cursor.execute(query,startDate,endDate)
        
        if command=='ab':
            minimum= int(input('Please enter minimum price\n'))
            maximum= int(input('Please enter maximum price\n'))
            noOfBedrooms= int(input('Please Enter Number of Bedrooms:\n'))
            query="Select DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price  FROM Listings,Calendar WHERE Calendar.price>=? and Calendar.price<=? and number_of_bedrooms=? and Listings.id = Calendar.listing_id "
            cursor.execute(query,minimum,maximum,noOfBedrooms)
        
        if command=='ac':
            minimum= int(input('Please enter minimum price\n'))
            maximum= int(input('Please enter maximum price\n'))
            startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
            endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
            query="Select DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price e FROM Listings,Calendar WHERE Calendar.price>=? and Calendar.price<=? and Calendar.date>=? and Calendar.date<? and Calendar.listing_id =Listings.id"
            cursor.execute(query,minimum,maximum,startDate,endDate)                          
    
        if command=='bc':
            noOfBedrooms= int(input("Please Enter Number of Bedrooms:\n"))
            startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
            endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
            query="Select DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price  FROM Listings,Calendar WHERE Calendar.date>=? and Calendar.date<? and number_of_bedrooms=? and Calendar.listing_id =Listings.id"
            cursor.execute(query,startDate,endDate,noOfBedrooms)
    
        if command =='abc':
            minimum= int(input('Please enter minimum price\n'))
            maximum= int(input('Please enter maximum price\n'))
            noOfBedrooms= int(input("Please Enter Number of Bedrooms:\n"))
            startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
            endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
            query="Select DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price  FROM Listings,Calendar WHERE Calendar.price>=? and Calendar.price<=? and Calendar.date>=? and Calendar.date<? and number_of_bedrooms=? and Calendar.listing_id =Listings.id"
            cursor.execute(query,minimum,maximum,startDate,endDate,noOfBedrooms)
        
        if command !='a' and command !='b'  and command !='c'  and command !='ab'  and command !='bc'  and command !='ac'  and command !='abc':
            print('Wrong input\n')
            terminate=1
        else:
            terminate=0
        
if filter_or_not==('no'):
    sql_select_Query= "Select DISTINCT Listings.id,name, number_of_bedrooms, SUBSTRING(description,1,25), price From Listings,Calendar WHERE Listings.id=Calendar.listing_id"
    cursor.execute(sql_select_Query)
    
records = cursor.fetchall()
    
if len(records) == 0:
        print("\nERROR! WITH THE ABOVE DETAILS NO DATA IS FOUND:\n")        
else:
    for row in records:
        print("Id = ", row[0])
        print("Name = ", row[1])
        print("No. of bedrooms  = ", row[2])
        print("description  = ", row[3])
        print("price  = ", row[4], "\n")
  

    if len(records)!=0:
        to_book= int(input('TO Do Bookings Please Enter The Listing ID From The Searched Lisitngs ID\n'))
        input_name=input('Please Enter your name\n')
        BookstartDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
        BookendDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
        guests= int(input("Please enter number of guests\n"))
        SQLCommand = ("""INSERT INTO Bookings(id,listing_id,guest_name,stay_from,stay_to,number_of_guests) VALUES (?,?,?,?,?,?)""")  
        cursor.execute("Select MAX(id) AS max,Count(id) AS count FROM Bookings ")
        record=cursor.fetchall()
 
        if record[0][1]==0:
            value=1
        elif record[0][1]==1:
            value=2
        else:
            value= int(record[0][0])+1

        VALUES = [value,to_book,input_name,BookstartDate,BookendDate,guests]  
        
        cursor.execute(SQLCommand,VALUES) 
        print('Booking Updated\n')
        print('Calendar updated Through Trigger\n')

        
review_or_not= input('Do you want to Add a Reviews Enter -yes/no \n')

if review_or_not=='no':
    print('Ended\n')
    print('To Search, book, and review Please run programme again\n')
else:
    entered_name= input('Please Enter your name\n')
    query= "Select * From Bookings Where guest_name=?"
    cursor.execute(query,entered_name)
    record= cursor.fetchall()

    if len(record)==0:
        print('Noting Found')
    else:
        for i in record:
            print('id',i[0])
            print('listing_id',i[1])
            print('guest_name',i[2])
            print('stay_from',i[3])
            print('stay_to',i[4])
            print('number_of_guests',i[5])
        print('\n')    
        listing_id=int(input('Please enter listing_id\n'))
        name_entered=input('Please enter your name\n')
        date_entered=input('please enter current date\n')
        review_entered=input('Please enter review text\n')

        cursor.execute("Select MAX(id) AS max,Count(id) AS count FROM Reviews ")
        record=cursor.fetchall()
 
        if record[0][1]==0:
            value=1
        elif record[0][1]==1:
            value=2
        else:
            value= int(record[0][0])+1

        query="Insert Into Reviews(id,listing_id,comments,guest_name) Values(?,?,?,?)"
        review_values=[value,listing_id,review_entered,name_entered]
        cursor.execute(query,review_values)

connection.commit()
connection.close()


# In[ ]:





# In[3]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:





# In[ ]:





# 
