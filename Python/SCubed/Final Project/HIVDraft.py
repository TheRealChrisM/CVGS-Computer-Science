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
ax.set_title("HIV Infection Status")
ax.set_xlabel("Time")
ax.set_ylabel("Cells")
plt.subplots_adjust(left=0.30, right=0.95, bottom=0.25)

#Setting various rates and known values to be used later.
a = 0
deltaTime = .01
n = 10000
b = n*deltaTime
lambdaRate = .1089
muRate = .01089
kRate = (1.179)*(10**-3)
deltaRate = .3660
pRate = (1.427)*(10**3)
cRate = 3

#Creates arrays for the equations to use in the models for the control and experimental datasets.
healthyArray = np.zeros(n)
infectedArray = np.zeros(n)
virusParticleArray = np.zeros(n)
healthyArrayExp = np.zeros(n)
infectedArrayExp = np.zeros(n)
virusParticleArrayExp = np.zeros(n)

#Applies euler's method to the control equations.
def euler():
    #Sets up initial values for the arrays.
    healthyArray[0] = 500
    infectedArray[0] = 0
    virusParticleArray[0] = (10**-3)
    #Begins actually applying Euler's method through a for loop.
    for x in range(1, n):
        healthyArray[x] = healthyArray[x-1] + deltaTime * healthyEquation(healthyArray[x-1], virusParticleArray[x-1])
        infectedArray[x] = infectedArray[x-1] + deltaTime * infectedEquation(healthyArray[x-1], virusParticleArray[x-1], infectedArray[x-1])
        virusParticleArray[x] = virusParticleArray[x-1] + deltaTime * virusParticleEquation(infectedArray[x-1], virusParticleArray[x-1])
    #Then moves over to calculate the experimental group.
    eulerExperimental()

#Applies eulers method to the experimental equations.
def eulerExperimental():
    #Sets up initial values for the arrays.
    healthyArrayExp[0] = 500
    infectedArrayExp[0] = 0
    virusParticleArrayExp[0] = (10**-3)
    expKRate = kRate
    #Begins actually applying Euler's method through a for loop.
    for x in range(1,n):
        healthyArrayExp[x] = healthyArrayExp[x-1] + deltaTime * healthyEquationExperimental(healthyArrayExp[x-1], virusParticleArrayExp[x-1], expKRate)
        infectedArrayExp[x] = infectedArrayExp[x-1] + deltaTime * infectedEquationExperimental(healthyArrayExp[x-1], virusParticleArrayExp[x-1], infectedArrayExp[x-1], expKRate)
        virusParticleArrayExp[x] = virusParticleArrayExp[x-1] + deltaTime * virusParticleEquation(infectedArrayExp[x-1], virusParticleArrayExp[x-1])
        #Checks to see if the increasing rate of quarentining is less than 100%.
        if expKRate < 1:
            expKRate = expKRate*rateIncrease
        #If the increasing rate of quarentining is over 100% set it to 100%.
        else:
            expKRate = 1

def healthyEquation(tIn, vIn):
    return ((lambdaRate) - (muRate*tIn) - (kRate*tIn*vIn))

def infectedEquation(tIn, vIn, iIn):
    return ((kRate*tIn*vIn) - (deltaRate*iIn))

def virusParticleEquation(iIn, vIn):
    return ((pRate*iIn)-(cRate*vIn))

def healthyEquationExperimental(tIn, vIn, expRate):
    return ((lambdaRate) - (muRate*tIn) - ((kRate*expRate)*tIn*vIn))

def infectedEquationExperimental(tIn, vIn, iIn, expRate):
    return (((kRate*expRate)*tIn*vIn) - (deltaRate*iIn))

#Updates the rate at which rate of quarentining increases and runs a function to update the graph.
def updateRate(val):
    global rateIncrease
    rateIncrease = val
    updateLines()
    return

#Changes the group that is displayed on the graph, then begins the process to update the graph.
def updateLineType(val):
    global lineType
    if (val == "Healthy"):
        lineType = 1
    elif (val == "Infected"):
        lineType = 2
    elif (val == "Virus Particles"):
        lineType = 3
    updateLines()
    return

#Clears the graph, recalculates the arrays, then displays the correct group.
def updateLines():
    #Reset graph and set limits on axes.
    ax.cla()
    #ax.set_ylim([0,20000])
    ax.set_xlim([0,100])
    euler()
    
    fig.canvas.draw_idle()
    if (lineType == 1):
        healthyCellsGraph()
    elif (lineType == 2):
        infectedCellsGraph()
    elif (lineType == 3):
        virusParticleGraph()
    return

#Displays the susceptible group on the graph.
def healthyCellsGraph():
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
    yControl = healthyArray
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimental = healthyArrayExp
    experimental, = ax.plot(xExperimental, yExperimental)

    #Displaying the difference between the two equations.
    xDifference = np.linspace(a,b,n)
    yDifference = []
    for i in range(len(xControl)):
        yDifference.append(abs(yExperimental[i] - yControl[i]))
    difference, = ax.plot(xDifference, yDifference)
    ax.legend([control,experimental,difference], ['Control','Experimental', 'Difference'])

#Displays the quarentined group on the graph.
def infectedCellsGraph():
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
    yControl = infectedArray
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimental = infectedArrayExp
    experimental, = ax.plot(xExperimental, yExperimental)

    #Displaying the difference between the two equations.
    xDifference = np.linspace(a,b,n)
    yDifference = []
    for i in range(len(xControl)):
        yDifference.append(abs(yExperimental[i] - yControl[i]))
    difference, = ax.plot(xDifference, yDifference)
    ax.legend([control,experimental,difference], ['Control','Experimental', 'Difference'])

#Displays the infected group on the graph.
def virusParticleGraph():
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
    yControl = virusParticleArray
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimental = virusParticleArrayExp
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
healthyCellsGraph()

#Sets up the widget color.
axcolor = 'white'

#Sets up the slider widget.
axSize = plt.axes([0.20, 0.1, 0.65, 0.03], axisbg=axcolor)
xSize = Slider(axSize, 'Rate Increasing', 0.95, 1.05, valinit=rateIncrease)
xSize.on_changed(updateRate)

#Sets up the radiobutton widget.
rax = plt.axes([0.025, 0.7, 0.20, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('Healthy', 'Infected', 'Virus Particles'), active=0)
radio.on_clicked(updateLineType)

#Prepares the graph to be displayed.
ax.grid(True)
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)

#Displays the graph.
plt.show()
