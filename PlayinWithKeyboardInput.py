#Christopher Marotta
#October 30th 2019
#Playin' with Keyboard Input

import sys
import time
import os
import curses

gameArea = []

for m in range(5):
    line=[]
    for n in range(50):
        line.append("0")
    gameArea.append(line)

printGame = ""

for i in range(len(gameArea)):
    for l in range(len(gameArea[i])):
        printGame+=gameArea[i][l]
    printGame+= "\n"

sys.stdout.write(printGame)


gameWindow = curses.newwin(100,100)

time.sleep(500)
playing = True
while (playing):
    printGame = ""

    for i in range(len(gameArea)):
        for l in range(len(gameArea[i])):
            printGame+=gameArea[i][l]
        printGame+= "\n"

    #sys.stdout.write(printGame)
    gameWindow.addstr(0,0, printGame)
    time.sleep(.5)
    #os.system('cls' if os.name == 'nt' else 'clear')
    gameWindow.clear()
