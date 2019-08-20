#Christopher Marotta
#Lab Assignment August 13, 2019 Problem 2

#input
numIn = eval(input("Enter a positive integer no larger than 255: "))

#calculations
binString = ""

binString += str(numIn//128)
numIn %= 128
binString += str(numIn//64)
numIn %= 64
binString += str(numIn//32)
numIn %= 32
binString += str(numIn//16)
numIn %= 16
binString += str(numIn//8)
numIn %= 8
binString += str(numIn//4)
numIn %= 4
binString += str(numIn//2)
numIn %= 2
binString += str(numIn//1)

#output

print("The binary number for your input is", binString)

