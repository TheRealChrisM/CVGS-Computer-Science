#Christopher Marotta
#March 27, 2019
#MathPlotLib Widgets

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

lineType = 1
rateIncrease = 1.00

#Setting up for x
fig, ax = plt.subplots()
ax.set_title("H1N1 Infection Status")
ax.set_xlabel("Time")
ax.set_ylabel("People")
plt.subplots_adjust(left=0.25, bottom=0.25)
a = 0
deltaTime = .01
n = 10000
b = n*deltaTime
aRate = 25*(10**-5)
bRate = .1
gRate = 1/6
dRate = 1/6

sA = np.zeros(n)
rA = np.zeros(n)
iA = np.zeros(n)
qA = np.zeros(n)
sAExp = np.zeros(n)
rAExp = np.zeros(n)
iAExp = np.zeros(n)
qAExp = np.zeros(n)

def euler():
    sA[0] = 18223
    rA[0] = 0
    iA[0] = 11
    qA[0] = 0
    for x in range(1, n):
        rA[x] = rA[x-1] + deltaTime * recoveredEquation(iA[x-1], qA[x-1])
        qA[x] = qA[x-1] + deltaTime * quarentinedEquation(iA[x-1], qA[x-1])
        sA[x] = sA[x-1] + deltaTime * susceptibleEquation(sA[x-1], iA[x-1])
        iA[x] = iA[x-1] + deltaTime * infectionEquation(sA[x-1], iA[x-1])
    eulerExperimental()

def eulerExperimental():
    sAExp[0] = 18223
    rAExp[0] = 0
    iAExp[0] = 11
    qAExp[0] = 0
    expBRate = bRate
    for x in range(1,n):
        rAExp[x] = rAExp[x-1] + deltaTime * recoveredEquation(iAExp[x-1], qAExp[x-1])
        qAExp[x] = qAExp[x-1] + deltaTime * quarentinedEquationExperimental(iAExp[x-1], qAExp[x-1], expBRate)
        sAExp[x] = sAExp[x-1] + deltaTime * susceptibleEquation(sAExp[x-1], iAExp[x-1])
        iAExp[x] = iAExp[x-1] + deltaTime * infectionEquationExperimental(sAExp[x-1], iAExp[x-1], expBRate)
        if expBRate < 1:
            expBRate = expBRate*rateIncrease
        else:
            expBRate = 1

def susceptibleEquation(sIn,iIn):
    return ((-1*aRate)*(sIn*iIn))

def quarentinedEquation(iIn, qIn):
    return ((bRate*iIn)-(gRate*qIn))

def quarentinedEquationExperimental(iIn, qIn, bIn):
    return ((bIn*iIn)-(gRate*qIn))

def infectionEquation(sIn, iIn):
    return ((aRate*sIn*iIn)-(bRate*iIn)-(dRate*iIn))

def infectionEquationExperimental(sIn, iIn, bIn):
    return ((aRate*sIn*iIn)-(bIn*iIn)-(dRate*iIn))

def recoveredEquation(iIn, qIn):
    return ((dRate*iIn)+(gRate*qIn))
    
def updateRate(val):
    global rateIncrease
    rateIncrease = val
    updateLines()
    return

def updateLineType(val):
    global lineType
    if (val == "Susceptible"):
        lineType = 1
    elif (val == "Quarantined"):
        lineType = 2
    elif (val == "Infected"):
        lineType = 3
    elif (val == "Recovered"):
        lineType = 4
    updateLines()
    updateLines()
    return

def updateLines():
    #Reset graph and set limits on axes.
    ax.cla()
    ax.set_ylim([0,20000])
    ax.set_xlim([0,100])
    euler()
    
    fig.canvas.draw_idle()
    if (lineType == 1):
        susceptibleGraph()
    elif (lineType == 2):
        quarantinedGraph()
    elif (lineType == 3):
        infectedGraph()
    elif (lineType == 4):
        recoveredGraph()
    return

def susceptibleGraph():
    global control, experimental, difference
    #Setting up subplot.
    ax.grid(True)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    ax.set_title("H1N1 Infection Status [Susceptible]")
    ax.set_xlabel("Time")
    ax.set_ylabel("People")
    
    #Displaying the control group.
    xControl = np.linspace(a,b,n)
    yControl = sA
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimental = sAExp
    experimental, = ax.plot(xExperimental, yExperimental)

    #Displaying the difference between the two equations.
    xDifference = np.linspace(a,b,n)
    yDifference = []
    for i in range(len(xControl)):
        yDifference.append(abs(yExperimental[i] - yControl[i]))
    difference, = ax.plot(xDifference, yDifference)
    ax.legend([control,experimental,difference], ['Control','Experimental', 'Difference'])
    
def quarantinedGraph():
    global control, experimental, difference
    #Setting up subplot.
    ax.grid(True)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    ax.set_title("H1N1 Infection Status [Quarantined]")
    ax.set_xlabel("Time")
    ax.set_ylabel("People")
    
    #Displaying the control group.
    xControl = np.linspace(a,b,n)
    yControl = qA
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimental = qAExp
    experimental, = ax.plot(xExperimental, yExperimental)

    #Displaying the difference between the two equations.
    xDifference = np.linspace(a,b,n)
    yDifference = []
    for i in range(len(xControl)):
        yDifference.append(abs(yExperimental[i] - yControl[i]))
    difference, = ax.plot(xDifference, yDifference)
    ax.legend([control,experimental,difference], ['Control','Experimental', 'Difference'])

def infectedGraph():
    global control, experimental, difference
    #Setting up subplot.
    ax.grid(True)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    ax.set_title("H1N1 Infection Status [Infected]")
    ax.set_xlabel("Time")
    ax.set_ylabel("People")
    
    #Displaying the control group.
    xControl = np.linspace(a,b,n)
    yControl = iA
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimental = iAExp
    experimental, = ax.plot(xExperimental, yExperimental)

    #Displaying the difference between the two equations.
    xDifference = np.linspace(a,b,n)
    yDifference = []
    for i in range(len(xControl)):
        yDifference.append(abs(yExperimental[i] - yControl[i]))
    difference, = ax.plot(xDifference, yDifference)
    ax.legend([control,experimental,difference], ['Control','Experimental', 'Difference'])
    
def recoveredGraph():
    global control, experimental, difference
    #Setting up subplot.
    ax.grid(True)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    ax.set_title("H1N1 Infection Status [Recovered]")
    ax.set_xlabel("Time")
    ax.set_ylabel("People")
    
    #Displaying the control group.
    xControl = np.linspace(a,b,n)
    yControl = rA
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimental = rAExp
    experimental, = ax.plot(xExperimental, yExperimental)

    #Displaying the difference between the two equations.
    xDifference = np.linspace(a,b,n)
    yDifference = []
    for i in range(len(xControl)):
        yDifference.append(abs(yExperimental[i] - yControl[i]))
    difference, = ax.plot(xDifference, yDifference)
    ax.legend([control,experimental,difference], ['Control','Experimental', 'Difference'])

euler()
susceptibleGraph()

axcolor = 'white'
axSize = plt.axes([0.20, 0.1, 0.65, 0.03], axisbg=axcolor)
xSize = Slider(axSize, 'Rate Increasing', 0.95, 1.05, valinit=rateIncrease)
xSize.on_changed(updateRate)

rax = plt.axes([0.025, 0.7, 0.18, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('Susceptible', 'Quarantined', 'Infected', 'Recovered'), active=0)
radio.on_clicked(updateLineType)



ax.grid(True)
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)
plt.show()
