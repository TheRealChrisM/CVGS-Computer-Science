#Christopher Marotta
#Lab Assignment August 13, 2019 Problem 3

#setting main variables
ipString = ""


print("Please enter each octet of your IP as prompted to convert from decimal to binary.")
#-------------------------------------------------
#input first octet
#input
numIn = eval(input("Enter the first octet, it must be a positive integer no larger than 255: "))

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

#Add first octet to IP string
ipString += binString + "."

#-------------------------------------------------  
#input second octet
#input
numIn = eval(input("Enter the second octet, it must be a positive integer no larger than 255: "))

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

#Add second octet to IP string
ipString += binString + "."

#-------------------------------------------------
#input third octet
#input
numIn = eval(input("Enter the third octet, it must be a positive integer no larger than 255: "))

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

#Add third octet to IP string
ipString += binString + "."

#-------------------------------------------------
#input fourth octet
#input
numIn = eval(input("Enter the fourth octet, it must be a positive integer no larger than 255: "))

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

#Add fourth octet to IP string
ipString += binString

#-------------------------------------------------
#output IP in binary
print("Your IP in binary is", ipString)
    
