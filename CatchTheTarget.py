#Christopher Marotta
#November 4th, 2019
#Project: Create a "Catch the Ball"-esqe game

#Import the Tkinter library for graphics.
from tkinter import *
#Imports the Random libary to allow for the target to spawn in a random location.
import random

#Sets up a Tkinter window.
window = Tk()
#Sets the title of the Tkinter window to "Target Practice".
window.title("Target Practice")

#Sets the first X coordinate for the Target to 100.
startX = 100
#Sets the first Y coordinate for the Target to 100.
startY = 100
#Sets the second X coordinate for the Target to 200.
endX = 200
#Sets the second Y coordinate for the Target to 200.
endY = 200
#Sets the beginning change for the X-axis to 2.
changeX = 2
#Sets the beginning change for the Y-axis to -2.
changeY = -2
#Sets the variable for the largest ring of the Target.
ringOne = None
#Sets the variable for the second largest ring of the Target.
ringTwo = None
#Sets the variable for the smallest ring of the Target.
ringThree = None
#Sets a placeholder to keep track of the string that represents the binding function for a "misclick".
canvasBind = ""
#Sets the amount of "lives" that a player will start with.
lives = 5
#Sets a placeholder variable for the "Score" label.
score = None
#Sets a placeholder for the variables which will keep track of the X-axis of the target as it shrinks.
xRatio = 0
#Sets a placeholder for the variables which will keep track of the Y-axis of the target as it shrinks.
yRatio = 0

#Sets the width of the game window to 400 pixels.
canvasWidth = 400
#Sets the height of the game window to 300 pixels.
canvasHeight = 300
#Sets the score to zero to prepare for the game to begin.
gameScore = 0

#An animate function which runs every 30ms to move the target around.
def animate():
    #Prepares the global variables so that they can reliably be used between functions.
    global startX, startY, endX, endY, changeX, changeY
    #Checks to see if the target has hit the horizontal sides of the canvas.
    if((endX+abs(changeX)) >= canvasWidth) or (startX-abs(changeX)) <=(0):
        #If one of the sides was hit, the game will switch the horizontal direction of the target.
        changeX = -changeX
    #Checks to see if the target has hit the vertical sides of the canvas.
    if ((endY+abs(changeY)) >= canvasHeight) or (startY-abs(changeY)) <=(0):
        #If one of the sides was hit, the game will switch the vertical direction of the target.
        changeY = -changeY
    #This is the change the target will have in the x direction.
    startX += changeX
    #This is the change the target will have in the y direction.
    startY += changeY
    #This moves the "end" point of the target to it's new location in the x direction.
    endX += changeX
    #This moves the "end" point of the target to it's new location in the y direction.
    endY += changeY
    #This moves the target to it's new location.
    canvas.move("target", changeX, changeY)
    #Runs the animate function again after 30ms.
    window.after(30, animate)
    return

