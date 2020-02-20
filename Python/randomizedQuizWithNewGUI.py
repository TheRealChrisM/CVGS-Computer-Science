#Christopher Marotta
#October 29th, 2019
#Lab I - Part I (Class Schedule Program)
from tkinter import *
import random
from tkinter import ttk

class Student:
    #sets up the student object with an input of their first and last name
    def __init__(self, fName="", lName=""):
        self.__firstName = fName
        self.__lastName = lName
        self.__testScores = []
        return
    #returns the student's first name
    def getFirstName(self):
        return self.__firstName

    #returns the student's last name
    def getLastName(self):
        return self.__lastName

    #outputs a test score based on which number test is requested
    def getTestScore(self,num):
        numGet = num - 1
        return self.__testScores[numGet]

    #sets a new first name for the student
    def setFirstName(self, newName):
        self.__firstName = newName
        return

    #sets a new last name for the student
    def setLastName(self, newName):
        self.__lastName = newName
        return

    #adds a test score to the student
    def setTestScore(self, newScore):
        self.__testScores.append(newScore)
        return

    #calculates the average test score of the student
    def returnTestAverage(self):
        x = 1
        scoreTotal = 0
        while(x<=len(self.__testScores)):
            scoreTotal += self.getTestScore(x)
            x += 1
        return scoreTotal/(len(self.__testScores))

    #calcualtes the letter grade for the students average score
    def calculateGrade(self):
        grade = "ERR"
        scoreAverage = self.returnTestAverage()
        if scoreAverage >= 90:
            grade = "A"
        elif scoreAverage >= 80:
            grade = "B"
        elif scoreAverage >= 70:
            grade = "C"
        elif scoreAverage >= 60:
            grade = "D"
        else:
            grade = "F"
        return grade

    #returns a formatted string with a student's information
    def __str__(self):
        returnString = self.getLastName() + ", " + self.getFirstName() + ":\n"
        for i in range(len(self.__testScores)):
            returnString += "\tQuiz " + str(i+1) + ": " + str(self.getTestScore(i+1)) + "% \n"
        returnString += "--------------------\n"
        returnString += "Average Score: " + str(format(self.returnTestAverage(), "2.2f")) + "%\n"
        returnString += "Grade: " + self.calculateGrade()
        return returnString
    
