#Christopher Marotta
#November 12, 2019
#Lab Assignment - Concentration Game
from tkinter import *
from PIL import ImageTk

#Sets up the game
window = Tk()
frame = Frame(window)
buttonFrame = Frame(window)
window.title("Concentration Game")
pickedCard = IntVar()
pickedCard.set(0)
matches = IntVar()
matches.set(0)
lives = IntVar()
lives.set(5)
score = Label(frame, text = "Score: 0")
score.grid(row = 0, column = 0)
lifeLabel = Label(frame, text = "Lives: 5")
lifeLabel.grid(row=0, column = 1)
buttonList = []
endFrame = Frame(window)

#Flips a card back over to the background
def flipBack(card):
    card['image'] = cardBackground
    card['state'] = "active"
    lives.set(lives.get()-1)
    lifeLabel["text"] = "Lives: " + str(lives.get())
    if (lives.get() == 0) or (matches.get() == 8):
        endGame()
    return

#Flips a card over to it's image
def flipOver(card, img):
    card['image'] = img
    card['state'] = "disabled"
    if (matches.get() == 8):
        endGame()
    return

#Ends the game
def endGame():
    buttonFrame.pack_forget()
    frame.pack_forget()
    endGameLabelString = ""
    if (matches.get() == 8):
        endGameLabelString = "You have won! You got " + str(matches.get()) + " matches with " + str(lives.get()) + " lives remaining. \n Would you like to play again?"
    elif (lives.get() == 0):
        endGameLabelString = "You have lost! You got " + str(matches.get()) + " matches with Zero lives remaining.\n Would you like to play again?"
    else:
        endGameLabelString = "There has been an error. You finished the game with " + str(matches.get()) + " matches and " + str(lives.get()) + " lives. \n Would you like to play again?"
    endGameLabel = Label(endFrame, text = endGameLabelString)
    endGameLabel.grid(row = 0, column = 0)
    playAgainButton = Button(endFrame, text = "Play Again", command = playAgain)
    endGameButton = Button(endFrame, text = "Exit", command = exitGame)
    playAgainButton.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
    endGameButton.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = E)
    endFrame.pack()

#Allows player to exit the game
def exitGame():
    window.destroy()

#Allows the player to play again and resets the game
def playAgain():
    for i in range(16):
        flipBack(buttonList[i])
    buttonFrame.pack()
    frame.pack()
    endFrame.pack_forget()
    lives.set(5)
    matches.set(0)
    pickedCard.set(0)
    score['text'] = "Score: " + str(matches.get())
    lifeLabel["text"] = "Lives: " + str(lives.get())

#All the logic for when a user presses any card button
def buttonOne():
    flipOver(buttonOne, cardOne)#funcbutton, cardnum
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 7):#matchnum
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonOne['state'] = 'disabled'#funcbutton
            buttonSeven['state'] = 'disabled'#matchbutton
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonOne['image'] = cardBackground#funcbutton
            buttonOne['state'] = "active"#funcbutton
    else:
        pickedCard.set(1)#funcnum
    return

