import random
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
        self.__optionBank.append("\t[A]: Bark \n \t[B]: Meow \n \t[C]: *Static Noises* \n \t[D]: I'm a cat.")
        self.__optionBank.append("\t[A]: 21 \n \t[B]: 1 \n \t[C]: 19 \n \t[D]: 90")
        self.__optionBank.append("\t[A]: Rainbow \n \t[B]: Pink \n \t[C]: Null \n \t[D]: Blue")
        self.__optionBank.append("\t[A]: A Lie. \n \t[B]: A Star. \n \t[C]: A Planet. \n \t[D]: A Pluto.")
        self.__optionBank.append("\t[A]: Rockstar Energy Drink Formula \n \t[B]: Robitussin DM \n \t[C]: Water \n \t[D]: Table Salt")
        self.__optionBank.append("\t[A]: A Biologist. \n \t[B]: A Police Officer. \n \t[C]: A Telephone. \n \t[D]: A Astronaut.")
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
        self.__questionsGenerated = [[],[],[]]
        questionsGenerated = self.__questionsGenerated
        returnString = "Welcome, " + self.getStudent().getFirstName() + ", to your Quiz!\n"
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

#Sets up the list to contain the students
listOfStudents = []

#adds first student to list
sOneFirstName = input("Student One, what is your first name? ")
sOneLastName = input(sOneFirstName + ", what is your last name? ")
listOfStudents.append(Student(sOneFirstName, sOneLastName))

#adds second student to list
sTwoFirstName = input("Student Two, what is your first name? ")
sTwoLastName = input(sTwoFirstName + ", what is your last name? ")
listOfStudents.append(Student(sTwoFirstName, sTwoLastName))

#adds third student to list
sThreeFirstName = input("Student Three, what is your first name? ")
sThreeLastName = input(sThreeFirstName + ", what is your last name? ")
listOfStudents.append(Student(sThreeFirstName, sThreeLastName))



#lets student one take their first quiz
print(listOfStudents[0].getFirstName(), " it is now time to take your first quiz...", sep="")
sOneNumberOfQuestions = eval(input(listOfStudents[0].getFirstName() + ", how many questions would you like? [Choose a number between 3 and 5] "))
while(sOneNumberOfQuestions > 5) or (sOneNumberOfQuestions < 3):
    sOneNumberOfQuestions = eval(input(listOfStudents[0].getFirstName() + ", please choose a number greater than three and less than five... ")) 
sOneQuizOne = Quiz(listOfStudents[0], sOneNumberOfQuestions)
sOneQuizOne.takeQuiz()

#lets student one take their second quiz                                  
print(listOfStudents[0].getFirstName(), " it is now time to take your second quiz...", sep="")
sOneNumberOfQuestions = eval(input(listOfStudents[0].getFirstName() + ", how many questions would you like? [Choose a number between 3 and 5] "))
while(sOneNumberOfQuestions > 5) or (sOneNumberOfQuestions < 3):
    sOneNumberOfQuestions = eval(input(listOfStudents[0].getFirstName() + ", please choose a number greater than three and less than five... ")) 
sOneQuizTwo = Quiz(listOfStudents[0], sOneNumberOfQuestions)
sOneQuizTwo.takeQuiz()



#lets student two take their first quiz
print(listOfStudents[1].getFirstName(), " it is now time to take your first quiz...", sep="")
sTwoNumberOfQuestions = eval(input(listOfStudents[1].getFirstName() + ", how many questions would you like? [Choose a number between 3 and 5] "))
while(sTwoNumberOfQuestions > 5) or (sTwoNumberOfQuestions < 3):
    sTwoNumberOfQuestions = eval(input(listOfStudents[1].getFirstName() + ", please choose a number greater than three and less than five... ")) 
sTwoQuizOne = Quiz(listOfStudents[1], sTwoNumberOfQuestions)
sTwoQuizOne.takeQuiz()

#lets student two take their second quiz                                  
print(listOfStudents[1].getFirstName(), " it is now time to take your second quiz...", sep="")
sTwoNumberOfQuestions = eval(input(listOfStudents[1].getFirstName() + ", how many questions would you like? [Choose a number between 3 and 5] "))
while(sTwoNumberOfQuestions > 5) or (sTwoNumberOfQuestions < 3):
    sTwoNumberOfQuestions = eval(input(listOfStudents[1].getFirstName() + ", please choose a number greater than three and less than five... ")) 
sTwoQuizTwo = Quiz(listOfStudents[1], sTwoNumberOfQuestions)
sTwoQuizTwo.takeQuiz()



#lets student three take their first quiz
print(listOfStudents[2].getFirstName(), " it is now time to take your first quiz...", sep="")
sThreeNumberOfQuestions = eval(input(listOfStudents[2].getFirstName() + ", how many questions would you like? [Choose a number between 3 and 5] "))
while(sThreeNumberOfQuestions > 5) or (sThreeNumberOfQuestions < 3):
    sThreeNumberOfQuestions = eval(input(listOfStudents[2].getFirstName() + ", please choose a number greater than three and less than five... ")) 
sThreeQuizOne = Quiz(listOfStudents[2], sThreeNumberOfQuestions)
sThreeQuizOne.takeQuiz()

#lets student three take their second quiz                                  
print(listOfStudents[2].getFirstName(), " it is now time to take your second quiz...", sep="")
sThreeNumberOfQuestions = eval(input(listOfStudents[2].getFirstName() + ", how many questions would you like? [Choose a number between 3 and 5] "))
while(sThreeNumberOfQuestions > 5) or (sThreeNumberOfQuestions < 3):
    sThreeNumberOfQuestions = eval(input(listOfStudents[2].getFirstName() + ", please choose a number greater than three and less than five... ")) 
sThreeQuizTwo = Quiz(listOfStudents[2], sThreeNumberOfQuestions)
sThreeQuizTwo.takeQuiz()



#separates and prints out student summaries
print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
for i in range(0,3):
    print("=========================================")
    print(listOfStudents[i])
    print("=========================================")
