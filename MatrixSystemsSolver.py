#Christopher Marotta and Andrew Dunlop
#Lab G - Solving Systems of Equations with Matrix
#October 8th, 2019

class matrix:
    def __init__(self, row, column):
        return
    
    def getEntry():
        return
    
    def setEntry():
        return
    
    def __mult__():
        return
    
    def __str__():
        return
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
    matrixOut = inverseCoefficentMatrix*constantMatrix
    return matrixOut

#Returns the inverse of the matrix input as matrixIn into the function.
def Inverse(matrixIn):
    #Finds out the determinant for the input matrix.
    determinantValue = matrixIn.determinant()
    #Uses the determinant to find the coefficient used to calculate the inverse.
    coefficient = 1/determinantValue
    #Calculates the new row of the inverse matrix.
    newRow = [(coefficient*matrixIn[1][1]), ((-1)*(coefficient*matrixIn[0][1]))]
    #Calculates the new column of the inverse matrix.
    newCol = [((-1)*(coefficient*matrixIn[1][0])), (coefficient*matrixIn[0][0])]
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
colMatrixA = [xEqTwo, y,EqTwo]
matrixA = matrix(rowMatrixA, colMatrixA)

validMatrix = doesSolutionExist(matrixA)

rowMatrixC = [cEqOne]
colMatrixC = [cEqTwo]
matrixC = matrix(rowMatrixC, colMatrixC)

if validMatrix:
    result = SystemSolution(matrixA, matrixC)

    print("Here is the resulting matrix: \n")
    print(result)
    print("Therefore the solution of ""x"" for this equation is ", result.getEntry(0,0)," and the solution for ""y"" is ", result.getEntry(1,0),".")

else:
    print("Sorry this is not a valid matrix.")

