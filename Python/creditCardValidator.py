#Christopher Marotta and Andrew Dunlop
#9/17/19
#Lab D - pg.210 6.29 (Credit Card Validator)

number = input("Enter Credit Card Number: ")

#adds the double of every second digit from right to left
def sumOfDoubleEvenPlace(number):
    newNum = 0
    for i in range(getSize(number)-2, -1, -2):
        newNum += getDigit(eval(number[i]) * 2)
        
    return newNum



#checks to see if number is single or double digit
#if double, it return the two digits added together
def getDigit(number):
    number = str(number)
    if getSize(number) == 2:
        newDigits = eval(number[0]) + eval(number[1])
    else:
        newDigits = eval(number)
        
    return newDigits



#checks to see if the number is a valid credit card number
def isValid(number):
    
    #variable for prefix check
    preValid = False
    #variable for sum divisible by 10 check
    sumValid = False

    #checks for credit card length
    if getSize(number) >= 13 and getSize(number) <= 16:
        #Checks all of the prefixes
        if prefixMatched(number, 4):
            preValid = True
       
        elif prefixMatched(number, 5):
            preValid = True

        elif prefixMatched(number, 37):
            preValid = True

        elif prefixMatched(number, 6):
            preValid = True

        #Checks that the odds and evens are divisible by 10
        if (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0:
            sumValid = True
            
    return sumValid and preValid



# Return sum of odd place digits in number
def sumOfOddPlace(number):
    returnVar = 0 #Variable to be returned by the function
    
    #creates a list of numbers from the odd places
    for i in range(len(number)-1, 0, -2):
        #adds odd digits together
        returnVar += eval(number[i])

    #returns returnVar
    return returnVar



# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    cardString = str(number) #turns the credit card number into a string
    prefixString = str(d) #turns prefix into a string
    prefixLength = len(prefixString) #gets length of prefix
    cardPrefix = "" #prepares the cardPrefix for numbers to be added
    
    #adds the amount of numbers equal to the length of the prefix input to
    #to a string
    for i in range(0, prefixLength):
        cardPrefix += cardString[i]

    return prefixString == cardPrefix


    
# Return the number of digits in d
def getSize(d):
    dStr = str(d) #turns d into a string
    #returns the size of dStr which returns the size of the list of chars
    #in dStr
    
    return len(dStr)



#prints out whether the credit card number is valid
if isValid(number):
    print("The credit card number (",number,") is valid!", sep="")
else:
    print("The credit card number (",number,") is invalid!", sep="")
