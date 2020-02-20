#Christopher Marotta
#November 4th, 2019
#Smiley Face (Animate a smiley face with 2 eyes, a mouth, nose)

from tkinter import *
import time

window = Tk()
window.title("Smiley Smiles")

canvasWidth = 400
canvasHeight = 300
gameScore = 0

def animate():
    global startX, startY, endX, endY, changeX, changeY
    startX += changeX
    startY += changeY
    endX += changeX
    endY += changeY
    if(endX+2) >= canvasWidth or startX <=(0+2):
        changeX = -changeX
    if (endY+2) >= canvasHeight or startY <=(0+2):
        changeY = -changeY
    canvas.move("face", changeX, changeY)
    window.after(15, animate)
    
def backToYellow():
    canvas.itemconfigure(head, fill="yellow")
    
def processFaceClick(event):
    global gameScore
    canvas.itemconfigure(head, fill="red")
    gameScore += 1
    scoreString = "Score: " + str(gameScore)
    canvas.delete("score")
    canvas.create_text(10,15,text = scoreString, font = "Times 10 bold underline", tag="score", anchor="w")
    canvas.after(100, backToYellow)

def beginFaceGame(event):
    global head, leftEye, rightEye, mouth, nose
    animate()
    canvas.delete("beginGame")
    #create face
    head = canvas.create_oval(startX, startY, endX, endY, fill = "yellow", tags = "face")
    #create eyes
    leftEye = canvas.create_oval((startX+15), (startY+15), (startX+20), (startY+20), fill = "black", tags="face")
    rightEye = canvas.create_oval((endX-15), (startY+15), (endX-20), (startY+20), fill = "black", tags="face")
    #create mouth
    mouth = canvas.create_arc((startX+15), (endY-10), (endX-15), (endY-30), start = 180, extent = 180, fill = "black", tags="face")
    #create nose
    nose = canvas.create_rectangle((startX+25),(startY+20), (endX-25), (endY-25), fill="black", tags="face")
    #Create Score Counter
    score = canvas.create_text(10,15,text = "Score: 0", font = "Times 10 bold underline", tag="score", anchor="w")
    canvas.unbind("<Button-3",beginGameFuncID)
canvas = Canvas(window, width = canvasWidth, height = canvasHeight, bg = "white")
canvas.pack()

startX = 50
startY = 50
endX = 100
endY = 100
changeX = 2
changeY = -2
head = None
leftEye = None
rightEye = None
mouth = None
nose = None
score = None
#begin game message
beginGame = canvas.create_text(200,150,text="Right Click to Begin Game!", font="Times 20 bold underline", tag="beginGame", anchor="center")
beginGameFuncID = canvas.bind("<Button-3>", beginFaceGame)
canvas.tag_bind("face", "<Button-1>", processFaceClick)



window.mainloop()

