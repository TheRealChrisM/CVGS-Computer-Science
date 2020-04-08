#Christopher Marotta
#April 8th, 2020
#Assignment: S-Cubed A2

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
selectionFrame = Frame(root)
inputFrame = Frame(root)
root.title("Input Window")


initialX = StringVar()
initialY = StringVar()
deltaXOne = StringVar()
deltaXTwo = StringVar()
deltaXThree = StringVar()

def f(x,y):
    return ((3*x)-(2*y))

def killit():
    plt.close()
    return
 

def graphIt():
    global initialX, initialY, deltaXOne, deltaXTwo, deltaXThree, deltaOneValueLabel, deltaTwoValueLabel, deltaThreeValueLabel
    killit()
    h = float(deltaXOne.get())
    a = 0
    b = 2
    n = (b-a)/h

    initX = float(initialX.get())
    initY = float(initialY.get())
    
    xVals = []
    yVals = []

    yVals.append(initY)
    xVals.append(initX)

    displayNumOne = 0
    displayNumTwo = 0
    displayNumThree = 0
    
    curX = initX
    curY = initY
    while(curX < b):
        newY = f(curX,curY)
        nextY = curY + (h*newY)
        yVals.append(nextY)
        curY = nextY
        curX = curX + h
        xVals.append(curX)
    plt.plot(xVals,yVals)
    displayNumOne = np.interp(.5, xVals, yVals)
    deltaOneValueLabel["text"] = ("Delta One y(.5)=" + str(displayNumOne))
    
    h = float(deltaXTwo.get())
    
    yValsGraphTwo = []
    xValsGraphTwo = []
    yValsGraphTwo.append(initY)
    xValsGraphTwo.append(initX)
    curX = initX
    curY = initY
    while(curX < b):
        newY = f(curX,curY)
        nextY = curY + (h*newY)
        yValsGraphTwo.append(nextY)
        curY = nextY
        curX = curX + h
        xValsGraphTwo.append(curX)
    plt.plot(xValsGraphTwo,yValsGraphTwo)
    displayNumTwo = np.interp(.5, xValsGraphTwo, yValsGraphTwo)
    deltaTwoValueLabel["text"] = ("Delta Two y(.5)=" + str(displayNumTwo))
    h = float(deltaXThree.get())
    
    yValsGraphThree = []
    xValsGraphThree = []
    yValsGraphThree.append(initY)
    xValsGraphThree.append(initX)
    curX = initX
    curY = initY
    while(curX < b):
        newY = f(curX,curY)
        nextY = curY + (h*newY)
        yValsGraphThree.append(nextY)
        curY = nextY
        curX = curX + h
        xValsGraphThree.append(curX)
    plt.plot(xValsGraphThree,yValsGraphThree)
    displayNumThree = np.interp(.5, xValsGraphThree, yValsGraphThree)
    deltaThreeValueLabel["text"] = ("Delta Three y(.5)=" + str(displayNumThree))

    
    plt.title("S-Cubed A2 Assignment")
    plt.legend(["deltaXOne","deltaXTwo","deltaXThree"])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    

inputRequestWindowLabel = Label(selectionFrame, text = "Enter Initial Values:", pady = 10, padx = 15)
initialXLabel = Label(inputFrame, text = "x:", pady = 5)
initialYLabel = Label(inputFrame, text = "y:", pady = 5)
deltaXOneLabel = Label(inputFrame, text = "Delta X One:", pady = 5)
deltaXTwoLabel = Label(inputFrame, text = "Delta X Two:", pady = 5)
deltaXThreeLabel = Label(inputFrame, text = "Delta X Three:", pady = 5)
deltaXOneEntry = Entry(inputFrame, textvariable = deltaXOne)
deltaXTwoEntry = Entry(inputFrame, textvariable = deltaXTwo)
deltaXThreeEntry =Entry(inputFrame, textvariable = deltaXThree)
initialXEntry = Entry(inputFrame, textvariable = initialX)
initialYEntry = Entry(inputFrame, textvariable = initialY)
goButton = Button(inputFrame, text = "Go!", command = graphIt)
deltaOneValueLabel = Label(inputFrame, text = "")
deltaTwoValueLabel = Label(inputFrame, text = "")
deltaThreeValueLabel = Label(inputFrame, text = "")
resultLabel = Label(inputFrame, text = "")

inputRequestWindowLabel.grid(row = 0, columnspan = 2)
selectionFrame.pack()

initialXLabel.grid(row = 0, column = 0)
initialYLabel.grid(row = 1, column = 0)
initialXEntry.grid(row = 0, column = 1)
initialYEntry.grid(row = 1, column = 1)
deltaXOneLabel.grid(row = 2, column = 0)
deltaXTwoLabel.grid(row = 3, column = 0)
deltaXThreeLabel.grid(row = 4, column = 0)
deltaXOneEntry.grid(row = 2, column = 1)
deltaXTwoEntry.grid(row = 3, column = 1)
deltaXThreeEntry.grid(row = 4, column = 1)
goButton.grid(row = 5, columnspan = 2)
deltaOneValueLabel.grid(row = 6, columnspan = 2)
deltaTwoValueLabel.grid(row = 7, columnspan = 2)
deltaThreeValueLabel.grid(row = 8, columnspan = 2)
inputFrame.pack()

root.mainloop()

#I used delta x values of 0.05, 0.1, and 0.025. This represents the value required by the problem alongside both doubling and halving that number. I chose these numbers because I think they show the importance of a low delta x value
#which ensures a high level of accuracy in the graphed model. You can clearly see the line begin to become significantly more "smooth" as the delta x value decreases which would be expected as more calculations would need to occur in order
#to plot the line. Yes, it might be understandable to set a higher delta x value when trying to work on a problem like this by hand because of time constraints. In this case we are using a program run out calculations, so to take full
#advantage of this it would make most sense to begin using much smaller delta x values to attain a higher level of accuracy that best represents what is being modeled.
