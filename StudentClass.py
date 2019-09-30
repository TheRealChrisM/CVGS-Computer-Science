class Student:
    def __init__(self, fName="", lName=""):
        self.__firstName = fName
        self.__lastName = lName
        self.__testScores = [0,0,0]
        return

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getTestScore(self,num):
        num = num - 1
        return self.__testScores[num]

    def setFirstName(self, newName):
        self.__firstName = newName
        return

    def setLastName(self, newName):
        self.__lastName = newName
        return

    def setTestScore(self, testNum, newScore):
        testNum = testNum - 1
        self.__testScores[testNum] = newScore
        return

    def returnTestAverage(self):
        x = 0
        scoreTotal = 0
        while(x<=2):
            scoreTotal += self.getTestScore(x)
            x += 1
        return scoreTotal/3
