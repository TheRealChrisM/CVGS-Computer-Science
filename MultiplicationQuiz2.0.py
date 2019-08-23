#Christopher Marotta
#Endless Multiplication Quiz

#Made a multiplication quiz that keeps going with a question if they wanna play again
#Right = congratulations | wrong = tell answer

#import stuff
import random

#set global vars
currScore = 0
totalQuestions = 1
keepPlaying = "y"

#Game loop
while keepPlaying == "y":
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    printStr = str(totalQuestions) + ") " + str(num1) + " * " + str(num2) + " = "
    answer = eval(input(printStr))
    if answer == (num1*num2):
        currScore += 1
        print("Congratulations! You got the question right!")
    else:
        print("Sorry, that is not the correct answer! The correct answer is: ", (num1*num2), sep="")
    totalQuestions += 1
    keepPlaying = input("Would you like another question? (y/n): ")

#display final score
print("======Final Score======")
        