#This function spawns in the target at a random location.
def spawnInTarget():
    #Prepares the global variables so that they can reliably be used between functions.
    global startX, startY, endX, endY, changeX, changeY, randX, randY, xRatio, yRatio, canvasBind
    #Determines the correct sizing of the new target along the X-axis.
    xRatio = ((endX - startX)//4)*3
    #Determines the correct sizing of the new target along the Y-axis.
    yRatio = ((endY - startY)//4)*3
    #Choses a random X-coordinate in the middle area of the canvas.
    randX = random.randint(150, 250)
    #Choses a random Y-coordinate in the middle area of the canvas.
    randY = random.randint(150, 200)
    #Sets the x starting location to the randomly selected number.
    startX = randX
    #Sets the x endpoint based on the x starting location.
    endX = randX + (xRatio)
    #Sets the y starting location to the randomly selected number.
    startY = randY
    #Sets the y endpoint based on the y starting location.
    endY = randY + (yRatio)
    #Runs the function which will actually draw the target on the canvas.
    drawTarget()
    #Sets the speed of the target in the x direction.
    changeX = changeX*1.5
    #Sets the speed of the target in the y direction.
    changeY = changeY*1.5
    #Enables the functionality which causes lives to decrease when the user does not click on the target.
    canvasBind = canvas.bind("<Button-1>", missTarget)
    return
    
#Function which runs when the user clicks on the target.
def processTargetClick(event):
    #Prepares the global variables so that they can reliably be used between functions.
    global gameScore, lives
    #Unbinds the misclick function so that the user does not loose lives when they click "Ok".
    canvas.unbind("<Button-1>", canvasBind)
    #Increases the user's score by one.
    gameScore += 1
    #Sets the lives back to five for the next round.
    lives = 5
    #Checks to see if the user has clicked the target more than two times.
    if (gameScore > 2):
        #If the user has clicked the target more than two times, they are directed to the end screen.
        endTargetGame(True)
    #Run only if the user has not won the game yet, and set up for the next round.
    else:
        #Update the score and lives counter.
        scoreString = "Round: " + str(gameScore) + " | Lives: " + str(lives)
        #Remove the clicked target.
        canvas.delete("target")
        #Remove the old score.
        canvas.delete("score")
        #Place the updated score information on the canvas.
        canvas.create_text(10,15,text = scoreString, font = "Times 10 bold underline", tag="score", anchor="w")
        #Displayh a textbox which informs the user they have successfully clicked on the target.
        messagebox.showinfo(title="Congratulations", message="Congratulations! You hit the target!")
        #After they close the messageBox, wait 100ms then spawn in another target and start the next round.
        canvas.after(100, spawnInTarget)
    return

#This function will draw the target onto the canvas.
def drawTarget():
    #Prepares the global variables so that they can reliably be used between functions.
    global ringOne, ringTwo, ringThree
    #Creates the outer ring of the target.
    ringOne = canvas.create_oval(startX, startY, endX, endY, fill = "red", tags = "target")
    #Creates the middle ring of the target.
    ringTwo = canvas.create_oval(startX+((10/50)*xRatio), startY+((10/50)*yRatio), endX-((10/50)*xRatio), endY-((10/50)*yRatio), fill = "white", tags = "target")
    #Creates the inner ring of the target.
    ringThree = canvas.create_oval(startX+((20/50)*xRatio), startY+((20/50)*yRatio), endX-((20/50)*xRatio), endY-((20/50)*yRatio), fill = "red", tags = "target")
    return

#Function which will process an event where the user misses the target.
def missTarget(event):
    #Prepares the global variables so that they can reliably be used between functions.
    global lives, gameScore, canvasBind
    #Decrease the life count by one.
    lives = lives - 1
    #Create a new score string with updated game information.
    scoreString = "Round: " + str(gameScore) + " | Lives: " + str(lives)
    #Removes the old score label.
    canvas.delete("score")
    #Draws the new and updated score label onto the canvas.
    canvas.create_text(10,15,text = scoreString, font = "Times 10 bold underline", tag="score", anchor="w")
    #Check to see if the user has no more lives remaining.
    if (lives == 0):
        #Unbinds the misclick function so that there are no more functions bound to a click event.
        canvas.unbind("<Button-1>", canvasBind)
        #Moves the user to the end game screen, displaying a loss.
        endTargetGame(False)
    return

#This is the function which will actually start the game after the user right clicks.
def beginTargetGame(event):
    #Prepares the global variable so that it can reliably be used between functions.
    global canvasBind
    #Binds the mouse click outside of the target to the missTarget function saving the string so that can be unbound later.
    canvasBind = canvas.bind("<Button-1>", missTarget)
    #Runs the animation function which will then begin looping.
    animate()
    #Removes the screen instructing the user how to begin the game.
    canvas.delete("beginGame")
    #Spawns in the target.
    spawnInTarget()
    #Creates the scoreboard which will be displayed in the top left side of the screen.
    score = canvas.create_text(10,15,text = "Score: 0 | Lives: 5", font = "Times 10 bold underline", tag="score", anchor="w")
    #Unbinds the click event which begins the game as it is no longer required.
    canvas.unbind("<Button-3",beginGameFuncID)
    return

#Takes in a boolean to determine whether to display a win or loose condition. True = win & False = Loose
def endTargetGame(win):
    #Creates an empty label string which will be filled based on whether the game was won or lost.
    labelString = ""
    #Checks to see if the function input represents a win.
    if win:
        #If the user did win, it will set the labelString to a winning message.
        labelString = "Congratulations! You have completed three \n \t rounds and won the game!"
    #Checks to see if the input to the function represents a loss.
    elif (not win):
        #If the user did loose, it will set the labelString to a loosing message.
        labelString = "Sorry you did not complete three \n              rounds! You loose!"
    #Removes the scoreboard from the canvas.
    canvas.delete("score")
    #Removes the target from the canvas.
    canvas.delete("target")
    #Displays the appropriate labelString on the canvas.
    canvas.create_text(200,150, text = labelString, font = "Times 15 bold", tag = "endGameScreen", anchor="center")
    #After five seconds the window will close.
    canvas.after(5000, window.destroy)
    return

#Creates a canvas with the saved variables from the beginning of the program.
canvas = Canvas(window, width = canvasWidth, height = canvasHeight, bg = "white")
#Packs the canvas into the window which will display it.
canvas.pack()

#Display the message instructing the user on how to begin the game.
beginGame = canvas.create_text(200,150,text="Right Click to Begin Game!", font="Times 20 bold underline", tag="beginGame", anchor="center")
#Binds a "right mouse click" to the function which begins the game, saving the functionID so that it may be unbound when appropriate.
beginGameFuncID = canvas.bind("<Button-3>", beginTargetGame)
#Binds a "left mouse click" when done to the target to a function which processess sucessfully clicking the target.
canvas.tag_bind("target", "<Button-1>", processTargetClick)

#Begins the mainloop which will start up the GUI.
window.mainloop()

