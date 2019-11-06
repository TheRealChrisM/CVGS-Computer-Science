#Canvas Demo by Mr. Howard
from tkinter import * # Import tkinter

# Display a rectangle
def displayRect():
    canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
    return
    
# Display an oval
def displayOval():
    canvas.create_oval(10, 10, 190, 90, fill = "red",
                       tags = "oval")
    return

# Display an arc
def displayArc():
    canvas.create_arc(10, 10, 190, 90, start = 0,
                      extent = 90, width = 8, fill = "red", tags = "arc")
    return

# Display a polygon
def displayPolygon():
    canvas.create_polygon(10, 10, 190, 90, 30, 50,
                          tags = "polygon")
    return

# Display a line
def displayLine():
    canvas.create_line(10, 10, 190, 90, fill = "red",
                       tags = "line")
    canvas.create_line(10, 90, 190, 10, width = 9,
                       arrow = "last", activefill = "blue", tags = "line")
    return

# Display a string
def displayString():
    canvas.create_text(60, 40, text = "Hi, I am a string",
                       font = "Times 10 bold underline", tags = "string")
    return

# Clear drawings
def clearCanvas():
    canvas.delete("rect", "oval", "arc", "polygon", "line", "string")
    return
    
window = Tk() # Create a window
window.title("Canvas Demo") # Set title

# Place canvas in the window
canvas = Canvas(window, width = 200, height = 100, bg = "white")
canvas.pack()

# Place buttons in frame
frame1 = Frame(window)

btRectangle = Button(frame1, text = "Rectangle", command = displayRect)
btOval = Button(frame1, text = "Oval", command = displayOval)
btArc = Button(frame1, text = "Arc", command = displayArc)
btPolygon = Button(frame1, text = "Polygon", command = displayPolygon)
btLine = Button(frame1, text = "Line", command = displayLine)
btString = Button(frame1, text = "String", command = displayString)
btClear = Button(frame1, text = "Clear", command = clearCanvas)

#Grid Widgets in frame1
btRectangle.grid(row = 1, column = 1)
btOval.grid(row = 1, column = 2)
btArc.grid(row = 1, column = 3)
btPolygon.grid(row = 1, column = 4)
btLine.grid(row = 1, column = 5)
btString.grid(row = 1, column = 6)
btClear.grid(row = 1, column = 7)

#Pack frame1 in main window
frame1.pack()

window.mainloop() # Create an event loop



 
