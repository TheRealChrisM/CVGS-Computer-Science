#Christopher Marotta, William Adu-Jamfi, Aidan Horton, Clare Cocker, and Lauren Chase
#April 20, 2020
#S-Cubed H1N1 Graph

#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

#Sets default values for MatPlotLib Widgets
lineType = 1
rateIncrease = 1.00

#Setting up the graph.
fig, ax = plt.subplots()
ax.set_title("H1N1 Infection Status")
ax.set_xlabel("Time")
ax.set_ylabel("People")
plt.subplots_adjust(left=0.30, right=0.95, bottom=0.25)

#Setting various rates and known values to be used later.
a = 0
deltaTime = .01
n = 10000
b = n*deltaTime
aRate = 25*(10**-5)
bRate = .1
gRate = 1/6
dRate = 1/6

#Creates arrays for the equations to use in the models for the control and experimental datasets.
sA = np.zeros(n)
rA = np.zeros(n)
iA = np.zeros(n)
qA = np.zeros(n)
sAExp = np.zeros(n)
rAExp = np.zeros(n)
iAExp = np.zeros(n)
qAExp = np.zeros(n)

#Applies euler's method to the control equations.
def euler():
    #Sets up initial values for the arrays.
    sA[0] = 18223
    rA[0] = 0
    iA[0] = 11
    qA[0] = 0
    #Begins actually applying Euler's method through a for loop.
    for x in range(1, n):
        rA[x] = rA[x-1] + deltaTime * recoveredEquation(iA[x-1], qA[x-1])
        qA[x] = qA[x-1] + deltaTime * quarentinedEquation(iA[x-1], qA[x-1])
        sA[x] = sA[x-1] + deltaTime * susceptibleEquation(sA[x-1], iA[x-1])
        iA[x] = iA[x-1] + deltaTime * infectionEquation(sA[x-1], iA[x-1])
    #Then moves over to calculate the experimental group.
    eulerExperimental()

#Applies eulers method to the experimental equations.
def eulerExperimental():
    #Sets up initial values for the arrays.
    sAExp[0] = 18223
    rAExp[0] = 0
    iAExp[0] = 11
    qAExp[0] = 0
    expBRate = bRate
    #Begins actually applying Euler's method through a for loop.
    for x in range(1,n):
        rAExp[x] = rAExp[x-1] + deltaTime * recoveredEquation(iAExp[x-1], qAExp[x-1])
        qAExp[x] = qAExp[x-1] + deltaTime * quarentinedEquationExperimental(iAExp[x-1], qAExp[x-1], expBRate)
        sAExp[x] = sAExp[x-1] + deltaTime * susceptibleEquation(sAExp[x-1], iAExp[x-1])
        iAExp[x] = iAExp[x-1] + deltaTime * infectionEquationExperimental(sAExp[x-1], iAExp[x-1], expBRate)
        #Checks to see if the increasing rate of quarentining is less than 100%.
        if expBRate < 1:
            expBRate = expBRate*rateIncrease
        #If the increasing rate of quarentining is over 100% set it to 100%.
        else:
            expBRate = 1

#Differential equation for the susceptible group.
def susceptibleEquation(sIn,iIn):
    return ((-1*aRate)*(sIn*iIn))

#Differential equation for the quarentined group.
def quarentinedEquation(iIn, qIn):
    return ((bRate*iIn)-(gRate*qIn))

#Differential equation for the quarentined group applying an increasing rate of quarentining.
def quarentinedEquationExperimental(iIn, qIn, bIn):
    return ((bIn*iIn)-(gRate*qIn))

#Differential equation for the infected group.
def infectionEquation(sIn, iIn):
    return ((aRate*sIn*iIn)-(bRate*iIn)-(dRate*iIn))

#Differential equation for the infected group applying an increasing rate of quarentining.
def infectionEquationExperimental(sIn, iIn, bIn):
    return ((aRate*sIn*iIn)-(bIn*iIn)-(dRate*iIn))

#Differential equation for the recovered group.
def recoveredEquation(iIn, qIn):
    return ((dRate*iIn)+(gRate*qIn))

#Updates the rate at which rate of quarentining increases and runs a function to update the graph.
def updateRate(val):
    global rateIncrease
    rateIncrease = val
    updateLines()
    return

#Changes the group that is displayed on the graph, then begins the process to update the graph.
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
    return

#Clears the graph, recalculates the arrays, then displays the correct group.
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

#Displays the susceptible group on the graph.
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

#Displays the quarentined group on the graph.
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

#Displays the infected group on the graph.
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

#Displays the recovered group on the graph.   
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

#Gets everything started by calculating the datasets before anything is graphed.
euler()
#Graphs the susceptible population.
susceptibleGraph()

#Sets up the widget color.
axcolor = 'white'

#Sets up the slider widget.
axSize = plt.axes([0.20, 0.1, 0.65, 0.03], axisbg=axcolor)
xSize = Slider(axSize, 'Rate Increasing', 0.95, 1.05, valinit=rateIncrease)
xSize.on_changed(updateRate)

#Sets up the radiobutton widget.
rax = plt.axes([0.025, 0.7, 0.18, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('Susceptible', 'Quarantined', 'Infected', 'Recovered'), active=0)
radio.on_clicked(updateLineType)

#Prepares the graph to be displayed.
ax.grid(True)
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)

#Displays the graph.
plt.show()
