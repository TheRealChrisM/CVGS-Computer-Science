#Christopher Marotta
#Project 1: Create a Calendar
#August 29th, 2019

goAgain = "y"
while(goAgain == "y"):
    #Set global variables
    spot = 0
    curDay = 1
    startDay = 0
    endDate = 0
    width = 35

    #ask for month information
    startDay = eval(input("Please input the number for the day of the week your month starts on (Sunday = 1 & Saturday = 7): "))
    endDate = eval(input("Please input the number of days in your month: "))
    print()

    #format beginning lines
    print("  ", end="")
    print(format("Sun", "<5s"), end="")
    print(format("Mon", "<5s"), end="")
    print(format("Tue", "<5s"), end="")
    print(format("Wed", "<5s"), end="")
    print(format("Thu", "<5s"), end="")
    print(format("Fri", "<5s"), end="")
    print(format("Sat", "<5s"), end="")
    print()

    for i in range(35):
        print("-", end="")
    print()

    #find the start location
    calStarted = False
    while(not calStarted):
        if (spot != startDay):
            print(format("", ">5s"), end="")
        else:
            print(format(str(curDay), ">5s"), end="")
            curDay += 1
            calStarted = True
        spot+=1

    #start inputting numbers
    while(curDay<=endDate):
        if((spot%7) == 0):
            print()
        print(format(str(curDay), ">5s"), end="")
        spot+=1
        curDay += 1
    print()
    goAgain = input("Would you like to create another calendar (y/n): ")
        
