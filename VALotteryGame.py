#Christopher Marotta
#VA Decades for Dollars Lottery
import random


#set global variables
ballsWon = 0
ticketPrice = 2
playAgain = "y"
startBal = 10
bank = startBal
#gameloop
while (playAgain == "y" and bank>=2):
    winnings = 0
    playAgain = "n"
    bank -= 2
    #ask user for numbers
    print("Please choose 6 numbers from 1 to 47...")
    choiceOne = eval(input("Please input your first number: "))
    choiceTwo = eval(input("Please input your second number: "))
    choiceThree = eval(input("Please input your third number: "))
    choiceFour = eval(input("Please input your fourth number: "))
    choiceFive = eval(input("Please input your fifth number: "))
    choiceSix = eval(input("Please input your sixth number: "))

    #generate random numbers
    randIntOne = random.randint(1,47)
    randIntTwo = random.randint(1,47)
    randIntThree = random.randint(1,47)
    randIntFour = random.randint(1,47)
    randIntFive = random.randint(1,47)
    randIntSix = random.randint(1,47)

    #save random numbers
    randIntOneSaved = randIntOne
    randIntTwoSaved = randIntTwo
    randIntThreeSaved = randIntThree
    randIntFourSaved = randIntFour
    randIntFiveSaved = randIntFive
    randIntSixSaved = randIntSix
    
    #check choiceOne
    if ((choiceOne == randIntOne) or (choiceOne == randIntTwo) or (choiceOne == randIntThree) or (choiceOne == randIntFour) or (choiceOne == randIntFive) or (choiceOne == randIntSix)):
        ballsWon += 1
        if(choiceOne == randIntOne):
            randIntOne = -1
        elif(choiceOne == randIntTwo):
            randIntTwo = -1
        elif(choiceOne == randIntThree):
            randIntThree = -1
        elif(choiceOne == randIntFour):
            randIntFour = -1
        elif(choiceOne == randIntFive):
            randIntFive = -1
        elif(choiceOne == randIntSix):
            randIntSix = -1
        

    #check choiceTwo
    if ((choiceTwo == randIntOne) or (choiceTwo == randIntTwo) or (choiceTwo == randIntThree) or (choiceTwo == randIntFour) or (choiceTwo == randIntFive) or (choiceTwo == randIntSix)):
        ballsWon += 1
        if(choiceTwo == randIntOne):
            randIntOne = -1
        elif(choiceTwo == randIntTwo):
            randIntTwo = -1
        elif(choiceTwo == randIntThree):
            randIntThree = -1
        elif(choiceTwo == randIntFour):
            randIntFour = -1
        elif(choiceTwo == randIntFive):
            randIntFive = -1
        elif(choiceTwo == randIntSix):
            randIntSix = -1

    #check choiceThree
    if ((choiceThree == randIntOne) or (choiceThree == randIntTwo) or (choiceThree == randIntThree) or (choiceThree == randIntFour) or (choiceThree == randIntFive) or (choiceThree == randIntSix)):
        ballsWon += 1
        if(choiceThree == randIntOne):
            randIntOne = -1
        elif(choiceThree == randIntTwo):
            randIntTwo = -1
        elif(choiceThree == randIntThree):
            randIntThree = -1
        elif(choiceThree == randIntFour):
            randIntFour = -1
        elif(choiceThree == randIntFive):
            randIntFive = -1
        elif(choiceThree == randIntSix):
            randIntSix = -1

    #check choiceFour
    if ((choiceFour == randIntOne) or (choiceFour == randIntTwo) or (choiceFour == randIntThree) or (choiceFour == randIntFour) or (choiceFour == randIntFive) or (choiceFour == randIntSix)):
        ballsWon += 1
        if(choiceFour == randIntOne):
            randIntOne = -1
        elif(choiceFour == randIntTwo):
            randIntTwo = -1
        elif(choiceFour == randIntThree):
            randIntThree = -1
        elif(choiceFour == randIntFour):
            randIntFour = -1
        elif(choiceFour == randIntFive):
            randIntFive = -1
        elif(choiceFour == randIntSix):
            randIntSix = -1

    #check choiceFive
    if ((choiceFive == randIntOne) or (choiceFive == randIntTwo) or (choiceFive == randIntThree) or (choiceFive == randIntFour) or (choiceFive == randIntFive) or (choiceFive == randIntSix)):
        ballsWon += 1
        if(choiceFive == randIntOne):
            randIntOne = -1
        elif(choiceFive == randIntTwo):
            randIntTwo = -1
        elif(choiceFive == randIntThree):
            randIntThree = -1
        elif(choiceFive == randIntFour):
            randIntFour = -1
        elif(choiceFive == randIntFive):
            randIntFive = -1
        elif(choiceFive == randIntSix):
            randIntSix = -1

    #check choiceSix
    if ((choiceSix == randIntOne) or (choiceSix == randIntTwo) or (choiceSix == randIntThree) or (choiceSix == randIntFour) or (choiceSix == randIntFive) or (choiceSix == randIntSix)):
        ballsWon += 1
        if(choiceSix == randIntOne):
            randIntOne = -1
        elif(choiceSix == randIntTwo):
            randIntTwo = -1
        elif(choiceSix == randIntThree):
            randIntThree = -1
        elif(choiceSix == randIntFour):
            randIntFour = -1
        elif(choiceSix == randIntFive):
            randIntFive = -1
        elif(choiceSix == randIntSix):
            randIntSix = -1

    print()
    print("Here were the balls you picked:", end="")
    print(choiceOne, choiceTwo, choiceThree, choiceFour, choiceFive, choiceSix, sep=", ")
    print("Here are the randomly picked balls:", end="")
    print(randIntOneSaved, randIntTwoSaved, randIntThreeSaved, randIntFourSaved, randIntFiveSaved, randIntSixSaved, sep=", ")
    print("You got", ballsWon, "correct!")
    print()

    if (ballsWon == 2):
        winnings = 2
        bank += 2
    elif (ballsWon == 3):
        winnings = 10
        bank += 10
    elif (ballsWon == 4):
        winnings = 100
        bank += 100
    elif (ballsWon == 5):
        winnings = 10000
        bank +=10000
    elif (ballsWon == 6):
        winnings = 4000000
        bank += 4000000

    if (winnings-ticketPrice)>0:
        print("Congratulations! You have won $", str(winnings), "! Thanks for playing!", sep="")
    elif (winnings-ticketPrice) == 0:
        print("Congratulations! Your next ticket is on the house, here is $2!")
    else:
        print("Sorry you have lost $", str(ticketPrice), ".", sep="")


    printPlayAgain = "You currently have $" + str(bank) + ". Play again? (y/n): "
    playAgain = input(printPlayAgain)
    print()

    
print("Your final balance is $", bank, ". Congratulations!", sep="")
if bank>startBal:
    print("You gained $", (bank-startBal), ".", sep="")
elif bank==startBal:
    print("You broke even!")
elif bank<startBal:
    print("You lost $", (startBal-bank), ".", sep="")
