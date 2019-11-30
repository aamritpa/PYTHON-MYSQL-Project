#!/usr/bin/env python
# coding: utf-8

# In[12]:

import pyodbc

connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=cypress.csil.sfu.ca;Trusted_Connection=yes;',autocommit=True)
cursor = connection.cursor()

numberofBedrooms=1   # Default value for bedrooms if not Entered.
print("PLEASE DONT USE ANY CAPITAL ALPHABET IN INPUT COMMANDS. THANKS\n")
def function(value):
    print('For Search and Book-: a\n')
    print('For Review-: b \n')
    print('Terminate-: 0')
    first=input('\n')

    if first=='0':
        exit(0)

    while (first!='a' and first !='b' and first!='0' ):
        print('Wrong Entry')
        print('For Search and Book-: a\n')
        print('For Review-: b \n')
        print('Terminate-: 0')
        first=input()

    if first=='a':
        filter_or_not= input("Do you want to filter the search: yes/no:\n")

        if filter_or_not==('yes'):
            print('Please Choose Filters From Below\n')
        
            terminate=1
            while terminate==1:
                print('For StartDate and EndDate Enter- 1\n')
                print('For min and max and Dates- 2\n')
                print('For number of bedrooms and Dates Enter- 3\n')
                print('For all filters Enter- 4\n')
                command= input('Please Enter From these types\n')
            
                if command=='1':
                    startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
                    endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
                    query="SELECT DISTINCT id,name,number_of_bedrooms,SUBSTRING(description,1,25),MAX(price) FROM Listings,Calendar WHERE id=listing_id AND (date >= ? AND date <= ? )AND  id NOT IN  (SELECT listing_id FROM Calendar WHERE (date >= ?  AND date <= ?) AND (available = 0)) GROUP BY id,name,SUBSTRING(description,1,25),number_of_bedrooms"
                    cursor.execute(query,startDate,endDate,startDate,endDate)
            
                if command=='2':
                    minimum= int(input('Please enter minimum price\n'))
                    maximum= int(input('Please enter maximum price\n'))
                    startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
                    endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
                    query="SELECT DISTINCT id,name,number_of_bedrooms,SUBSTRING(description,1,25),MAX(price) FROM Listings,Calendar WHERE id=listing_id AND (date >= ? AND date <= ? )AND (price >= ? AND price <= ?) AND  id NOT IN  (SELECT listing_id FROM Calendar WHERE (date >= ? AND date <= ?) AND (price >= ? AND price <= ? AND available = 0)) GROUP BY id,name,SUBSTRING(description,1,25),number_of_bedrooms"
                    cursor.execute(query,startDate,endDate,minimum,maximum,startDate,endDate,minimum,maximum)                       
        
                if command=='3':
                    noOfBedrooms= int(input("Please Enter Number of Bedrooms:\n"))
                    startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
                    endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
                    query="SELECT DISTINCT id,name,number_of_bedrooms,LEFT(description,25),MAX(price) FROM Listings,Calendar WHERE number_of_bedrooms= ? AND id=listing_id AND (date >= ? AND date <= ? )AND  id NOT IN  (SELECT listing_id FROM Calendar WHERE (date >= ? AND date <= ?) AND available = 0) GROUP BY id,name,LEFT(description,25),number_of_bedrooms"
                    cursor.execute(query,noOfBedrooms,startDate,endDate,startDate,endDate)
        
                if command =='4':
                    minimum= int(input('Please enter minimum price\n'))
                    maximum= int(input('Please enter maximum price\n'))
                    noOfBedrooms= int(input("Please Enter Number of Bedrooms:\n"))
                    startDate = input('Enter a Startdate in YYYY-MM-DD format:\n')
                    endDate = input('Enter a Enddate in YYYY-MM-DD format:\n')
                    query="SELECT DISTINCT id,name,number_of_bedrooms,LEFT(description,25),MAX(price) FROM Listings,Calendar WHERE number_of_bedrooms= ? AND price >= ? AND price <= ? and id=listing_id AND (date >= ? AND date <= ? )AND  id NOT IN  (SELECT listing_id FROM Calendar WHERE (date >= ? AND date <= ?) AND (price >= ? AND price <= ? AND available = 0)) GROUP BY id,name,LEFT(description,25),number_of_bedrooms"
                    cursor.execute(query,noOfBedrooms,minimum,maximum,startDate,endDate,startDate,endDate,minimum,maximum)
            
                if command !='1' and command !='2'  and command !='3'  and command !='4':
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
                guests= int(input("Please enter number of guests\n"))
                SQLCommand = ("INSERT INTO Bookings(id,listing_id,guest_name,stay_from,stay_to,number_of_guests) VALUES (?,?,?,?,?,?)")  
                cursor.execute("Select MAX(id) AS max,Count(id) AS count FROM Bookings ")
                record=cursor.fetchall()
    
                if record[0][1]==0:
                    value=1
                elif record[0][1]==1:
                    value=2
                else:
                    value= int(record[0][0])+1

                VALUES = [value,to_book,input_name,startDate,endDate,guests]  
            
                cursor.execute(SQLCommand,VALUES) 
                print('Booking Updated\n')
                function(1)

    if first=='b':
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
                print('No Data Found with this name')
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
                function(1)
                
    connection.commit()
    connection.close()

def main():
    function(1)

if __name__== "__main__":
  main()