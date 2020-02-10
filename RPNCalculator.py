#Christopher Marotta
#RPN Calculator Project
#February 6th, 2020

from tkinter import *

class StackNode:
    def __init__(self, myData, myNext):
        self.data = myData
        self.next = myNext

class Stack:
    def __init__(self):
        #Construct a new StackNode. The first node and last node are the same. Size is 0
        self.firstNode = None #LinkedListNode(None, None)
        self.lastNode = self.firstNode
        self.size = 0
        return

    def push(self, data):
        #Add a node to the front of the list
        node = StackNode(data, None)
        if self.firstNode == None: #.data == None:
            self.firstNode = node
            self.lastNode = node
        else:
            self.lastNode.next = node
            self.lastNode = node
        self.size += 1
        return
        
    def pop(self):
        #Remove a node from the end of the list
        if self.size == 0:
            print ("Linked List is empty")
            rearData = None
        else:
            currentNode = self.firstNode
            rearData = self.lastNode.data
            # This is the case where we have only one node in the list
            if currentNode.next == None:
                self.firstNode = None #LinkedListNode(None, None)
                self.lastNode = self.firstNode
                self.size = self.size - 1
            else:
                while not(currentNode.next == self.lastNode):
                    currentNode = currentNode.next
                # Here there are more than one nodes in the list
                self.lastNode = currentNode
                self.size = self.size - 1
        return rearData

    def __str__(self):
        currentNode =  self.firstNode
        for i in range(self.size):
            print (currentNode.data)
            currentNode = currentNode.next
        return "Reached end of list.\n"

