import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def f(x, theta, v, y0):
    return (x*np.tan(theta))-((9.8 * (x**2))/((2* (v**2))*(np.cos(theta)**2))) + y0


def killit():
    plt.close()
    return

def graphit():
    global c_coef
    a = 0
    b = 15
    n = 50
   
    x = np.linspace(a,b,n)
    y = f(x,np.radians(c_coef.get()),a_coef.get(),b_coef.get())
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Trajectory'])
    plt.axis([-15,15,0,10])
    plt.title('My first plot using entry boxes')
    plt.grid(True)
    plt.axhline(0, color='black', lw=2)
    plt.axvline(0, color='black', lw=2)
    plt.show()
   


root = tk.Tk()
f1 = tk.Frame(root)
#Assign coefficient variables
a_coef = tk.IntVar()
a_coef.set(1)
b_coef = tk.IntVar()
b_coef.set(0)
c_coef = tk.IntVar()
c_coef.set(0)
#define labels
alabel = tk.Label(f1, text = 'Enter starting velocity:')
blabel = tk.Label(f1, text = 'Enter starting height:')
clabel = tk.Label(f1, text = 'Enter theta angle:')

#define entry boxes
aentry = tk.Entry(f1, textvariable = a_coef)
bentry = tk.Entry(f1, textvariable = b_coef)
centry = tk.Entry(f1, textvariable = c_coef)
#gris widgets in frame
alabel.grid(row = 1, column = 1)
blabel.grid(row = 2, column = 1)
clabel.grid(row = 3, column = 1)
aentry.grid(row = 1, column = 2)
bentry.grid(row = 2, column = 2)
centry.grid(row = 3, column = 2)
#pack widgets in root window
f1.pack()
button1=tk.Button(root, text='Graph It', command=graphit)
button2 = tk.Button(root, text = 'Kill Graph Window', command = killit)
button1.pack()
button2.pack()


plt.show
root.mainloop()
