from tkinter import * # Import tkinter

def display():
    canvas.delete("line")
    #p1 = [width / 2, 10]
    #p2 = [10, height - 10]
    #p3 = [width - 10, height - 10]
    
    centerPoint = [(width/2), (height/2)]
    displayH(int(order.get()), centerPoint)

def displayH(order, center):
    p1 = [((center[0])+(center[0]/(order+7))), center[1]]
    p2 = [((center[0])-(center[0]/(order+7))), center[1]]
    p3 = [(center[0]+(center[0]/(order+7))), (center[1]+(center[1]/(order+7)))]
    p4 = [(center[0]+(center[0]/(order+7))), (center[1]-(center[1]/(order+7)))]
    p5 = [(center[0]-(center[0]/(order+7))), (center[1]+(center[1]/(order+7)))]
    p6 = [(center[0]-(center[0]/(order+7))), (center[1]-(center[1]/(order+7)))]
    
    drawLine(p1, p2)
    print(p1,p2)
    drawLine(p3, p4)
    print(p3,p4)
    drawLine(p5, p6)
    print(p5,p6)
    #else:
    if (order > 0):    
        displayH(order - 1, p5)
        displayH(order - 1, p6)
        displayH(order - 1, p3)
        displayH(order - 1, p4)
    return

def drawLine(p1, p2):
    canvas.create_line(
        p1[0], p1[1], p2[0], p2[1], tags = "line")
    
# Return the midpoint between two points
def midpoint(p1, p2):
    p = 2 * [0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p   

window = Tk() # Create a window
window.title("Sierpinski Triangle") # Set a title

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
Button(frame1, text = "Display Sierpinski Triangle", command = display).pack(side = LEFT)

window.mainloop() # Create an event loop
        
