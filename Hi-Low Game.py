#Christopher Marotta
#November 13, 2019
#Lab Assignmnet - Hi-Lo Game
from tkinter import *
from PIL import ImageTk
import random

#setup game
window = Tk()
frame = Frame(window)
cardBackground = ImageTk.PhotoImage(file = "image/card/b1fv.gif")
firstCard = None
secondCard = None
cardOne = IntVar()
cardTwo = IntVar()
cardOne.set(0)
cardTwo.set(0)
selectVar = IntVar()
selectVar.set(0)
#returns a file location of a random card
def randomImage(cardNumVar):
    #global cardDrawn
    cardString = "image/card/"
    cardNum = random.randint(1,52)
    cardString = cardString + str(cardNum)
    cardString = cardString + ".gif"
    cardDrawn = ImageTk.PhotoImage(file = cardString)
    calcCardValue(cardNumVar, cardNum)
    return cardDrawn

#function to be run to calculate the "value" of both cards
def calcCardValue(cardNumVar, cardDrawn):
    cardValue = cardDrawn % 13
    if (cardValue == 0):
        cardValue = 13
    cardNumVar.set(cardValue)
    return
    
#function to be run when the left button is pressed
def drawFirstCard():
    global firstCard
    firstCard = randomImage(cardOne)
    leftButton['image'] = firstCard
    leftButton['state'] = "disabled"
    beginGameLabel.grid_remove()
    promptFrame.grid(row = 0, column = 1)
    rightButton.grid(row = 0, column = 2)
    return

#function to be run when the user wants to draw the second card
def drawSecondCard():
    global secondCard
    secondCard = randomImage(cardTwo)
    rightButton['image'] = secondCard
    rightButton['state'] = "disabled"
    promptFrame.grid_remove()
    endGameLabelString = checkWin()
    endGameLabel['text'] = endGameLabelString
    endGameLabel.grid(row = 0, column = 1)
    endGameButton.grid(row = 1, column = 1)
    return

#Resets the game and allows the player to play again
def playAgain():
    cardOne.set(0)
    cardTwo.set(0)
    selectVar.set(0)
    leftButton['image'] = cardBackground
    leftButton['state'] = "active"
    rightButton['image'] = cardBackground
    rightButton['state'] = "active"
    endGameButton.grid_remove()
    endGameLabel.grid_remove()
    beginGameLabel.grid(row = 0, column = 1)
    rightButton.grid_remove()
    
    return

#after the second card is drawn this will compare the two cards and determine if it was a win, lose, or tie.
def checkWin():
    returnString = ""
    higherSelected = None
    if (selectVar.get() == 1):
        higherSelected = False
    elif (selectVar.get() == 2):
        higherSelected = True
    else:
        higherSelected = False

    if (cardOne.get() > cardTwo.get()) and (not higherSelected):
        returnString = "Yay! You WIN!"
    elif (cardOne.get() > cardTwo.get()) and (higherSelected):
        returnString = "Sorry! You LOOSE!"
    elif (cardOne.get() < cardTwo.get()) and (higherSelected):
        returnString = "Yay! You WIN!"
    elif (cardOne.get() < cardTwo.get()) and (not higherSelected):
        returnString = "Sorry! You LOOSE!"
    elif cardOne.get() == cardTwo.get():
        returnString = "Sorry, you TIE!"
    else:
        returnString = "There has been a problem,\n so you WIN!"
    return returnString
        

#setup buttons
leftButton = Button(window, image = cardBackground, command = drawFirstCard)
rightButton = Button(window, image = cardBackground)

#Sets up and grids the label with instructions on how to begin the game
beginGameLabel = Label(window, text="Click the card to draw target.")
beginGameLabel.grid(row = 0, column = 1)

#Grids the left button, aka the first card.
leftButton.grid(row = 0, column = 0)

#Setup prompt frame for better formatting
promptFrame = Frame(window)

#Sets up the end game button and label
endGameLabel = Label(window, text = "PlaceHolder")
endGameButton = Button(window, text = "Draw", command = playAgain)

#prepares the prompt labels and button inputs.
promptLabel = Label(promptFrame, text = "Select Higher or Lower")
selectHigher = Radiobutton(promptFrame, text = "Higher", variable = selectVar, value = "2", command = drawSecondCard)
selectLower = Radiobutton(promptFrame, text = "Lower", variable = selectVar, value = "1", command = drawSecondCard)
promptLabel.grid(row = 0, column = 0)
selectHigher.grid(row = 1, column = 0)
selectLower.grid(row = 2, column = 0)

window.mainloop()
