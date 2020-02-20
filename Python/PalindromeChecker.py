#Christopher Marotta
#9/15/19
#6.3 Palindrome Checker

#Return the reversal of an integer, e.g. reverse(456) returns
def reverse(number):
    number = str(number)
    inverseInt = []
    x = len(number)-1
    while(x>0):
        inverseInt.append(number[x])
        x = x - 1
    inverseInt.append(number[0])
    x = 0
    returnString = ""
    while(x<len(inverseInt)):
        returnString += inverseInt[x]
        x = x + 1
    return eval(returnString)

#Return true if number is a palindrome
def isPalindrome(number):
    return (number == reverse(number))

x = eval(input("Please enter an Integer: "))
if(isPalindrome(x)):
    print("Your number (",x,") is a palindrome!", sep="")
else:
    print("Your number (",x,") is not a palindrome!", sep="")
