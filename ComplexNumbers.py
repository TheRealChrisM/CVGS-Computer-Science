class ComplexNumbers:
    def __init__(self, r = 0, i = 0):
        self.__real = r
        self.__imaginary = i
        return

    def getReal(self):
        return self.__real

    def getImaginary(self):
        return self.__imaginary

    def __str__(self):
        returnStatement = str(self.__real) + " + " + str(self.__imaginary) + "i"
        return returnStatement

    def __add__(self, other):
        realNums = self.getReal() + other.getReal()
        imaginaryNums = self.getImaginary() + other.getImaginary()
        return(ComplexNumbers(realNums, imaginaryNums))