class Quiz:
    #sets up a quiz with the input of a student object and the number of questions
    def __init__(self, student, questions):
        self.__testTaker = student
        self.__numberOfQuestions = questions
        self.__questionBank = []
        self.__optionBank = []
        self.__answerBank = []
        self.__quizQuestions = []
        self.__submittedAnswers = []
        self.__pointsCorrect = 0
        self.__questionsGenerated = [[],[],[]]
        self.__quizGenerated = False
        self.setQuestion()
        self.setAnswerChoices()
        self.setAnswer()
        return

    #returns the student object associated with the quiz object
    def getStudent(self):
        return self.__testTaker

    #returns the number of questions for the quiz
    def getNumberOfQuestions(self):
        return self.__numberOfQuestions

    #changes the state of the quizGenerated variable to the input
    def changeQuizGenerated(self, newVal):
        self.__quizGenerated = newVal;
        return

    #returns the value of quizGenerated
    def quizGenerated(self):
        return self.__quizGenerated
    
    #sets up the question choices
    def setQuestion(self):
        self.__questionBank.append("What sound does a cat make?")
        self.__questionBank.append("What is 9 + 10?")
        self.__questionBank.append("Red, White, and ____ are the colors of the American Flag?")
        self.__questionBank.append("What is the Sun?")
        self.__questionBank.append("What is H2O commonly known as?")
        self.__questionBank.append("What do you call someone who studies Biology?")
        return
    #returns a question from the bank based on the number input
    def getQuestion(self,questionNo):
        return self.__questionBank[questionNo]

    #sets up the answer choices which correspond to the questions
    def setAnswerChoices(self):
        self.__optionBank.append("[A]: Bark\n[B]: Meow\n[C]: *Static Noises*\n[D]: I'm a cat.")
        self.__optionBank.append("[A]: 21\n[B]: 1\n[C]: 19\n[D]: 90")
        self.__optionBank.append("[A]: Rainbow\n[B]: Pink\n[C]: Null\n[D]: Blue")
        self.__optionBank.append("[A]: A Lie.\n[B]: A Star.\n[C]: A Planet.\n[D]: A Pluto.")
        self.__optionBank.append("[A]: Rockstar Energy Drink Formula\n[B]: Robitussin DM\n[C]: Water\n[D]: Table Salt")
        self.__optionBank.append("[A]: A Biologist.\n[B]: A Police Officer.\n[C]: A Telephone.\n[D]: A Astronaut.")
        return 

    #returns the answer choices based on the number input
    def getAnswerChoices(self, questionNo):
        return self.__optionBank[questionNo]

    #sets up the correct answers which correspond to the questions
    def setAnswer(self):
        self.__answerBank.append("B")
        self.__answerBank.append("C")
        self.__answerBank.append("D")
        self.__answerBank.append("B")
        self.__answerBank.append("C")
        self.__answerBank.append("A")
        return 

    #returns the correct answer based on the number input
    def getAnswer(self, questionNo):
        return self.__answerBank[questionNo]

    #returns a question based on it's index within the selected quiz questions list
    def getQuestionByID(self, id):
        return self.__quizQuestions[id]

    #actually generates the quiz and chooses the questions
    def generateQuiz(self):
        quesNo = self.getNumberOfQuestions()
        bankSize = len(self.__questionBank)
        rangeSize = bankSize - 1
        
        for i in range(quesNo):
            randNo = random.randint(0, rangeSize)
            while (randNo in self.__quizQuestions):
                randNo = random.randint(0, rangeSize)
            self.__quizQuestions.append(randNo)
        self.__questionsGenerated = [[],[],[]]
        questionsGenerated = self.__questionsGenerated
        for i in range(self.getNumberOfQuestions()):
            questionNo = self.getQuestionByID(i)
            questionsGenerated[0].append(self.getQuestion(questionNo))
            questionsGenerated[1].append(self.getAnswerChoices(questionNo))
            questionsGenerated[2].append(self.getAnswer(questionNo))
        self.changeQuizGenerated(True)
        return
    
    #collects the answers to the questions from the student
    def collectAnswers(self):
        self.__submittedAnswers = []
        for i in range(self.getNumberOfQuestions()):
            self.__submittedAnswers.append(input(str(i+1) + ": "))
        return

    #compares the student's answers against the correct answer
    def checkAnswers(self):
        self.__pointsCorrect = 0
        for i in range(self.getNumberOfQuestions()):
            if (self.__submittedAnswers[i] == self.__questionsGenerated[2][i]):
                self.__pointsCorrect += 1
        return self.__pointsCorrect

    #manually set student's answers, takes in a list and sets it to submittedAnswers
    def manuallyCollectAnswers(self, answerChoiceInput):
        self.__submittedAnswers = answerChoiceInput
        return
    
    #actually assigns the student a grade based on their accuracy on the quiz
    def assignGrade(self, percentage):
        student = self.getStudent()
        percentage = eval(format(percentage, "2.2f"))
        student.setTestScore(percentage)
        return

    #gives the student their quiz 
    def takeQuiz(self):
        if not (self.quizGenerated()):
            self.generateQuiz()
        print(self)
        self.collectAnswers()
        pointsCorrect = self.checkAnswers()
        ratioCorrect = pointsCorrect/(self.getNumberOfQuestions())
        percentageCorrect = ratioCorrect * 100
        self.assignGrade(percentageCorrect)
        return
    
    #overloads the string object to print out the questions for the quiz
    def __str__(self):
        if not (self.quizGenerated()):
            self.generateQuiz()
        
        returnString = "Welcome, " + self.getStudent().getFirstName() + ", to your Quiz!\n"
        returnString += "You have chosen to have " + str(self.getNumberOfQuestions()) + " questions. Here are your questions!\n"
        returnString += "The questions will be generated, then to choose an answer you must enter the desired letter in uppercase after the appropriate question number. \n"
        returnString += "\n"
        x = 0
        for i in range(self.getNumberOfQuestions()):
            returnString += str(i+1) + "- " + questionsGenerated[0][i] + "\n"
            returnString += questionsGenerated[1][i] + "\n"

        return returnString

#creates thinker window
window = Tk()
window.title("Quiz Application")

#creates a placeholder for collectedAnswers and currentquiz so it may be used as a global variable to allow for it to be used in nextQuestion function
collectedAnswers = []
currentQuiz = None

#Allows any function to see the current answer choice
answerChoice = StringVar()
answerChoice.set("0")
#creates the function to process a "SignIn"
def processSignIn():
    beginTest(Student(firstNameVar.get(), lastNameVar.get()))
    return

#defines all the GUI elements outside of the function
collectedAnswers = []
currentQuiz = None
currentQuestion = 0

