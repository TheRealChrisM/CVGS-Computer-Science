from tkinter import *

class GUI:
    def __init__(self, title):
        self.__window = Tk()
        self.__window.title(title)
        #sets a new window size in pixels
        self.__window.geometry("300x300")    
        return

    def getWindow(self):
        return self.__window

    def setWindowTitle(self, newTitle):
        self.getWindow().title(newTitle)
        return

def buttonOneProcess():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame2.pack()
    frame4.pack()
    frame3.pack()
    return



window = GUI("This is the title of a Tkinter Window")

#creates a frame
frame1 = Frame(window.getWindow())

#Sets a label into the frame1
greetingLabel = Label(frame1, text = "This is text within a Tkinter window in a frame")
greetingLabel.pack()


#sets another label which is set into a grid
frame2 = Frame(window.getWindow())
anotherlabel = Label(frame2, text="This is text within a grid frame.")
motivationalExample = Label(frame2, text="//TODO: Find motivation")
anotherlabel.grid(row = 0, column = 0)
motivationalExample.grid(row = 0, column = 1)

#makes a button frame
frame3 = Frame(window.getWindow())
buttonThing = Button(frame3, text = "Click MEEEEEE", command = buttonOneProcess)
buttonThing.grid()

#makes a frame for the button press
frame4 = Frame(window.getWindow())
specialButtonLabel = Label(frame4, text="OH NO!!! You pressed the button!!!! AHHHHH")
specialButtonLabel.grid()

#This packs the frames
frame1.pack()
frame2.pack()
frame3.pack()

window.getWindow().mainloop()
