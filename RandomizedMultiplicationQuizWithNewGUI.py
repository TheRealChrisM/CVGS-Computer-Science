from tkinter import *
import random

def processGoButton():
    global num1, num2
    frame1.grid_remove()
    frame3.grid(row = 0, column = 0)
    goButton.grid_remove()
    gradeButton.grid()

    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    questionLabel["text"] = (str(num1) + " * " + str(num2) + " = ")
    return

def processGradeButton():
    global num1,num2
    answer = num1 * num2
    result = "Incorrect"
    if (str(answer) == answerVar.get()):
        result = "Correct"
    gradeLabel["text"] = firstVar.get() + " " + lastVar.get() + ", you are " + result + "."
    gradeLabel.grid(row = 1, columnspan = 2)
    gradeButton.grid_remove()
    nextQuestionButton.grid()
    return

def processNextQuestion():
    global num1, num2
    gradeButton.grid()

    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    questionLabel["text"] = (str(num1) + " * " + str(num2) + " = ")
    nextQuestionButton.grid_remove()
    gradeLabel.grid_remove()
    answerVar.set("")
    gradeButton.grid()
    return

num1 = 0
num2 = 0

window = Tk()
window.geometry("300x300")

frame1 = Frame(window)
firstVar = StringVar()
lastVar = StringVar()
firstLabel = Label(frame1, text="First Name: ")
lastLabel = Label(frame1, text = "Last Name: ")
firstEntry = Entry(frame1, textvariable = firstVar)
lastEntry = Entry(frame1, textvariable = lastVar)


firstEntry.grid(row = 0, column = 1)
lastEntry.grid(row = 1, column = 1)
firstLabel.grid(row = 0, column = 0, sticky = E)
lastLabel.grid(row = 1, column = 0, sticky = E)


frame2 = Frame(window)
goButton = Button(frame2, text = "Start", command = processGoButton)
gradeButton = Button(frame2, text = "Check Answer", command = processGradeButton)
nextQuestionButton = Button(frame2, text = "Next Question", command = processNextQuestion)
goButton.grid(row = 2, columnspan = 2)


frame3 = Frame(window)
answerVar = StringVar()
questionLabel = Label(frame3, text = "Place Holder")
answerEntry = Entry(frame3, textvariable = answerVar)
questionLabel.grid(row = 0, column = 0)
answerEntry.grid(row = 0, column = 1)
gradeLabel = Label(frame3, text = "place holder")

frame1.grid()
frame2.grid()
#"I've done all of this but my window doesn't show up."
window.mainloop()
