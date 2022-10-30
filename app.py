import mysql.connector
from riderOptions import riderOptions
from updateDriverAttributes import updateDriverAttributes
from getDriverAttributes import getDriverAttributes

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

#sql = "ALTER TABLE users ADD COLUMN FromAddress VARCHAR(30), ADD COLUMN ToAddress VARCHAR(30)"
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

#Prints Users 
mycursor.execute("SELECT* FROM users WHERE userID = " + ID_number)
myresult = mycursor.fetchall()
for x in myresult:
    RiderType = x[1]

if RiderType == "Rider":
    riderChoice = riderOptions.getRiderChoice()
    if riderChoice == "1":
        riderOptions.findOpenDriver(mycursor)
        
        #TODO 
        # Find Driver with Drive Mode On = True
        # Enter To Address
        # Enter From Address
    if riderChoice == "2":
        print("Rating Driver")
        #TODO
        #Lookup last Driver ID
        #Ask Rider for new Rating
        #Then, calculate the driver’s new rating by taking their current rating + their new rating and dividing by 2.
elif RiderType == "Driver":
    driverMode = getDriverAttributes.getDriverMode(ID_number,mycursor)
    if driverMode == 0:
        wantsToChangeMode = input("Your driver mode is currently off, would you like to turn it on? (y/n) ")
        if wantsToChangeMode == "y":
            modeVal = "true"
            updateDriverAttributes.changeDriverMode(ID_number, mycursor,mydb, modeVal)
    elif driverMode == 1:
        wantsToChangeMode = input("Your driver mode is currently on, would you like to turn it off? (y/n) ")
        if wantsToChangeMode == "y":
            modeVal = "false"
            updateDriverAttributes.changeDriverMode(ID_number, mycursor,mydb, modeVal)
    
mydb.close()