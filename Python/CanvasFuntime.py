#Christopher Marotta
#November 7th, 2019
#Create a yeild sign and a puzzle/

from tkinter import *


window = Tk()
window.title("Interactive Canvas")

canvasWidth = 1080
canvasHeight = 720

def draw(newX1, newY1, newX2, newY2, newX3, newY3, objectToMove):
    canvas.coords(objectToMove, newX1, newY1, newX2, newY2, newX3, newY3)
    return

def movePieceOne(event):
    draw((event.x-150), (event.y-75), (event.x+25), (event.y), (event.x+50), (event.y+75), puzzlePieceOne)
    return

def movePieceTwo(event):
    draw((event.x+15), (event.y-75), (event.x-10), (event.y), (event.x+15), (event.y+75), puzzlePieceTwo)
    return

def movePieceThree(event):
    draw((event.x-100), (event.y-25), (event.x+75), (event.y+50), (event.x+100), (event.y-25), puzzlePieceThree)
    return

def animate():
    canvas.itemconfigure(yieldLight, fill = "white")
    canvas.after(500, backToLit)
    return

def backToLit():
    canvas.itemconfigure(yieldLight, fill = "yellow")
    window.after(500, animate)
    return

canvas = Canvas(window, width = canvasWidth, height = canvasHeight, bg = "white")
canvas.pack()

#create sign post
yieldPost = canvas.create_rectangle(145,360,155,460, fill = "black", tags="sign")
yieldTriangle = canvas.create_polygon(150,350,250,200,50,200, fill = "white", outline = "red", width = 25, tags="sign")
yieldText = canvas.create_text(150,250, text="YIELD", font="Times 20 bold", tags="sign", anchor="center")
yieldLight = canvas.create_oval(125,140,175,190, fill = "yellow", tags="sign")

#create puzzle
#P1: 0,0,175,75,200,150
#P2: 200,0,175,75,200,150
#P3: 0,0,175,75,200,0
puzzleOutline = canvas.create_polygon(500,400,700,550,700,400, outline = "black", width = 2, fill = "")
puzzlePieceOne = canvas.create_polygon(341,465,516,540,541,615,fill = "red")
puzzlePieceTwo = canvas.create_polygon(984,59,959,134,984,209,fill = "blue")
puzzlePieceThree = canvas.create_polygon(337,91,512,166,537,91,fill = "orange")

canvas.tag_bind(puzzlePieceOne, "<B1-Motion>", movePieceOne)
canvas.tag_bind(puzzlePieceTwo, "<B1-Motion>", movePieceTwo)
canvas.tag_bind(puzzlePieceThree, "<B1-Motion>", movePieceThree)

animate()
window.mainloop()
