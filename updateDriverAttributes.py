class updateDriverAttributes():
    def changeDriverMode(ID_number, mycursor,mydb,modeVal):
        #Prints Users 
        mycursor.execute("UPDATE users SET DriverMode = " + modeVal + " WHERE userID = " + ID_number)
        print("Drive Mode now set to " + modeVal)
        mydb.commit()
    

