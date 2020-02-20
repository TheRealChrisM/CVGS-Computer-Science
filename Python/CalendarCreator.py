#Christopher Marotta
#Project 1: Create a Calendar
#August 29th, 2019

goAgain = "y"
while(goAgain == "y"):
    #Set global variables
    spot = 1 #used to determine when the date goes to the next row on the calendar
    curDay = 1 #used to track the current day of the calendar
    startDay = 0 #used later to determine what day of the week to start on
    endDate = 0 #used to determine what day of the month to end on

    #ask for month information to generate calendar
    startDay = eval(input("Please input the number for the day of the week your month starts on (Sunday = 1 & Saturday = 7): "))
    endDate = eval(input("Please input the number of days in your month: "))
    print()

    #format beginning line containing days of week
    print("  ", end="")
    print(format("Sun", "<5s"), end="")
    print(format("Mon", "<5s"), end="")
    print(format("Tue", "<5s"), end="")
    print(format("Wed", "<5s"), end="")
    print(format("Thu", "<5s"), end="")
    print(format("Fri", "<5s"), end="")
    print(format("Sat", "<5s"), end="")
    print()

    #generate line to divide beginning line from calendar
    for i in range(35):
        print("-", end="")
    print()

    #find the start location
    calStarted = False #forces the while loop to continue until the program locates the starting position
    #inserts spaces until the program locates the day of the week the calendar starts on
    while(not calStarted):
        if (spot != startDay):
            print(format("", ">5s"), end="")
        else:
            print(format(str(curDay), ">5s"), end="")
            curDay += 1
            calStarted = True
        spot+=1

    #start inputting numbers into the calendar
    while(curDay<=endDate):
        print(format(str(curDay), ">5s"), end="")
        #moves to the next line when end of week is reached
        if((spot%7) == 0):
            print()
        spot+=1
        curDay += 1
        
    print()
    
    #determine if user wants to generate a new calendar
    goAgain = input("Would you like to create another calendar (y/n): ")
        
