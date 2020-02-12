#Christopher Marotta
#RPN Calculator Project
#February 6th, 2020

#Import the tkinter library for graphics.
from tkinter import *

#************************************************************************
#Creates a StackNode Class so that the nodes for the stack can be created.
class StackNode:
    #Instantiates the stacknode class with data and a "next" node pointer.
    def __init__(self, myData, myNext):
        #Assigns the data value for the node.
        self.data = myData
        #Establishes the next node that this node will point to.
        self.next = myNext
        
#************************************************************************
#Creates a Stack class to store data variables.
class Stack:
    #Instantiates the stack class without any inputs.
    def __init__(self):
        #Establishes the location of the first node which doesn't exist as there is not any data in the list yet.
        self.firstNode = None #LinkedListNode(None, None)
        #Points the last node in the same place as the first one.
        self.lastNode = self.firstNode
        #Sets the size of the list to 0.
        self.size = 0
        return

    #************************************************************************
    #Function which returns the size of the list.
    def checkSize(self):
        #Return the current size of the list.
        return self.size

    #************************************************************************
    #Function which adds data to the "top" of the stack. Takes in the data that is to be added.
    def push(self, data):
        #Creates a new node which doesn't point to anything.
        node = StackNode(data, None)
        #Checks to see if there is nothing in the list yet.
        if self.firstNode == None: #.data == None:
            #Sets the new node as the first node in the list.
            self.firstNode = node
            #Sets the new node as the last node in the list.
            self.lastNode = node
        #Checks if there is already data in the list.
        else:
            #Makes the previous last node point to this new one.
            self.lastNode.next = node
            #Saves this as the new last node.
            self.lastNode = node
        #Increases the size of the stack by one.
        self.size += 1
        return

    #************************************************************************
    #Function which removes data from the "top" of the stack. This does not take any inputs.
    def pop(self):
        #Checks to see if the list is empty.
        if (self.size == 0):
            #If the list is empty, return nothing.
            rearData = None
        #Checks to see if the list is not empty yet.
        else:
            #Records the "current node" for tracking through the list.
            currentNode = self.firstNode
            #Records the data of the last node.
            rearData = self.lastNode.data
            # This is the case where we have only one node in the list
            if self.size == 1:
                #Sets the first node as None to indicate that it is removed.
                self.firstNode = None #LinkedListNode(None, None)
                #Sets the last node equal to the first node.
                self.lastNode = self.firstNode
                #Sets the size of the stack to zero as there is nothing left.
                self.size = 0
            #Checks to see if there is more than one node in the list.
            else:
                #Goes through the list until it gets to the second to last node.
                while not(currentNode.next == self.lastNode):
                    #Sets the current "pointer" node to the next node in the stack.
                    currentNode = currentNode.next
                #Sets the new last node as the second to last node in the stack.
                self.lastNode = currentNode
                #Decreases the stack size by one.
                self.size = self.size - 1
        #Returns the data from the node which was just removed, or returns None if no node was removed.
        return rearData

    #************************************************************************
    #Function which allows the stack to be printed out to the console.
    def __str__(self):
        #Sets the current "pointer" node to the first node.
        currentNode =  self.firstNode
        #Goes through the stack.
        for i in range(self.size):
            #Prints out the data from the current "pointer" node.
            print (currentNode.data)
            #Moves the "pointer" node to the next node.
            currentNode = currentNode.next
        #Returns a string indicating it has reached the end of the stack.
        return "Reached end of list.\n"

