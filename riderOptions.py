class riderOptions():
    def getRiderChoice():
        print("\n")
        print("What would you like to do?")
        print("1. Find a Driver")
        print("2. Rate my Driver")
        print("\n")
        RiderChoice = input("Input Choice: ")
        print("\n")
        return RiderChoice
    
    def findOpenDriver(mycursor):
        print("Finding Open Driver")
        mycursor.execute("SELECT userID FROM users WHERE DriverMode = false")
        myresult = mycursor.fetchall()
        for x in myresult:
            OpenDriverID = x[0]
        print(OpenDriverID)
        return(OpenDriverID)
