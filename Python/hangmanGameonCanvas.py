from tkinter import *
import random
#Determine if letter of button clicked is in the word
def checkletter(word, alpha, guesslist):
    if alpha in word:
        for i in range(len(word)):
            if word[i] == alpha:
                guesslist[i] = alpha
        strikecount = 0 #letter found      
    else:
        strikecount = 1 #letter not found
    return strikecount

#Function to hide the word in a list
def hiddenword(word, guesslist):
    for i in range(len(word)):
        guesslist.append('*')
    return

#Function to turn hidden word list into a string to use with widgets
def listToString(guesslist):
    wordstr = ''
    for i in range(len(guesslist)):
        wordstr += guesslist[i]
    return wordstr

#Determine which button/letter was chosen
def getletter(t,index):
    global hiddenlist, word, strike
    #Call function to look for letter in the word
    if checkletter(word, t, hiddenlist) == 0:  #Letter in word case
        wordlabel['text'] = listToString(hiddenlist)
        if wordlabel['text'] == word:  #Player wins the game
            letterframe.grid_remove()
            canvas.delete("strikes")
            canvas.create_text(95, 20, text = "You WIN! Game Over", tags = "strikes")
            wordlabel['text'] = word
    elif strike <= 6: #Letter not in word case with strikes remaining
        strike += 1
        drawStickMan(strike)
        #Redraw/update canvas text
        canvas.delete("strikes")
        canvas.create_text(95, 20, text = "Strike " + str(strike), tags = "strikes")
    letbuttonlist[index]['state'] = 'disabled'
    #else: #Case where did not guess word and ran out of strikes
        
    return

def gameOver():
    letterframe.grid_remove()
    canvas.delete("strikes")
    canvas.create_text(95, 20, text = "Game Over", tags = "strikes")
    wordlabel['text'] = word
    return

def drawStickMan(strike):
    if strike == 0:
        canvas.create_line(95, 80, 95, 70, tags = "stickMan")
        canvas.create_line(95, 70, 50, 70, tags = "stickMan")
        canvas.create_line(50, 70, 50, 150, tags = "stickMan")
        canvas.create_line(25, 150, 75, 150, tags = "stickMan")
    if strike == 1:
        canvas.create_oval(90,80, 100,90, tags = "stickMan")
    if strike == 2:
        canvas.create_line(95, 90, 95, 110, tags = "stickMan")
    if strike == 3:
        canvas.create_line(95, 110, 80, 125, tags = "stickMan")
    if strike == 4:
        canvas.create_line(95, 110, 110, 125, tags = "stickMan")
    if strike == 5:
        canvas.create_line(95, 95, 80, 105, tags = "stickMan")
    if strike == 6:
        canvas.create_line(95, 95, 110, 105, tags = "stickMan")
    if strike == 7:
        canvas.create_oval(92, 83, 93, 85, tags = "stickMan")
        canvas.create_oval(98, 83, 97, 85, tags = "stickMan")
        canvas.create_line(92, 87, 98, 87, tags = "stickMan")
        for i in range(len(letbuttonlist)):
            letbuttonlist[i]['state'] = 'disabled'
        canvas.after(2000, gameOver)
        
    return

window = Tk()
wordList = ["GUITAR", "MOO", "FORTNITE", "CALCULUS", "TRAIN", "THANKSGIVING", "FOOTBALL", "FALL", "OCEAN", "HANGMAN", "MINECRAFT", "FUN", "TIKTOK", "BOOMER", "BALL", "TABLE", "WATER", "PROCRASTINATE", "AIRPODS", "VINE", "KING", "NAPALM", "FUN", "SPONGEBOB", "MEME", "SPEED" "CARS", "COLLEGE", "SCHOOL"]
word = wordList[random.randint(0,(len(wordList))-1)]
strike = 0
hiddenlist = []
hiddenword(word, hiddenlist) #Create hidden word list

#Create canvas with text
canvas = Canvas(window, width = 200, height = 200)
canvas.create_text(95, 20, text = "Strike 0", tags = "strikes")
canvas.grid()


#Create labels for game window
headingLabel = Label(window, text = 'The word is ...')
wordlabel = Label(window, text = listToString(hiddenlist))
headingLabel.grid()
wordlabel.grid()

#Create frame for letter buttons
letterframe = Frame(window)
letterframe.grid()

letbuttonlist = [] #Letter button list
#Generate Letter buttons and place in Letter button list
for i in range(26):
    letter = chr(65+i)
    b = Button(letterframe, text = letter, command = lambda ltr=letter,
               ltrnum=i: getletter(ltr,ltrnum))
    b.grid(row=i//13, column=i%13)
    letbuttonlist.append(b)

drawStickMan(strike)     
window.mainloop()
