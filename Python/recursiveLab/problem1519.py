#Christopher Marotta
#15.4 Recursive
#January 14, 2019

def decimalToBinary(value):
    if int(value)==1:
        num = 1
    else:
        num = str(decimalToBinary(value/2)) + str(int(value%2))
    return num


print(decimalToBinary(12))
print(decimalToBinary(128))
print(decimalToBinary(64))
print(decimalToBinary(18))

goAgain = True
while(goAgain):
    inputNum = int(input("Please input a decimal to be converted to binary: "))
    print(str(inputNum), " in Binary is : ", decimalToBinary(inputNum), sep = "")
    checkPlayAgain = input("Play again? Y/N")
    if (checkPlayAgain == "N"):
        playAgain = False
