from tkinter import *

class GUI:
    def __init__(self, title):
        self.__window = Tk()
        self.__window.title(title)
        #sets a new window size in pixels
        self.__window.geometry("500x300")    
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
    frame5.pack()
    return

def processCheckbutton():
    if v1.get() == 1:
        result = "Checked"
    else:
        result = "Unchecked"
    print("Check button is" + result)
    return

def processRadioButton():
    if v2.get() == 1:
        result = "Red"
    else:
        result = "Yellow"
    print(result + " is selected.")
    return

def processButton():
    print("Your name is", name.get())
    return

window = GUI("This is the title of a Tkinter Window")

#creates a frame
frame1 = Frame(window.getWindow())

#Sets a label into the frame1
greetingLabel = Label(frame1, text = "This is text within a Tkinter window in a frame")
greetingLabel.grid(row = 1, column = 1)
#IntVar is a class within the TKinter Library, variable of type Integer.
v1 = IntVar()
checkButtonExample = Checkbutton(frame1, text="Bold", variable = v1, command = processCheckbutton)
v2 = IntVar()
rbRed = Radiobutton(frame1, text="Red", bg = "red", variable = v2, value = 1, command = processRadioButton)
rbYellow = Radiobutton(frame1, text="Yellow", bg="yellow", variable = v2, value = 2, command = processRadioButton)
checkButtonExample.grid(row = 2, column = 1)
rbRed.grid(row = 2, column = 2)
rbYellow.grid(row = 2, column = 3)

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

#creates a frame for strings
frame5 = Frame(window.getWindow()) # Create and add a frame to window
frame5.pack()
label = Label(frame5, text = "Enter your name: ")
name = StringVar()
entryName = Entry(frame5, textvariable = name) 
btGetName = Button(frame5, text = "Get Name", command = processButton)
message = Message(frame5, text = "It is a widgets demo")
label.grid(row = 1, column = 1)
entryName.grid(row = 1, column = 2)
btGetName.grid(row = 1, column = 3)
message.grid(row = 1, column = 4)              

#This packs the frames
frame1.pack()
frame2.pack()
frame3.pack()

window.getWindow().mainloop()
