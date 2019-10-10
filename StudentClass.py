import random
class Student:
    def __init__(self, fName="", lName=""):
        self.__firstName = fName
        self.__lastName = lName
        self.__testScores = []
        return

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getTestScore(self,num):
        numGet = num - 1
        return self.__testScores[numGet]

    def setFirstName(self, newName):
        self.__firstName = newName
        return

    def setLastName(self, newName):
        self.__lastName = newName
        return

    def setTestScore(self, newScore):
        self.__testScores.append(newScore)
        return

    def returnTestAverage(self):
        x = 1
        scoreTotal = 0
        while(x<=len(self.__testScores)):
            scoreTotal += self.getTestScore(x)
            x += 1
        return scoreTotal/(len(self.__testScores))

class Quiz:
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

    def getStudent(self):
        return self.__testTaker

    def getNumberOfQuestions(self):
        return self.__numberOfQuestions

    def getQuestion(self, questionNo):
        #make questionBank
        self.__questionBank.append("Lmao what are dogs?")
        self.__questionBank.append("Lmao what are cats?")
        self.__questionBank.append("Lmao what are horses?")
        self.__questionBank.append("Lmao what are meows?")
        self.__questionBank.append("Lmao what are mice?")
        self.__questionBank.append("Lmao what are NullPointerError?")
        return self.__questionBank[questionNo]

    def getAnswerChoices(self, questionNo):
        #make optionBank
        self.__optionBank.append("\t[A]: Not Cats \n \t[B]: Fortnite \n \t[C]: Macbook \n \t[D]: Drugs")
        self.__optionBank.append("\t[A]: Meanieheads \n \t[B]: Meow \n \t[C]: Minecraft \n \t[D]: The Spanish Inquisition")
        self.__optionBank.append("\t[A]: Car \n \t[B]: Not Car \n \t[C]: Car? \n \t[D]: Car.")
        self.__optionBank.append("\t[A]: Cats \n \t[B]: Rats \n \t[C]: Mats \n \t[D]: Zaps")
        self.__optionBank.append("\t[A]: Not Cats \n \t[B]: Door \n \t[C]: An I Oop \n \t[D]: Hmmm?")
        self.__optionBank.append("\t[A]: Nah \n \t[B]: Java be like... \n \t[C]: None \n \t[D]: Skskskksksk")
        return self.__optionBank[questionNo]

    def getAnswer(self, questionNo):
        #make answerBank
        self.__answerBank.append("A")
        self.__answerBank.append("A")
        self.__answerBank.append("A")
        self.__answerBank.append("A")
        self.__answerBank.append("A")
        self.__answerBank.append("A")
        return self.__answerBank[questionNo]

    def getQuestionByID(self, id):
        return self.__quizQuestions[id]

    def generateQuiz(self):
        self.getQuestion(0)
        self.getAnswerChoices(0)
        self.getAnswer(0)
        
        quesNo = self.getNumberOfQuestions()
        bankSize = len(self.__questionBank)
        rangeSize = bankSize - 1
        
        for i in range(quesNo):
            randNo = random.randint(0, rangeSize)
            self.__quizQuestions.append(randNo)
        return

    def collectAnswers(self):
        self.__submittedAnswers = []
        for i in range(self.getNumberOfQuestions()):
            self.__submittedAnswers.append(input(str(i+1) + ": "))
        return
    
    def checkAnswers(self):
        self.__pointsCorrect = 0
        for i in range(self.getNumberOfQuestions()):
            if (self.__submittedAnswers[i] == self.__questionsGenerated[2][i]):
                self.__pointsCorrect += 1
        return self.__pointsCorrect

    def assignGrade(self, student, score):
        
        
    def takeQuiz(self, student):        
            
    def __str__(self):
        self.__questionsGenerated = [[],[],[]]
        questionsGenerated = self.__questionsGenerated
        returnString = "Welcome " + self.getStudent().getFirstName() + " to your Quiz!\n"
        returnString += "You have chosen to have " + str(self.getNumberOfQuestions()) + " questions. Here are your questions!\n"
        returnString += "The questions will be generated, then to choose an answer you must enter the desired letter in uppercase after the appropriate question number. \n"
        returnString += "\n"
        for i in range(self.getNumberOfQuestions()):
            questionNo = self.getQuestionByID(i)
            questionsGenerated[0].append(self.getQuestion(questionNo))
            questionsGenerated[1].append(self.getAnswerChoices(questionNo))
            questionsGenerated[2].append(self.getAnswer(questionNo))
        x = 0
        for i in range(self.getNumberOfQuestions()):
            returnString += str(i+1) + "- " + questionsGenerated[0][i] + "\n"
            returnString += questionsGenerated[1][i] + "\n"

        return returnString


x=Student("Chris", "Marotta")
y=Quiz(x,5)
y.generateQuiz()
print(y)
y.collectAnswers()
print(y.checkAnswers())
