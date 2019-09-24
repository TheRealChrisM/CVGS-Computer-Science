class Rectangle:
    def __init__(self, L = 1, W = 1):
        self.__length = L
        self.__width = W
        return

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def setLength(self, newLength):
        self.__length = newLength
        return

    def setWidth(self, newWidth):
        self.__width = newWidth
        return

    def getPerimeter(self):
        return (2*self.getWidth())+(2*self.getLength())

    def getArea(self):
        return self.getWidth()*self.getLength()

    def __str__(self):
        returnStatement = "A Rectangle with a Width of " + str(self.getWidth()) + " and Length of " + str(self.getLength()) + "."
        returnStatement += " (Area: " + str(self.getArea()) + " Perimeter: " + str(self.getPerimeter()) + ")"
        return returnStatement
