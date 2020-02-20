#Christopher Marotta
#Mean and Standard Deviation Calculator
import math
totalNums = 0
totalSum = 0
totalSumSquared = 0
numIn = 0

print("Welcome to the Mean/Deviation Calculator! Enter all of your numbers and then press 'n' when you are finished!")
while (numIn != "n"):
    numIn = input("Please input a number: ")
    if numIn != "n":
        totalNums += 1
        totalSum += eval(numIn)
        totalSumSquared +=eval(numIn)*eval(numIn)
mean = totalSum/totalNums
sd = math.sqrt((totalSumSquared - ((totalSum*totalSum)/totalNums))/(totalNums-1))

print("The mean is: ", mean, sep="")
print("The Standard Deviation is: ", sd, sep="")
