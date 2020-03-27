#Christopher Marotta
#March 27, 2019
#MathPlotLib Widgets

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def f(x):
    return x**2

def updateLineWidth(val):
    lw = xSize.val
    l.set_linewidth(lw)
    m.set_linewidth(lw)
    n.set_linewidth(lw)
    fig.canvas.draw_idle()
    return

def updateLineType(val):
    l.set_linestyle(val)
    m.set_linestyle(val)
    n.set_linestyle(val)
    fig.canvas.draw_idle()
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

#Setting up for x
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
a = 0
b = 4
n = 101
lw = 2
#Displaying f(x).
xNormal = np.linspace(a,b,n)
yNormal = f(xNormal)
l, = ax.plot(xNormal, yNormal, lw = lw)

#plt.plot(xNormal, yNormal)

#Displaying the antiderivative.
xAntiderivative = np.linspace(a, b, n)
yAntiderivative = f(xAntiderivative)
RSMain = Riemann(a, b, yAntiderivative, (n))
m, = ax.plot(xAntiderivative, RSMain, lw = lw)

#Displaying the derivative.
dx = (b-a)/(n-1)
xDerivative = np.linspace(a,b,n)
yDerivativeTmp = f(xDerivative)
yDerivative = np.diff(yDerivativeTmp)/dx
n, = ax.plot(xDerivative[:-1], yDerivative, lw = lw)


axcolor = 'white'
axSize = plt.axes([0.20, 0.1, 0.65, 0.03], axisbg=axcolor)
xSize = Slider(axSize, 'Line Width', 1, 10, valinit=lw)
xSize.on_changed(updateLineWidth)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('solid', 'dashed', 'dashdot', 'dotted'), active=0)
radio.on_clicked(updateLineType)

ax.legend(["f(x) = x^2", "F(x) = (x^3)/3", "f'(x) = 2*x"], loc = "upper right")

ax.grid(True)
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)
plt.show()
