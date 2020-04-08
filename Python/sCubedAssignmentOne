from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if returnVal.get() == 1:
        returnFunc = (2 - (x**2))
    elif returnVal.get() == 2:
        returnFunc = (np.cos(x))
    elif returnVal.get() == 3:
        returnFunc = ((np.exp(x))-2)
    return returnFunc

def killit():
    plt.close()
    return

def secantLine(xIn, x0In, x1In):
    return ((f(x1In))+((f(x1In)-f(x0In))/(x1In-x0In))*(xIn-x1In))

def locSecantRoot(x0In, x1In):
    return ((x1In)-((f(x1In))*((x1In-x0In)/(f(x1In)-f(x0In)))))

def graphIt():
    killit()
    
    a = -4
    b = 4
    n = 50
    x = np.linspace(a,b,n)
    y = f(x)

    x0 = int(xZeroEntry.get())
    x1 = int(xOneEntry.get())
    x2 = locSecantRoot(x0, x1)
    x3 = locSecantRoot(x1, x2)
    x4 = locSecantRoot(x2, x3)

    secLineOne = secantLine(x, x0, x1)
    secLineTwo = secantLine(x, x1, x2)
    secLineThree = secantLine(x, x2, x3)

    resultLabel["text"] = ("The root approximation = " + str(x4))
    
    plt.plot(x, y)
    plt.plot(x, secLineOne)
    plt.plot(x, secLineTwo)
    plt.plot(x, secLineThree)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['2 - x^2','Secant Line 1', 'Secant Line 2', 'Secant Line 3'])
    plt.axis([-4,4,-15,5])
    plt.title('Secant Method Assignment')
    plt.grid(True)
    plt.axhline(0, color='black', lw=2)
    plt.axvline(0, color='black', lw=2)
    plt.show()

root = Tk()
selectionFrame = Frame(root)
inputFrame = Frame(root)
root.title("Input Window")

xZeroEntry = StringVar()
xOneEntry = StringVar()
returnVal = IntVar()
returnVal.set(1)

inputRequestWindowLabel = Label(selectionFrame, text = "Enter Initial Values:", pady = 10, padx = 15)
funcOneButton = Radiobutton(selectionFrame, text = "f(x) = 2 – x^2", variable = returnVal, value = 1)
funcTwoButton = Radiobutton(selectionFrame, text = "f(x) = cos(x)", variable = returnVal, value = 2)
funcThreeButton = Radiobutton(selectionFrame, text = "f(x) = e^x – 2", variable = returnVal, value = 3)

inputXZeroLabel = Label(inputFrame, text = "x0:", pady = 5)
inputXOneLabel = Label(inputFrame, text = "x1:", pady = 5)
inputXZeroEntry = Entry(inputFrame, textvariable = xZeroEntry)
inputXOneEntry = Entry(inputFrame, textvariable = xOneEntry)
goButton = Button(inputFrame, text = "Go!", command = graphIt)
resultLabel = Label(inputFrame, text = "")

inputRequestWindowLabel.grid(row = 0, columnspan = 2)
funcOneButton.grid(row = 1, column = 0)
funcTwoButton.grid(row = 1, column = 1)
funcThreeButton.grid(row = 1, column = 2)
selectionFrame.pack()

inputXZeroLabel.grid(row = 0, column = 0)
inputXOneLabel.grid(row = 1, column = 0)
inputXZeroEntry.grid(row = 0, column = 1)
inputXOneEntry.grid(row = 1, column = 1)
goButton.grid(row = 2, columnspan = 2)
resultLabel.grid(row = 3, columnspan = 2)
inputFrame.pack()

plt.show
root.mainloop()
