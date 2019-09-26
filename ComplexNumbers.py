class ComplexNumbers:
    def __init__(self, r = 0, i = 0):
        self.__real = r
        self.__imaginary = i
        return

    def getReal(self):
        return self.__real

    def getImaginary(self):
        return self.__imaginary

    def setReal(self, newReal):
        self.__real = newReal

    def setImaginary(self, newImaginary):
        self.__imaginary = newImaginary

    def abs(self):
        a = self.getReal()
        b = self.getImaginary()
        c = (a**2 + b**2)**.5
        return c
    
    def __str__(self):
        returnStatement = str(self.getReal()) + " + " + str(self.getImaginary()) + "i"
        return returnStatement

    def __add__(self, other):
        realNums = self.getReal() + other.getReal()
        imaginaryNums = self.getImaginary() + other.getImaginary()
        return(ComplexNumbers(realNums, imaginaryNums))

    def __sub__(self, other):
        realNums = self.getReal() - other.getReal()
        imaginaryNums = self.getImaginary() - other.getImaginary()
        return(ComplexNumbers(realNums, imaginaryNums))

    def __mul__(self, other):
        realNums = (self.getReal()*other.getReal()) - (self.getImaginary()*other.getImaginary())
        imaginaryNums = (self.getReal()*other.getImaginary())+(other.getReal()*self.getImaginary())
        return(ComplexNumbers(realNums,imaginaryNums))

    def __truediv__(self,other):
        realMult = (self.getReal()*other.getReal()) + (self.getImaginary()*other.getImaginary())
        realSquare = (other.getReal()**2) + (other.getImaginary()**2)
        realCombined = realMult/realSquare
        realImagCombined = self.getImaginary()*other.getReal() - self.getReal()*other.getImaginary()
        realImagImagSquaredCombined = realImagCombined/realSquare
        return ComplexNumbers(realCombined, realImagCombined)