class RPNCalculator:
    def __init__(self):
        self.calcMem = Stack()
        self.storedNum = ""
        window = Tk()
        window.resizable(False, False)
        window.geometry("175x175")
        window.title("")
        mainFrame = Frame(window)
        self.screenText = StringVar()
        
        screen = Entry(mainFrame, textvariable = self.screenText, state = "disabled")
        buttonEnter = Button(mainFrame, text = "ENTER", command = self.pressEnter)
        buttonStore = Button(mainFrame, text = "STO", command = self.pressStore, height = 1, width = 2)
        buttonRecall = Button(mainFrame, text = "RCL", command = self.pressRecall, height = 1, width = 2)
        buttonPlus = Button(mainFrame, text = "-", command = self.pressMinus, height = 1, width = 2)
        buttonMinus = Button(mainFrame, text = "+", command = self.pressPlus, height = 1, width = 2)
        buttonDivide = Button(mainFrame, text = "÷", command = self.pressDivide, height = 1, width = 2)
        buttonMultiply = Button(mainFrame, text = "×", command = self.pressMultiply, height = 1, width = 2)
        buttonZero = Button(mainFrame, text = "0", command = self.pressZero, height = 1, width = 2)
        buttonOne = Button(mainFrame, text = "1", command = self.pressOne, height = 1, width = 2)
        buttonTwo = Button(mainFrame, text = "2", command = self.pressTwo, height = 1, width = 2)
        buttonThree = Button(mainFrame, text = "3", command = self.pressThree, height = 1, width = 2)
        buttonFour = Button(mainFrame, text = "4", command = self.pressFour, height = 1, width = 2)
        buttonFive = Button(mainFrame, text = "5", command = self.pressFive, height = 1, width = 2)
        buttonSix = Button(mainFrame, text = "6", command = self.pressSix, height = 1, width = 2)
        buttonSeven = Button(mainFrame, text = "7", command = self.pressSeven, height = 1, width = 2)
        buttonEight = Button(mainFrame, text = "8", command = self.pressEight, height = 1, width = 2)
        buttonNine = Button(mainFrame, text = "9", command = self.pressNine, height = 1, width = 2)
        buttonCLR = Button(mainFrame, text = "C", command = self.pressClear, height = 1, width = 2)
        buttonCE = Button(mainFrame, text = "CE", command = self.pressClearAll, height = 1, width = 2)
        
        screen.grid(row = 0, columnspan = 4, pady=10)
        buttonEnter.grid(row = 1, columnspan = 2, sticky = "nesw")
        buttonStore.grid(row = 1, column = 2, sticky = "nesw")
        buttonRecall.grid(row = 1, column = 3, sticky = "nesw")
        buttonPlus.grid(row = 2, column = 0, sticky = "nesw")
        buttonMinus.grid(row = 3, column = 0, sticky = "nesw")
        buttonDivide.grid(row = 4, column = 0, sticky = "nesw")
        buttonMultiply.grid(row = 5, column = 0, sticky = "nesw")
        buttonCLR.grid(row = 5, column = 2, sticky = "nesw")
        buttonCE.grid(row = 5, column = 3, sticky = "nesw")
        buttonZero.grid(row = 5, column = 1, sticky = "nesw")
        buttonOne.grid(row = 4, column = 1, sticky = "nesw")
        buttonTwo.grid(row = 4, column = 2, sticky = "nesw")
        buttonThree.grid(row = 4, column = 3, sticky = "nesw")
        buttonFour.grid(row = 3, column = 1, sticky = "nesw")
        buttonFive.grid(row = 3, column = 2, sticky = "nesw")
        buttonSix.grid(row = 3, column = 3, sticky = "nesw")
        buttonSeven.grid(row = 2, column = 1, sticky = "nesw")
        buttonEight.grid(row = 2, column = 2, sticky = "nesw")
        buttonNine.grid(row = 2, column = 3, sticky = "nesw")
        
        mainFrame.pack()
        window.mainloop()
        return
    
    def pressZero(self):
        newStr = self.screenText.get()+ "0"
        self.screenText.set(newStr)
        return
    
    def pressOne(self):
        newStr = self.screenText.get()+ "1"
        self.screenText.set(newStr)
        return
    
    def pressTwo(self):
        newStr = self.screenText.get()+ "2"
        self.screenText.set(newStr)
        return
    
    def pressThree(self):
        newStr = self.screenText.get()+ "3"
        self.screenText.set(newStr)
        return
    
    def pressFour(self):
        newStr = self.screenText.get()+ "4"
        self.screenText.set(newStr)
        return
    
    def pressFive(self):
        newStr = self.screenText.get()+ "5"
        self.screenText.set(newStr)
        return
    
    def pressSix(self):
        newStr = self.screenText.get()+ "6"
        self.screenText.set(newStr)
        return
    
    def pressSeven(self):
        newStr = self.screenText.get()+ "7"
        self.screenText.set(newStr)
        return
    
    def pressEight(self):
        newStr = self.screenText.get()+ "8"
        self.screenText.set(newStr)
        return
    
    def pressNine(self):
        newStr = self.screenText.get()+ "9"
        self.screenText.set(newStr)
        return
    
    def pressEnter(self):
        self.calcMem.push(int(self.screenText.get()))
        self.screenText.set("")
        return
    
    def pressStore(self):
        self.storedNum = self.screenText.get()
        self.pressClear()
        return
    
    def pressRecall(self):
        self.screenText.set(self.storedNum)
        return

    def pressPlus(self):
        numOne = self.calcMem.pop()
        numTwo = int(self.screenText.get())
        answer = numOne + numTwo
        self.screenText.set(str(answer))
        return

    def pressMinus(self):
        numOne = self.calcMem.pop()
        numTwo = int(self.screenText.get())
        answer = numOne - numTwo
        self.screenText.set(str(answer))
        return

    def pressDivide(self):
        numOne = self.calcMem.pop()
        numTwo = int(self.screenText.get())
        answer = numOne / numTwo
        self.screenText.set(str(answer))
        return

    def pressMultiply(self):
        numOne = self.calcMem.pop()
        numTwo = int(self.screenText.get())
        answer = numOne * numTwo
        self.screenText.set(str(answer))
        return

    def pressClear(self):
        self.screenText.set("")
        return

    def pressClearAll(self):
        return


    
calc = RPNCalculator()
