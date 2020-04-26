#Christopher Marotta
#April 20, 2020
#Foxes and Rabbits

#The equilibrium solutions are found at approximately (0,0) and (50,20).
#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
from tkinter import *

#Sets default values for MatPlotLib Widgets
lineType = 1
rateIncrease = 1.00

#Setting up the graph.
fig, ax = plt.subplots()
ax.set_title("Foxes and Rabbits Assignment [A4]")
ax.set_xlabel("Time")
ax.set_ylabel("Animals")
plt.subplots_adjust(left=0.30, right=0.95, bottom=0.25)

root = Tk()
selectionFrame = Frame(root)
inputFrame = Frame(root)
root.title("Input Window")

a = 0
deltaTime = .01
n = 10000
b = n*deltaTime

rA = np.zeros(n)
fA = np.zeros(n)

initialX = IntVar()
initialY = IntVar()
rateA = DoubleVar()
rateB = DoubleVar()
rateC = DoubleVar()
rateD = DoubleVar()

initialX.set(55)
initialY.set(10)
rateA.set(.8)
rateB.set(.04)
rateC.set(.3)
rateD.set(.006)
showFoxes = True
showRabbits = True

def euler():
    rA[0] = initialX.get()
    fA[0] = initialY.get()
    for x in range(1, n):
        rA[x] = rA[x-1] + deltaTime * rabbitPopulation(rA[x-1], fA[x-1])
        fA[x] = fA[x-1] + deltaTime * quarentinedEquation(rA[x-1], fA[x-1])

def rabbitPopulation(x,y):
    
    return ((rateA.get()*x)-(rateB.get()*x*y))

def quarentinedEquation(x, y):
    return ((-1*y*rateC.get())+(rateD.get()*x*y))
    
def updateRate(val):
    global rateIncrease
    rateIncrease = val
    updateLines()
    return

def updateLineType(val):
    
    if (val == "Foxes"):
         toggleFoxes()
    elif (val == "Rabbits"):
         toggleRabbits()
    updateLines()
    return

def toggleFoxes():
    global showFoxes
    showFoxes = not showFoxes

def toggleRabbits():
    global showRabbits
    showRabbits = not showRabbits
    
def updateLines():
    #Reset graph and set limits on axes.
    ax.cla()
    euler()
    ax.set_title("Foxes and Rabbits Assignment [A4]")
    ax.set_xlabel("Time")
    ax.set_ylabel("Animals")
    fig.canvas.draw_idle()
    if (showFoxes and showRabbits):
        foxesGraph()
        rabbitsGraph()
    elif (showFoxes):
        foxesGraph()
    elif (showRabbits):
        rabbitsGraph()
    return

def foxesGraph():
    global foxes
    #Setting up subplot.
    ax.grid(True)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    #Displaying the control group.
    xControl = np.linspace(a,b,n)
    yControl = fA
    foxes, = ax.plot(xControl, yControl)
    
    
def rabbitsGraph():
    global rabbits
    #Setting up subplot.
    ax.grid(True)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    
    #Displaying the control group.
    xControl = np.linspace(a,b,n)
    yControl = rA
    rabbits, = ax.plot(xControl, yControl)


def graphIt():
    print("goin")
    #Gets everything started by calculating the datasets before anything is graphed.
    euler()
    #Graphs the susceptible population.
    foxesGraph()
    rabbitsGraph()
    axcolor = 'white'

    rax = plt.axes([0.025, 0.7, 0.18, 0.15], axisbg=axcolor)
    radio = CheckButtons(rax, ('Foxes', 'Rabbits'), [True, True])
    radio.on_clicked(updateLineType)



    ax.grid(True)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    plt.show()


inputRequestWindowLabel = Label(selectionFrame, text = "Enter Initial Values:", pady = 10, padx = 15)
initialXLabel = Label(inputFrame, text = "x:", pady = 5)
initialYLabel = Label(inputFrame, text = "y:", pady = 5)
rateALabel = Label(inputFrame, text = "rateA:", pady = 5)
rateBLabel = Label(inputFrame, text = "rateB:", pady = 5)
rateCLabel = Label(inputFrame, text = "rateC:", pady = 5)
rateDLabel = Label(inputFrame, text = "rateD:", pady = 5)
rateAEntry = Entry(inputFrame, textvariable = rateA)
rateBEntry = Entry(inputFrame, textvariable = rateB)
rateCEntry = Entry(inputFrame, textvariable = rateC)
rateDEntry = Entry(inputFrame, textvariable = rateD)
initialXEntry = Entry(inputFrame, textvariable = initialX)
initialYEntry = Entry(inputFrame, textvariable = initialY)

goButton = Button(inputFrame, text = "Go!", command = graphIt)

inputRequestWindowLabel.grid(row = 0, columnspan = 2)
selectionFrame.pack()

initialXLabel.grid(row = 0, column = 0)
initialYLabel.grid(row = 1, column = 0)
initialXEntry.grid(row = 0, column = 1)
initialYEntry.grid(row = 1, column = 1)
rateALabel.grid(row = 2, column = 0)
rateBLabel.grid(row = 3, column = 0)
rateCLabel.grid(row = 4, column = 0)
rateDLabel.grid(row = 5, column = 0)


rateAEntry.grid(row = 2, column = 1)
rateBEntry.grid(row = 3, column = 1)
rateCEntry.grid(row = 4, column = 1)
rateDEntry.grid(row = 5, column = 1)
goButton.grid(row = 6, columnspan = 2)
inputFrame.pack()

root.mainloop()    


