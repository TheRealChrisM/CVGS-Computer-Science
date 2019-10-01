#Christopher Marotta
#Lab F - Part 1
#October 1, 2019

class Vector:
    #Constructs vector object
    def __init__(self, xPointIn=0, yPointIn=0):
        self.__xPoint = xPointIn
        self.__yPoint = yPointIn
        
    #Returns the X component of a Vector
    def getX(self):
        return self.__xPoint

    #Returns the Y component of a Vector
    def getY(self):
        return self.__yPoint

    #Sets a new value to the X component of a Vector
    def setX(self, newX):
        self.__xPoint = newX
        return

    #Sets a new value to the Y component of a Vector
    def setY(self, newY):
        self.__yPoint = newY
        return

    #Overloads multiplication to follow dot product rules for Vectors
    def __mul__(self, other):
        newX = self.getX() * other.getX()
        newY = self.getY() * other.getY()
        dotProduct = newX+newY
        return dotProduct

    #Overloads addidition to sum two Vectors
    def __add__(self, other):
        newX = self.getX() + other.getX()
        newY = self.getY() + other.getY()
        return Vector(newX, newY)

    #Overloads subtraction to subtract two Vectors
    def __sub__(self, other):
        newX = self.getX() - other.getX()
        newY = self.getY() - other.getY()
        return Vector(newX, newY)

    #Overloads string function to properly format a Vector into a string
    def __str__(self):
        returnStatment = "<"
        returnStatment += str(self.getX()) + " , " + str(self.getY())
        returnStatment += ">"
        return returnStatment

#Runs test code
V1 = Vector(2,-5)
V2 = Vector(10,11)
print(V1+V2)
print(V1-V2)
print(V1*V2)
