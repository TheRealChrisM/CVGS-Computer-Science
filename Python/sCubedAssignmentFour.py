#Christopher Marotta
#April 8th, 2020
#Assignment: S-Cubed A4

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons as widget

root = Tk()
selectionFrame = Frame(root)
inputFrame = Frame(root)
root.title("Input Window")


initialX = StringVar()
initialY = StringVar()
deltaXOne = StringVar()

initialX.set(55)
initialY.set(10)
deltaXOne.set(.01)


def fPrey(x,y):
    return ((.8*x)-((.04*x)*y))

def fPredator(x,y):
    return((-.3*y)+((.006*x)*y))

def killit():
    plt.close()
    return
 

def graphIt():
    global l,m
    global initialX, initialY, deltaXOne, deltaOneValueLabel
    killit()
    h = float(deltaXOne.get())
    a = 0
    b = 500
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
        newY = fPrey(curX,curY)
        nextY = curY + (h*newY)
        yVals.append(nextY)
        curY = nextY
        curX = curX + h
        xVals.append(curX)
    l, = plt.plot(xVals,yVals)
    
    yValsGraphTwo = []
    xValsGraphTwo = []
    yValsGraphTwo.append(initY)
    xValsGraphTwo.append(initX)
    curX = initX
    curY = initY
    while(curX < b):
        newY = fPredator(curX,curY)
        nextY = curY + (h*newY)
        yValsGraphTwo.append(nextY)
        curY = nextY
        curX = curX + h
        xValsGraphTwo.append(curX)
    m, = plt.plot(xValsGraphTwo,yValsGraphTwo)
    
    plt.title("S-Cubed A2 Assignment")
    plt.legend(["Prey","Predator"])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

axcolor = 'white'
rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
button = CheckButtons(rax, ('Prey','Predator'), (True,True))
button.on_clicked(updateLineType)    

inputRequestWindowLabel = Label(selectionFrame, text = "Enter Initial Values:", pady = 10, padx = 15)
initialXLabel = Label(inputFrame, text = "x:", pady = 5)
initialYLabel = Label(inputFrame, text = "y:", pady = 5)
deltaXOneLabel = Label(inputFrame, text = "Delta X:", pady = 5)
deltaXOneEntry = Entry(inputFrame, textvariable = deltaXOne)
initialXEntry = Entry(inputFrame, textvariable = initialX)
initialYEntry = Entry(inputFrame, textvariable = initialY)
goButton = Button(inputFrame, text = "Go!", command = graphIt)
deltaOneValueLabel = Label(inputFrame, text = "")
resultLabel = Label(inputFrame, text = "")

inputRequestWindowLabel.grid(row = 0, columnspan = 2)
selectionFrame.pack()

initialXLabel.grid(row = 0, column = 0)
initialYLabel.grid(row = 1, column = 0)
initialXEntry.grid(row = 0, column = 1)
initialYEntry.grid(row = 1, column = 1)
deltaXOneLabel.grid(row = 2, column = 0)
deltaXOneEntry.grid(row = 2, column = 1)
goButton.grid(row = 5, columnspan = 2)
deltaOneValueLabel.grid(row = 6, columnspan = 2)
inputFrame.pack()

root.mainloop()
