#Christopher Marotta
#April 8th, 2020
#Assignment: S-Cubed A2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def f(x,y):
    return ((3*x)-(2*y))

def killit():
    plt.close()
    return

def updateLineType(valC):
    newColor = valC
    l.set_c(newColor)
    fig.canvas.draw_idle()
    return


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)


def drawLine(val):
    global l
    
    h = .05
    a = 0
    b = 4
    n = (b-a)/h

    initX = 0
    initY = 0

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
    l, = ax.plot(xVals,yVals)
    plt.show()
    return

def newLine(val):
    h = .05
    a = 0
    b = 4
    n = (b-a)/h

    initX = 0
    initY = val

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
    l.set_ydata(yVals)
    l.set_xdata(xVals)
    return
    
plt.title("S-Cubed A3 Assignment")
plt.xlabel('x')
plt.ylabel('y')

    
axcolor = 'white'    
rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('blue', 'black', 'red'), active=0)
radio.on_clicked(updateLineType)

axcolor = 'white'
axSize = plt.axes([0.20, 0.1, 0.65, 0.03], axisbg=axcolor)
xSize = Slider(axSize, 'Line Width', 0, 5, valinit=0)
xSize.on_changed(newLine)

drawLine(3)


