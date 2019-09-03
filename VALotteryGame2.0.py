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
    #setup round-specific variables
    chosenNums = []
    randomNums = []
    winnings = 0
    playAgain = "n"
    bank -= 2
    
    #ask user for numbers
    print("Please choose 6 different numbers from 1 to 47...")
    chosenNums.append(eval(input("Please input your first number: ")))
    chosenNums.append(eval(input("Please input your second number: ")))
    chosenNums.append(eval(input("Please input your third number: ")))
    chosenNums.append(eval(input("Please input your fourth number: ")))
    chosenNums.append(eval(input("Please input your fifth number: ")))
    chosenNums.append(eval(input("Please input your sixth number: ")))

    #creates an array of random numbers
    randomNums.append(random.randint(1,47))
    numsGenerated = 1
    while (numsGenerated < 6):
        randIntTemp = random.randint(1,47)
        if (randIntTemp not in randomNums):
            randomNums.append(randIntTemp)
            numsGenerated += 1
    
    
    #compare chosen numbers and random numbers
    curCheck = 0
    while(len(chosenNums)>curCheck):
        if (chosenNums[curCheck] in randomNums):
            ballsWon += 1
        curCheck +=1

    print()
    print("Here were the balls you picked: ", end="")
    print(chosenNums, sep=", ")
    print("Here are the randomly picked balls: ", end="")
    print(randomNums, sep=", ")
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
