class getDriverAttributes():
    
    def getDriverMode(ID_number, mycursor):
        #Prints Users 
        mycursor.execute("SELECT driverMode FROM users WHERE userID = " + ID_number)
        myresult = mycursor.fetchall()
        for x in myresult:
            DriverMode = x[0]
        return(DriverMode)