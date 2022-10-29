import mysql.connector
from riderOptions import riderOptions
from driverOptions import driverOptions

mydb = mysql.connector.connect(host="localhost",
user="root",
password="Password!",
auth_plugin = 'mysql_native_password',
database="RideShare")
#print(mydb)

#create cursor obj to interact with mySQL
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE users (userID VARCHAR(22), name VARCHAR(20), userType VARCHAR(22))")

#Insert Table

#sql = "INSERT INTO users (userID, userType, DriverMode, DriverRating) VALUES(%s,%s, %s,%s)"
#vals = [
    #('3','Rider', None, None ),
    #('4','Driver', False, '3.0')
#]
#mycursor.executemany(sql,vals)

#sql = "INSERT INTO users (userID, userType) VALUES(%s,%s)"
#vals = [
    #('1','Rider'),
    #('2','Driver')
#]

#Alter Table Comands

#sql = "ALTER TABLE users ADD COLUMN DriverMode BOOLEAN, ADD COLUMN DriverRating FLOAT"
#mycursor.execute(sql)

#mydb.commit()
#print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT* FROM users")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#show the databases that eist in my local mysql

#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#    print(x)

#APP START
print("\n")
ID_number = input("Enter your User ID number: ")

mycursor.execute("SELECT* FROM users WHERE userID = " + ID_number)
myresult = mycursor.fetchall()
for x in myresult:
    RiderType = x[1]
    
    
if RiderType == "Rider":
    riderChoice = riderOptions.getRiderChoice()
    if riderChoice == "1":
        print("Finding Driver")
        #TODO 
        # Find Driver with Drive Mode On = True
    if riderChoice == "2":
        print("Rating Driver")
            #If Choice = Rate my Driver
                #Lookup last Driver ID
                #Ask Rider for new Rating
                #Then, calculate the driver’s new rating by taking their current rating + their new rating and dividing by 2.
elif RiderType == "Driver":
    driverChoice = driverOptions.getDriverChoice()
    if driverChoice == "1":
        print("Turning Drive Mode On")
    if driverChoice == "2":
        print("Exiting... ")
    #TODO
        #Ask them if they would like to turn Drive mode on
            #If Choice = Find a Drive
                #Find a Driver with Drive Mode On
            #If Choice = Rate my Driver
                #Lookup last Driver ID
                #Ask Rider for new Rating
                #Then, calculate the driver’s new rating by taking their current rating + their new rating and dividing by 2.
                

    

    
mydb.close()