#setup quizFrame
quizFrame = Frame(window)
answerFrame = Frame(window)
questionLabel = Label(quizFrame, text = "[x] Placeholder Question....")
answerChoiceLabel = Label(quizFrame, text = "[A]:Bark \n[B]:Meow\n[C]:*Static Noises*\n[D]:I'm a cat.")   
choiceA = Radiobutton(answerFrame, text="[A]", variable = answerChoice, value = "A")
choiceB = Radiobutton(answerFrame, text="[B]", variable = answerChoice, value = "B")
choiceC = Radiobutton(answerFrame, text="[C]", variable = answerChoice, value = "C")
choiceD = Radiobutton(answerFrame, text="[D]", variable = answerChoice, value = "D")
#starts the test
def beginTest(createdStudent):
    
    student = createdStudent
    
    #create and generate quiz
    global collectedAnswers, currentQuiz
    currentQuiz = Quiz(student, int(selectedQuizLength.get()))
    currentQuiz.generateQuiz()
    questionLabel.grid(row = 0, column = 0, sticky = W+E)
    answerChoiceLabel.grid(row = 1, column = 0)
    choiceA.grid(row = 0, column = 0)
    choiceB.grid(row = 0, column = 1)
    choiceC.grid(row = 0, column = 2)
    choiceD.grid(row = 0, column = 3)
    submitAnswer = Button(answerFrame, text="Submit Answer", command = nextQuestion)
    submitAnswer.grid(row = 1, columnspan = 4)
    questionLabel["text"] = currentQuiz.getQuestion(currentQuiz.getQuestionByID(0))
    answerChoiceLabel["text"] = currentQuiz.getAnswerChoices(currentQuiz.getQuestionByID(0))
    studentSignIn.pack_forget()
    quizFrame.pack()
    answerFrame.pack()
    return

def nextQuestion():
    if(len(collectedAnswers)<(int(selectedQuizLength.get())-1)):
        global collectedAnswers, currentQuiz
        questionLabel["text"] = currentQuiz.getQuestion(currentQuiz.getQuestionByID((len(collectedAnswers)+1)))
        answerChoiceLabel["text"] = currentQuiz.getAnswerChoices(currentQuiz.getQuestionByID((len(collectedAnswers)+1)))
        collectedAnswers.append(answerChoice.get())
        answerChoice.set("0")
    else:
        collectedAnswers.append(answerChoice.get())
        currentQuiz.manuallyCollectAnswers(collectedAnswers)
        showResults()
    return

def showResults():
    pointsCorrect = currentQuiz.checkAnswers()
    ratioCorrect = pointsCorrect/(currentQuiz.getNumberOfQuestions())
    percentageCorrect = ratioCorrect * 100
    currentQuiz.assignGrade(percentageCorrect)
    resultsFrame = Frame(window)
    quizSummaryString = "Results for " + currentQuiz.getStudent().getLastName() + ", " + currentQuiz.getStudent().getFirstName() + ": "
    quizSummaryTitle = Label(resultsFrame, text = quizSummaryString)
    quizSummaryTitle.grid(row = 0, sticky = W)
    for i in range(len(collectedAnswers)):
        Label(resultsFrame, text = ("["+str(i)+"] "+(currentQuiz.getQuestion(currentQuiz.getQuestionByID(i))))).grid(row = ((i*3)+1), sticky = W, padx = 10)
        userAnswerString = "You selected: " + collectedAnswers[i]
        correctAnswerString = "The correct answer is: " + currentQuiz.getAnswer(currentQuiz.getQuestionByID(i))
        Label(resultsFrame, text = userAnswerString).grid(row = ((i*3)+2), sticky = W, padx = 25)
        Label(resultsFrame, text = correctAnswerString).grid(row = ((i*3)+3), sticky = W, padx = 25)
    resultString = "You got a " + str(currentQuiz.getStudent().getTestScore(1)) + "% [" + currentQuiz.getStudent().calculateGrade() + "]"
    resultLable = Label(resultsFrame, text = resultString)
    resultLable.grid(row = ((len(collectedAnswers)*3)+4))
    quizFrame.pack_forget()
    answerFrame.pack_forget()
    resultsFrame.pack()
    return

#Collects student information
studentSignIn = Frame(window)
firstNameLabel = Label(studentSignIn, text="First Name:")
firstNameVar = StringVar()
firstNameEntry = Entry(studentSignIn, textvariable = firstNameVar)
lastNameLabel = Label(studentSignIn, text="Last Name:")
lastNameVar = StringVar()
lastNameEntry = Entry(studentSignIn, textvariable = lastNameVar)
firstNameLabel.grid(row = 0, column = 0, pady = 10, sticky = W)
firstNameEntry.grid(row = 0, columnspan = 2, pady = 10, padx = 5)
lastNameLabel.grid(row = 1, column = 0, pady = 10, sticky = W)
lastNameEntry.grid(row = 1, columnspan = 2, pady = 10, padx = 5)


#collects quiz length information
quizLengthOptions = ["3", "4", "5"]
selectedQuizLength = StringVar()
selectedQuizLength.set("3")
quizLengthDropdown = ttk.Combobox(studentSignIn, values = quizLengthOptions, textvariable = selectedQuizLength, state = "readonly")
quizLengthLabel = Label(studentSignIn, text="Quiz Length [# of Qs]: ")
quizLengthLabel.grid(row = 2, column = 0, pady = 10)
quizLengthDropdown.grid(row = 2, column = 1, pady =10)

#creates signin button
signInButton = Button(studentSignIn, text="Sign In", command = processSignIn)
signInButton.grid(row = 3, columnspan = 2, pady = 10)
studentSignIn.pack()


window.mainloop()