def buttonTwo():
    flipOver(buttonTwo, cardTwo)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 4):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonTwo['state'] = 'disabled'
            buttonFour['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonTwo['image'] = cardBackground
            buttonTwo['state'] = "active"
    else:
        pickedCard.set(2)
    return

def buttonThree():
    flipOver(buttonThree, cardSix)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 13):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonThree['state'] = 'disabled'
            buttonThirteen['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonThree['image'] = cardBackground
            buttonThree['state'] = "active"
    else:
        pickedCard.set(3)
    return

def buttonFour():
    flipOver(buttonFour, cardTwo)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 2):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonFour['state'] = 'disabled'
            buttonTwo['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonFour['image'] = cardBackground
            buttonFour['state'] = "active"
    else:
        pickedCard.set(4)
    return

def buttonFive():
    flipOver(buttonFive, cardThree)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 16):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonFive['state'] = 'disabled'
            buttonSixteen['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonFive['image'] = cardBackground
            buttonFive['state'] = "active"
    else:
        pickedCard.set(5)
    return

def buttonSix():
    flipOver(buttonSix, cardSeven)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 14):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonSix['state'] = 'disabled'
            buttonFourteen['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonSix['image'] = cardBackground
            buttonSix['state'] = "active"
    else:
        pickedCard.set(6)
    return

def buttonSeven():
    flipOver(buttonSeven, cardOne)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 1):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonOne['state'] = 'disabled'
            buttonSeven['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonSeven['image'] = cardBackground
            buttonSeven['state'] = "active"
    else:
        pickedCard.set(7)
    return

def buttonEight():
    flipOver(buttonEight, cardFour)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 10):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonEight['state'] = 'disabled'
            buttonTen['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonEight['image'] = cardBackground
            buttonEight['state'] = "active"
    else:
        pickedCard.set(8)
    return

def buttonNine():
    flipOver(buttonNine, cardEight)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 11):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonNine['state'] = 'disabled'
            buttonEleven['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonNine['image'] = cardBackground
            buttonNine['state'] = "active"
    else:
        pickedCard.set(9)
    return

def buttonTen():
    flipOver(buttonTen, cardFour)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 8):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonTen['state'] = 'disabled'
            buttonEight['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonTen['image'] = cardBackground
            buttonTen['state'] = "active"
    else:
        pickedCard.set(10)
    return

def buttonEleven():
    flipOver(buttonEleven, cardEight)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 9):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonEleven['state'] = 'disabled'
            buttonNine['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonEleven['image'] = cardBackground
            buttonEleven['state'] = "active"
    else:
        pickedCard.set(11)
    return

def buttonTwelve():
    flipOver(buttonTwelve, cardFive)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 15):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonTwelve['state'] = 'disabled'
            buttonFifteen['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonTwelve['image'] = cardBackground
            buttonTwelve['state'] = "active"
    else:
        pickedCard.set(12)
    return

def buttonThirteen():
    flipOver(buttonThirteen, cardSix)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 3):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonThirteen['state'] = 'disabled'
            buttonThree['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonThirteen['image'] = cardBackground
            buttonThirteen['state'] = "active"
    else:
        pickedCard.set(13)
    return

def buttonFourteen():
    flipOver(buttonFourteen, cardSeven)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 6):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonFourteen['state'] = 'disabled'
            buttonSix['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonFourteen['image'] = cardBackground
            buttonFourteen['state'] = "active"
    else:
        pickedCard.set(14)
    return

def buttonFifteen():
    flipOver(buttonFifteen, cardFive)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 12):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonFifteen['state'] = 'disabled'
            buttonTwelve['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonFifteen['image'] = cardBackground
            buttonFifteen['state'] = "active"
    else:
        pickedCard.set(15)
    return

def buttonSixteen():
    flipOver(buttonSixteen, cardThree)
    if not (pickedCard.get() == 0):
        if (pickedCard.get() == 5):
            matches.set(matches.get()+1)
            score['text'] = "Score: " + str(matches.get())
            if (matches.get() == 8):
                endGame()
            pickedCard.set(0)
            buttonSixteen['state'] = 'disabled'
            buttonFive['state'] = 'disabled'
        else:
            window.update()
            window.after(1000, flipBack(buttonList[pickedCard.get()-1]))
            pickedCard.set(0)
            buttonSixteen['image'] = cardBackground
            buttonSixteen['state'] = "active"
    else:
        pickedCard.set(16)
    return
#####END CARD BUTTON LOGIC#####

#creating images for the buttons
cardOne = ImageTk.PhotoImage(file = "image/card/1.gif")
cardTwo = ImageTk.PhotoImage(file = "image/card/2.gif")
cardThree = ImageTk.PhotoImage(file = "image/card/3.gif")
cardFour = ImageTk.PhotoImage(file = "image/card/4.gif")
cardFive = ImageTk.PhotoImage(file = "image/card/5.gif")
cardSix = ImageTk.PhotoImage(file = "image/card/6.gif")
cardSeven = ImageTk.PhotoImage(file = "image/card/7.gif")
cardEight = ImageTk.PhotoImage(file = "image/card/8.gif")
cardBackground = ImageTk.PhotoImage(file = "image/card/b2fv.gif")

###BUTTON MATCHES###
#buttonOne = buttonSeven (1)
#buttonTwo = buttonFour (2)
#buttonFive = buttonSixteen (3)
#buttonEight = buttonTen (4)
#buttonFifteen = buttonTwelve (5)
#buttonThirteen = buttonThree (6)
#buttonFourteen = buttonSix (7)
#buttonNine = buttonEleven (8)

#creating the buttons
buttonOne = Button(buttonFrame, image=cardBackground, command = buttonOne)
buttonTwo = Button(buttonFrame, image=cardBackground, command = buttonTwo)
buttonThree = Button(buttonFrame, image=cardBackground, command = buttonThree)
buttonFour = Button(buttonFrame, image=cardBackground, command = buttonFour)
buttonFive = Button(buttonFrame, image=cardBackground, command = buttonFive)
buttonSix = Button(buttonFrame, image=cardBackground, command = buttonSix)
buttonSeven = Button(buttonFrame, image=cardBackground, command = buttonSeven)
buttonEight = Button(buttonFrame, image=cardBackground, command = buttonEight)
buttonNine = Button(buttonFrame, image=cardBackground, command = buttonNine)
buttonTen = Button(buttonFrame, image=cardBackground, command = buttonTen)
buttonEleven = Button(buttonFrame, image=cardBackground, command = buttonEleven)
buttonTwelve = Button(buttonFrame, image=cardBackground, command = buttonTwelve)
buttonThirteen = Button(buttonFrame, image=cardBackground, command = buttonThirteen)
buttonFourteen = Button(buttonFrame, image=cardBackground, command = buttonFourteen)
buttonFifteen = Button(buttonFrame, image=cardBackground, command = buttonFifteen)
buttonSixteen = Button(buttonFrame, image=cardBackground, command = buttonSixteen)
buttonList = [buttonOne, buttonTwo, buttonThree, buttonFour, buttonFive, buttonSix, buttonSeven, buttonEight, buttonNine, buttonTen, buttonEleven, buttonTwelve, buttonThirteen, buttonFourteen, buttonFifteen, buttonSixteen]

#griding the buttons
buttonOne.grid(row = 0, column = 0)
buttonTwo.grid(row = 0, column = 1)
buttonThree.grid(row = 0, column = 2)
buttonFour.grid(row = 0, column = 3)
buttonFive.grid(row = 1, column = 0)
buttonSix.grid(row = 1, column = 1)
buttonSeven.grid(row = 1, column = 2)
buttonEight.grid(row = 1, column = 3)
buttonNine.grid(row = 2, column = 0)
buttonTen.grid(row = 2, column = 1)
buttonEleven.grid(row = 2, column = 2)
buttonTwelve.grid(row = 2, column = 3)
buttonThirteen.grid(row = 3, column = 0)
buttonFourteen.grid(row = 3, column = 1)
buttonFifteen.grid(row = 3, column = 2)
buttonSixteen.grid(row = 3, column = 3)

#Sets up the window and starts the game
buttonFrame.pack()
frame.pack()
window.mainloop()
