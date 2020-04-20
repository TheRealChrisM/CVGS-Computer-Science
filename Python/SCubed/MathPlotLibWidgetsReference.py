#Christopher Marotta
#March 27, 2019
#MathPlotLib Widgets

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

lineType = 1
rateIncrease = 1.001

#Setting up for x
fig, ax = plt.subplots()
ax.set_title("H1N1 Infection Status")
ax.set_xlabel("Time")
ax.set_ylabel("People")
plt.subplots_adjust(left=0.25, bottom=0.25)
a = 0
b = 4
n = 101
aRate = 25*(10**-5)
bRate = .1
gRate = 1/6
dRate = 1/6
deltaTime = .01

def f(x):
    return x**2

def s(n):
    for x in n: 
        if x>0:
            return (s(n-1))-(aRate*s(n-1)*i(n-1)*deltaTime)
        else:
            return 18223

def r(n):
    if n>0:
        return ((r(n-1))+(dRate*i(n-1))+(gRate*q(n-1)*deltaTime))
    else:
        return 0
def i(n):
    if n>0:
        return ((i(n-1))+(aRate*s(n-1)*i(n-1))-(bRate*i(n-1))-(dRate*i(n-1)*deltaTime))
    else:
        return 11
def q(n):
    if n>0:
        return ((q(n-1))+(bRate*i(n-1))-(gRate*q(n-1)*deltaTime))
    else:
        return 0
    
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
    return

def updateLines():
    #Reset graph and set limits on axes.
    ax.cla()
    ax.set_xlim([0, 4])
    ax.set_ylim([0, 25])
    
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

def Riemann(a, b, yIn, n):
    deltax = (b-a)/n
    area = np.zeros(n)
    for i in range(1, n+1):
        if i > 1:
            area[i-1] = yIn[i-1]*deltax+area[i-2]
        else:
            area[i-1] = yIn[i-1]*deltax
    return area

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
    yControl = s(xControl)
    #control, = ax.plot(xControl, yControl)
    print(xControl)
    print(yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimentalTmp = f(xExperimental)
    yExperimental = Riemann(a, b, yExperimentalTmp, (n))
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
    yControl = f(xControl)
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimentalTmp = f(xExperimental)
    yExperimental = Riemann(a, b, yExperimentalTmp, (n))
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
    yControl = f(xControl)
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimentalTmp = f(xExperimental)
    yExperimental = Riemann(a, b, yExperimentalTmp, (n))
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
    yControl = f(xControl)
    control, = ax.plot(xControl, yControl)

    #Displaying the experimental group.
    xExperimental = np.linspace(a, b, n)
    yExperimentalTmp = f(xExperimental)
    yExperimental = Riemann(a, b, yExperimentalTmp, (n))
    experimental, = ax.plot(xExperimental, yExperimental)

    #Displaying the difference between the two equations.
    xDifference = np.linspace(a,b,n)
    yDifference = []
    for i in range(len(xControl)):
        yDifference.append(abs(yExperimental[i] - yControl[i]))
    difference, = ax.plot(xDifference, yDifference)
    ax.legend([control,experimental,difference], ['Control','Experimental', 'Difference'])
  
susceptibleGraph()

axcolor = 'white'
axSize = plt.axes([0.20, 0.1, 0.65, 0.03], axisbg=axcolor)
xSize = Slider(axSize, 'Rate Increasing', 0, 2, valinit=rateIncrease)
xSize.on_changed(updateRate)

rax = plt.axes([0.025, 0.7, 0.18, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('Susceptible', 'Quarantined', 'Infected', 'Recovered'), active=0)
radio.on_clicked(updateLineType)

ax.grid(True)
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)
plt.show()
