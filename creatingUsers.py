#Christopher Marotta
#January 8, 2020
#Lab Assignment (Jan 7) Part 1

from tkinter import *

#variable for the location of the database file.
databaseLoc = "userDB.txt"

#Creates a class for User Objects
class User:
    #Initilizes the new user object
    def __init__(self, fName="", lName="", favColor=""):
        self.__firstName = fName
        self.__lastName = lName
        self.__color = favColor
        
    #returns the person's first name
    def getFirstName(self):
        return self.__firstName

    #returns the person's last name
    def getLastName(self):
        return self.__lastName

    #returns the person's favorite color
    def getFavColor(self):
        return self.__color

    #Overloads the to string method for this class
    def __str__(self):
        returnString = self.getFirstName() + ","
        returnString = returnString + self.getLastName() + ","
        returnString = returnString + self.getFavColor() + "\n"
        return returnString

#Sets up Tkinter
window = Tk()
frame = Frame(window)

#Sets up db access function
def addUser():
    #Access the Database
    inputFile = open(databaseLoc, "r")
    currentUsers = ""
    currentUsersList = inputFile.readlines()
    for i in range(len(currentUsersList)):
        currentUsers = currentUsers + currentUsersList[i]
    inputFile.close()
    #creates new user
    newUser = User(firstNameInput.get(), lastNameInput.get(), colorInput.get())
    #Access database
    outputFile = open(databaseLoc, "w")
    #adds new user to database and closes file
    currentUsers = currentUsers + str(newUser)
    outputFile.write(currentUsers)
    outputFile.close()
    firstNameInput.set("")
    lastNameInput.set("")
    colorInput.set("")
    return

#Creates labels
titleLabel = Label(frame, text = "Create New User")
firstLabel = Label(frame, text = "First Name: ")
lastLabel = Label(frame, text = "Last Name: ")
colorLabel = Label(frame, text = "Favorite Color: ")

#Creates input variables
firstNameInput = StringVar()
lastNameInput = StringVar()
colorInput = StringVar()

#Creates entry boxes
firstEntry = Entry(frame, textvariable = firstNameInput)
lastEntry = Entry(frame, textvariable = lastNameInput)
colorEntry = Entry(frame, textvariable = colorInput)

#creates button
submitButton = Button(frame, text = "SUBMIT", command = addUser)

#grids widgets and packs frame
titleLabel.grid(row = 0, columnspan = 2)
firstLabel.grid(row = 1, column = 0, sticky = "E")
lastLabel.grid(row = 2, column = 0, sticky = "E")
colorLabel.grid(row = 3, column = 0, sticky = "E")
firstEntry.grid(row = 1, column = 1)
lastEntry.grid(row = 2, column = 1)
colorEntry.grid(row = 3, column = 1)
submitButton.grid(row = 4, columnspan = 2)
frame.pack()

window.mainloop()
