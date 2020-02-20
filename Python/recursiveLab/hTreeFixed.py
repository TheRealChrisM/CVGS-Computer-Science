from tkinter import * # Import tkinter

def display():
    canvas.delete("line")

    centerPoint = [(width/2), (height/2)]
    
    makeH(int(order.get()), 100, centerPoint[0], centerPoint[1])

def makeH(order, size, x, y):
    if (order == 0):
        return
    x0 = x - size/2
    x1 = x + size/2
    y0 = y - size/2
    y1 = y + size/2

    drawLine(x0, y, x1, y)
    drawLine(x0, y0, x0, y1)
    drawLine(x1, y0, x1, y1)

    makeH(order-1, size/2, x0, y0)
    makeH(order-1, size/2, x0, y1)
    makeH(order-1, size/2, x1, y0)
    makeH(order-1, size/2, x1, y1)
    
def drawLine(p1x, p1y, p2x, p2y):
    canvas.create_line(p1x, p1y, p2x, p2y, tags = "line")
    return
    
# Return the midpoint between two points
def midpoint(p1x, p1y, p2x, p2y):
    p = 2 * [0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p   

window = Tk() # Create a window
window.title("H Tree") # Set a title

width = 400
height = 400
canvas = Canvas(window, width = width, height = height)
canvas.pack()

# Add a label, an entry, and a button to frame1
frame1 = Frame(window) # Create and add a frame to window
frame1.pack()

Label(frame1, text = "Enter an order: ").pack(side = LEFT)
order = StringVar()
entry = Entry(frame1, textvariable = order, justify = RIGHT).pack(side = LEFT)
Button(frame1, text = "Display H Tree", command = display).pack(side = LEFT)

window.mainloop() # Create an event loop
        