#************************************************************************
#Class which houses the logic for the RPNCalculator.
class RPNCalculator:
    #Initializes the calculator function so that it can be used. Runs the calculator.
    def __init__(self):
        #Creates a new stack object.
        self.calcMem = Stack()
        #Creates a variable for the Store function of the calculator.
        self.storedNum = ""
        #Creates a Tkinter window to be used to display the calculator.
        window = Tk()
        #Prevents the Tkinter window from being resized.
        window.resizable(False, False)
        #Sets the size of the Tkinter window to 175x175.
        window.geometry("175x175")
        #Sets the title of the window to nothing because it is too small to properly display a title.
        window.title("")
        #Creates the main frame for all the Tkinter widgets to be housed in.
        mainFrame = Frame(window)
        #Creates a stringVar to represent the "screen" of the calculator.
        self.screenText = StringVar()

        #Creates an entrybox for the calculator screen that is disabled so users cannot manipulate it.
        screen = Entry(mainFrame, textvariable = self.screenText, state = "disabled")
        #Creates the Enter button so users can add numbers to the RPN stack.
        buttonEnter = Button(mainFrame, text = "ENTER", command = self.pressEnter)
        #Creates the store button so that users can store the number currently displayed on the calculator.
        buttonStore = Button(mainFrame, text = "STO", command = self.pressStore, height = 1, width = 2)
        #Creates a recall button so that users can "recall" a saved number in memory.
        buttonRecall = Button(mainFrame, text = "RCL", command = self.pressRecall, height = 1, width = 2)
        #Creates a plus button so that users can perform summation with numbers.
        buttonPlus = Button(mainFrame, text = "-", command = self.pressMinus, height = 1, width = 2)
        #Creates a minus button so that users can perform subtraction with numbers.
        buttonMinus = Button(mainFrame, text = "+", command = self.pressPlus, height = 1, width = 2)
        #Creates a divide button so users can perform division with numbers.
        buttonDivide = Button(mainFrame, text = "÷", command = self.pressDivide, height = 1, width = 2)
        #Creates a multiply button so that users can perform multiplication with numbers.
        buttonMultiply = Button(mainFrame, text = "×", command = self.pressMultiply, height = 1, width = 2)
        #Creates a "0" button so that users can use that number in the calculator.
        buttonZero = Button(mainFrame, text = "0", command = self.pressZero, height = 1, width = 2)
        #Creates a "1" button so that users can use that number in the calculator.
        buttonOne = Button(mainFrame, text = "1", command = self.pressOne, height = 1, width = 2)
        #Creates a "2" button so that users can use that number in the calculator.
        buttonTwo = Button(mainFrame, text = "2", command = self.pressTwo, height = 1, width = 2)
        #Creates a "3" button so that users can use that number in the calculator.
        buttonThree = Button(mainFrame, text = "3", command = self.pressThree, height = 1, width = 2)
        #Creates a "4" button so that users can use that number in the calculator.
        buttonFour = Button(mainFrame, text = "4", command = self.pressFour, height = 1, width = 2)
        #Creates a "5" button so that users can use that number in the calculator.
        buttonFive = Button(mainFrame, text = "5", command = self.pressFive, height = 1, width = 2)
        #Creates a "6" button so that users can use that number in the calculator.
        buttonSix = Button(mainFrame, text = "6", command = self.pressSix, height = 1, width = 2)
        #Creates a "7" button so that users can use that number in the calculator.
        buttonSeven = Button(mainFrame, text = "7", command = self.pressSeven, height = 1, width = 2)
        #Creates a "8" button so that users can use that number in the calculator.
        buttonEight = Button(mainFrame, text = "8", command = self.pressEight, height = 1, width = 2)
        #Creates a "9" button so that users can use that number in the calculator.
        buttonNine = Button(mainFrame, text = "9", command = self.pressNine, height = 1, width = 2)
        #Creates a button that clears the stack and screen of the calculator.
        buttonCLR = Button(mainFrame, text = "C", command = self.pressClear, height = 1, width = 2)
        #Creates a button that clears the calculator screen.
        buttonCE = Button(mainFrame, text = "CE", command = self.pressClearAll, height = 1, width = 2)

        #Displays the screen on the frame.
        screen.grid(row = 0, columnspan = 4, pady=10)
        #Displays the enter button on the frame.
        buttonEnter.grid(row = 1, columnspan = 2, sticky = "nesw")
        #Displays the store button on the frame.
        buttonStore.grid(row = 1, column = 2, sticky = "nesw")
        #Displays the recall button on the frame.
        buttonRecall.grid(row = 1, column = 3, sticky = "nesw")
        #Displays the plus button on the frame.
        buttonPlus.grid(row = 2, column = 0, sticky = "nesw")
        #Displays the minus button on the frame.
        buttonMinus.grid(row = 3, column = 0, sticky = "nesw")
        #Displays the divide button on the frame.
        buttonDivide.grid(row = 4, column = 0, sticky = "nesw")
        #Displays the multiply button on the frame.
        buttonMultiply.grid(row = 5, column = 0, sticky = "nesw")
        #Displays the clear button on the frame.
        buttonCLR.grid(row = 5, column = 2, sticky = "nesw")
        #Displays the clear button on the frame.
        buttonCE.grid(row = 5, column = 3, sticky = "nesw")
        #Displays the zero button on the frame.
        buttonZero.grid(row = 5, column = 1, sticky = "nesw")
        #Displays the one button on the frame.
        buttonOne.grid(row = 4, column = 1, sticky = "nesw")
        #Displays the two button on the frame.
        buttonTwo.grid(row = 4, column = 2, sticky = "nesw")
        #Displays the three button on the frame.
        buttonThree.grid(row = 4, column = 3, sticky = "nesw")
        #Displays the four button on the frame.
        buttonFour.grid(row = 3, column = 1, sticky = "nesw")
        #Displays the five button on the frame.
        buttonFive.grid(row = 3, column = 2, sticky = "nesw")
        #Displays the six button on the frame.
        buttonSix.grid(row = 3, column = 3, sticky = "nesw")
        #Displays the seven button on the frame.
        buttonSeven.grid(row = 2, column = 1, sticky = "nesw")
        #Displays the eight button on the frame.
        buttonEight.grid(row = 2, column = 2, sticky = "nesw")
        #Displays the nine button on the frame.
        buttonNine.grid(row = 2, column = 3, sticky = "nesw")

        #Packs the main frame into the Tkinter window.
        mainFrame.pack()
        #Begins running the GUI for the application.
        window.mainloop()
        return

    #************************************************************************
    #Function to be run when the zero button is pressed.
    def pressZero(self):
        #Adds a zero to the current screen string.
        newStr = self.screenText.get()+ "0"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the one button is pressed.
    def pressOne(self):
        #Adds a one to the current screen string.
        newStr = self.screenText.get()+ "1"
        self.screenText.set(newStr)
        return

    #************************************************************************    
    #Function to be run when the two button is pressed.
    def pressTwo(self):
        #Adds a two to the current screen string.
        newStr = self.screenText.get()+ "2"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the three button is pressed.
    def pressThree(self):
        #Adds a three to the current screen string.
        newStr = self.screenText.get()+ "3"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the four button is pressed.
    def pressFour(self):
        #Adds a four to the current screen string.
        newStr = self.screenText.get()+ "4"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the five button is pressed.
    def pressFive(self):
        #Adds a five to the current screen string.
        newStr = self.screenText.get()+ "5"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the six button is pressed.
    def pressSix(self):
        #Adds a six to the current screen string.
        newStr = self.screenText.get()+ "6"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the seven button is pressed.
    def pressSeven(self):
        #Adds a seven to the current screen string.
        newStr = self.screenText.get()+ "7"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the eight button is pressed.
    def pressEight(self):
        #Adds a eight to the current screen string.
        newStr = self.screenText.get()+ "8"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the nine button is pressed.
    def pressNine(self):
        #Adds a nine to the current screen string.
        newStr = self.screenText.get()+ "9"
        #Displays the new current screen string.
        self.screenText.set(newStr)
        return

    #************************************************************************
    #Function to be run when the enter button is pressed.
    def pressEnter(self):
        #Identifies code to try and check for error.
        try:
            #Adds the current screen string to the stack.
            self.calcMem.push(eval(self.screenText.get()))
            #Resets the screen string.
            self.screenText.set("")
        #Checks to see if a error is found.
        except:
            #Clears the entire variable stack and screen string.
            self.pressClearAll()
            #Sets the current screen string to "ERR" to represent error.
            self.screenText.set("ERR")
        return

    #************************************************************************
    #Function to be run when the store button is pressed.
    def pressStore(self):
        #Saves the current screen string to the memory variable.
        self.storedNum = self.screenText.get()
        #Clears the current screen string.
        self.pressClear()
        return

    #************************************************************************
    #Function to be run when the recall button is pressed.
    def pressRecall(self):
        #Sets the current screen text variable to the memory variable.
        self.screenText.set(self.storedNum)
        return

    #************************************************************************
    #Function to be run when the plus button is pressed.
    def pressPlus(self):
        #Checks to make sure that the screen has characters in it.
        screenText = (not(self.screenText.get()==""))
        #Ensures that the stack has atleast one number in it.
        stackPopulated = (self.calcMem.checkSize()>0)
        #If the screen has characters and stack has data then continue.
        if((screenText)and(stackPopulated)):
            #Pops off the first number from the stack for calculations.
            numOne = self.calcMem.pop()
            #Gets the second number which is the one currently displayed on the screen string.
            numTwo = eval(self.screenText.get())
            #Adds the two numbers together.
            answer = numOne + numTwo
            #Displays the new number into the screen string.
            self.screenText.set(str(answer))
        #Runs this if there is any reason that the computation can't be completed.
        else:
            #Clears the screen variable and the stack.
            self.pressClearAll()
            #Sets the screen to "ERR" to represent an error.
            self.screenText.set("ERR")
        return

    #************************************************************************
    #Function to be run when the minus button is pressed.
    def pressMinus(self):
        #Checks to make sure that the screen has characters in it.
        screenText = (not(self.screenText.get()==""))
        #Ensures that the stack has atleast one number in it.
        stackPopulated = (self.calcMem.checkSize()>0)
        #If the screen has characters and stack has data then continue.
        if((screenText)and(stackPopulated)):
            #Pops off the first number from the stack for calculations.
            numOne = self.calcMem.pop()
            #Gets the second number which is the one currently displayed on the screen string.
            numTwo = eval(self.screenText.get())
            #Subtracts the two numbers.
            answer = numOne - numTwo
            #Displays the new number into the screen string.
            self.screenText.set(str(answer))
        #Runs this if there is any reason that the computation can't be completed.
        else:
            #Clears the screen variable and the stack.
            self.pressClearAll()
            #Sets the screen to "ERR" to represent an error.
            self.screenText.set("ERR")
        return

    #************************************************************************
    #Function to be run when the divide button is pressed.
    def pressDivide(self):
        #Checks to make sure that the screen has characters in it.
        screenText = (not(self.screenText.get()==""))
        #Ensures that the stack has atleast one number in it.
        stackPopulated = (self.calcMem.checkSize()>0)
        #If the screen has characters and stack has data then continue.
        if((screenText)and(stackPopulated)):
            #Pops off the first number from the stack for calculations.
            numOne = self.calcMem.pop()
            #Gets the second number which is the one currently displayed on the screen string.
            numTwo = eval(self.screenText.get())
            #Divides the two numbers.
            answer = numOne / numTwo
            #Displays the new number into the screen string.
            self.screenText.set(str(answer))
        #Runs this if there is any reason that the computation can't be completed.
        else:
            #Clears the screen variable and the stack.
            self.pressClearAll()
            #Sets the screen to "ERR" to represent an error.
            self.screenText.set("ERR")
        return

    #************************************************************************
    #Function to be run when the multiply button is pressed.
    def pressMultiply(self):
        #Checks to make sure that the screen has characters in it.
        screenText = (not(self.screenText.get()==""))
        #Ensures that the stack has atleast one number in it.
        stackPopulated = (self.calcMem.checkSize()>0)
        #If the screen has characters and stack has data then continue.
        if((screenText)and(stackPopulated)):
            #Pops off the first number from the stack for calculations.
            numOne = self.calcMem.pop()
            #Gets the second number which is the one currently displayed on the screen string.
            numTwo = eval(self.screenText.get())
            #Multiplies the two numbers.
            answer = numOne * numTwo
            #Displays the new number into the screen string.
            self.screenText.set(str(answer))
        #Runs this if there is any reason that the computation can't be completed.
        else:
            #Clears the screen variable and the stack.
            self.pressClearAll()
            #Sets the screen to "ERR" to represent an error.
            self.screenText.set("ERR")
        return

    #************************************************************************
    #Function to be run when the clear button is pressed.
    def pressClear(self):
        #Sets the current screen text to nothing to represent clearing the number.
        self.screenText.set("")
        return

    #************************************************************************
    #Function to be run when the clear all button is pressed.
    def pressClearAll(self):
        #Runs this code while the stack has data in it.
        while(self.calcMem.checkSize()>0):
            #Pops off the last node in the stack.
            self.calcMem.pop()
        #Sets the screen variable to nothing.
        self.screenText.set("")  
        return


#Creates a calculator object to begin the program.
calc = RPNCalculator()
