#Christopher Marotta
#March 24, 2019
#Riemann Sum Stuff

import numpy as np
import matplotlib.pyplot as plt

def fOne(x):
    return x**2

def fPartTwoActual(x):
    return ((x**3)/3)

def fPartThreeEstimated(x):
    return((2/(np.sqrt(np.pi)))*(np.exp(-(x)**2)))

def Riemann(a, b, yIn, n):
    deltax = (b-a)/n
    area = np.zeros(n)
    for i in range(1, n+1):
        if i > 1:
            area[i-1] = yIn[i-1]*deltax+area[i-2]
        else:
            area[i-1] = yIn[i-1]*deltax
    return area

def RiemannSummed(a, b, yIn, n):

    deltax = (b-a)/n
    area = np.zeros(n)
    for i in range(1, n+1):
        area[i-1] = yIn[i]*deltax
    
    mysum = area.sum()

    return mysum

aOne = 0
bOne = 2
nOne = 51
xPartOne = np.linspace(aOne, bOne, nOne)
yPartOne = fOne(xPartOne)
RSPartOne = RiemannSummed(aOne, bOne, yPartOne, (nOne-1))
print("The area for part 1 is", RSPartOne)

#Setting up for part two.
aTwo = 0
bTwo = 2
nTwo = 101
#Displaying the actual graph for part two.
xPartTwoActual = np.linspace(aTwo, bTwo, nTwo)
yPartTwoActual = fPartTwoActual(xPartTwoActual)
plt.plot(xPartTwoActual, yPartTwoActual)

#Displaying the estimate for part two.
xPartTwoEstimate = np.linspace(aTwo, bTwo, nTwo)
yPartTwoEstimate = fOne(xPartTwoEstimate)
RSPartTwo = Riemann(aTwo, bTwo, yPartTwoEstimate, (nTwo))
plt.plot(xPartTwoEstimate, RSPartTwo)

#Setting up for part three.
aThree = 0
bThree = 2
nThree = 101
#Displaying the estimated graph for part three.
xPartThreeEstimated = np.linspace(aTwo, bTwo, nTwo)
yPartThreeEstimated = fPartThreeEstimated(xPartThreeEstimated)
RSPartThree = Riemann(aThree, bThree, yPartThreeEstimated, (nThree))
plt.plot(xPartThreeEstimated, RSPartThree)



plt.title("Riemann Sum Lab")
plt.legend(["Part 2 Actual", "Part 2 Estimated", "Part 3 Estimated"])
plt.show()
