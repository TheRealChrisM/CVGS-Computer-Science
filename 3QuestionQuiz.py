#Christopher Marotta
#October 28th, 2019
#3 Question Quiz: Radio Button (Multiple Choice), Entry Box, Drop Down
from tkinter import *
from tkinter import ttk

def processQuiz():
    correctAnswers = 0
    if (qOne.get() == 2):
        correctAnswers += 1
    if (qTwo.get() == "19"):
        correctAnswers += 1
    if (qThree.get() == "Richmond"):
        correctAnswers += 1
    questionFrame.pack_forget()
    gradeFrame = Frame(window)
    gradeString = "You got " + str(correctAnswers) + " correct out of 3."
    gradeLabel = Label(gradeFrame, text=gradeString)
    gradeLabel.grid(row = 0, column = 0)
    gradeFrame.pack()
window = Tk()
questionFrame = Frame(window)
qOne = IntVar()
qTwo = StringVar()
#question one code
questionOneLabel = Label(questionFrame, text = "1) What is the formula for the area of a square?")
questionOneChoiceA = Radiobutton(questionFrame, text="[A] 2*s*pi*(r^2)", variable = qOne, value = 1)
questionOneChoiceB = Radiobutton(questionFrame, text="[B] s^2", variable = qOne, value = 2)
questionOneChoiceC = Radiobutton(questionFrame, text="[C] 4s", variable = qOne, value = 3)
questionOneChoiceD = Radiobutton(questionFrame, text="[D] s+2", variable = qOne, value = 4)
questionOneLabel.grid(row = 0, column = 0)
questionOneChoiceA.grid(row = 1, sticky = W, padx = 20)
questionOneChoiceB.grid(row = 2, sticky = W, padx = 20)
questionOneChoiceC.grid(row = 3, sticky = W, padx = 20)
questionOneChoiceD.grid(row = 4, sticky = W, padx = 20)

#question two code
questionTwoLabel = Label(questionFrame, text = "2) What is the sum of the numbers nine and ten?")
questionTwoEntryBox = Entry(questionFrame, textvariable = qTwo)
questionTwoLabel.grid(row = 6, column = 0)
questionTwoEntryBox.grid(row = 7, column = 0)

#question three code
questionThreeLabel = Label(questionFrame, text = "3) What is the capital of Virginia?")
cities = ['Washington', 'Lynchburg', 'Seattle', 'Richmond', 'Springfield']
qThree = StringVar()
qThree.set('Choose City')
questionThreeDropdown = ttk.Combobox(questionFrame, values = cities, textvariable = qThree, state='readonly')
questionThreeLabel.grid(row = 9, column = 0, sticky = W)
questionThreeDropdown.grid(row = 9, column = 1, sticky = W)

#gradeButton
gradeQuiz = Button(questionFrame, text="Grade Quiz", command = processQuiz)
gradeQuiz.grid(row = 11, columnspan = 2)

questionFrame.pack()
window.mainloop()
