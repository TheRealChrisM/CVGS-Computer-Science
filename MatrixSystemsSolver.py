#Christopher Marotta and Andrew Dunlop
#Lab G - Solving Systems of Equations with Matrix
#October 8th, 2019

class matrix:
    def __init__(self, row, column):
        self.__matrix = [row,column]
        self.__row = len(self.__matrix)
        self.__column = len(self.__matrix[0])

    def getRow(self):
        return self.__row

    def getCol(self):
        return self.__column

    def getMatrix(self):
        return self.__matrix

    def setRow(self, newRow):
        self.__row = len(newRow)
        return

    def setCol(self, newCol):
        self.__column = len(newCol)
        return

    def getEntry(self, row, col):
        return self.__matrix[row][col]

    def setEntry(self, row, col, value):
        self.__matrix[row][col] = value
        return
        
    def determinant(self):
        deter = (self.__matrix[0][0] * self.__matrix[1][1]) - (self.__matrix[0][1] * self.__matrix[1][0])
        return deter

    def canMultiply(self, other):
        canMul = False
        if self.getCol() == other.getRow():
            canMul = True
        return canMul


    def __mul__(self, other):
        rowOfNew = []
        colOfNew = []
        valToAppend = 0
        if self.canMultiply(other):
            #Make the lists to put into Matrix() that are the right sizes
            for a in range(other.getCol()):
                rowOfNew.append(a)
            for b in range(self.getRow()):
                colOfNew.append(b)
            #Create the resulting matrix of the right dimensions
            result = matrix(rowOfNew, colOfNew)
            #iterate through rows of self
            for i in range(self.getRow()):
                #iterate through columns of other
                for j in range(other.getCol()):
                    valToAppend = 0
                    #iterate through rows of other
                    for k in range(other.getRow()):
                        valToAppend += (self.getMatrix()[i][k] * other.getMatrix()[k][j])
                        result.setEntry(i,j,valToAppend)

        else:
            result = None
            print("Cannot be Multiplied")
        return result

    def __str__(self):
        returnString = ""
        for i in range(self.getRow()):
            if i == 1:
                returnString += "\n"
            for j in range(self.getCol()):
                returnString += (format(self.getEntry(i,j), "5.2f"))
        return returnString
#Checks to see if matrix is non-singular. Returns true if non-singular, false if singular.
def DoesSolutionExist(matrixIn):
    determinantValue = matrixIn.determinant()
    isSingular = True
    #If the determinant is not equal to 0, isSingular will become false
    if not (determinantValue == 0):
        isSingular = False
    #Returns the opposite of isSingular to represent the status of a non-singular number.
    return (not isSingular)

#Calculates the solution of a system of equations which are put into matrix form.
def SystemSolution(coefficientMatrix, constantMatrix):
    inverseCoefficientMatrix = Inverse(coefficientMatrix)
    matrixOut = inverseCoefficientMatrix*constantMatrix
    return matrixOut

#Returns the inverse of the matrix input as matrixIn into the function.
def Inverse(matrixIn):
    #Finds out the determinant for the input matrix.
    determinantValue = matrixIn.determinant()
    #Uses the determinant to find the coefficient used to calculate the inverse.
    coefficient = 1/determinantValue
    #Calculates the new row of the inverse matrix.
    newRow = [(coefficient*matrixIn.getEntry(1,1)), ((-1)*(coefficient*matrixIn.getEntry(0,1)))]
    #Calculates the new column of the inverse matrix.
    newCol = [((-1)*(coefficient*matrixIn.getEntry(1,0))), (coefficient*matrixIn.getEntry(0,0))]
    #Creates a new matrix.
    matrixOut = matrix(newRow, newCol)
    return matrixOut

#Main code
#Get matrix entries -> Validate entries -> Create objects -> If they exist, call SystemSolution -> Output Results
print("Welcome to the Systems of Equations Solver featuring Matrices!")
print("Please convert your two functions into a format of nx + my = c")
print("First, we need to get the coefficents for the first equation...")
xEqOne = eval(input("What is the value of n? "))
yEqOne = eval(input("What is the value of m? "))
cEqOne = eval(input("What is the value of c? "))
print("Great! Now let's move on to your second equation...")
xEqTwo = eval(input("What is the value of n? "))
yEqTwo = eval(input("What is the value of m? "))
cEqTwo = eval(input("What is the value of c? "))



rowMatrixA = [xEqOne, yEqOne]
colMatrixA = [xEqTwo, yEqTwo]
matrixA = matrix(rowMatrixA, colMatrixA)

validMatrix = DoesSolutionExist(matrixA)

rowMatrixC = [cEqOne]
colMatrixC = [cEqTwo]
matrixC = matrix(rowMatrixC, colMatrixC)

if validMatrix:
    result = SystemSolution(matrixA, matrixC)

    print("Here is the resulting matrix:")
    print(result)
    print("Therefore...")
    print("x equals: ", format((result.getEntry(0,0)), ".2f"), sep="")
    print("y equals: ", format((result.getEntry(1,0)), ".2f"), sep="")
else:
    print("Sorry this is not a valid matrix.")

