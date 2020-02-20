#Christopher Marotta
#Endless Multiplication Quiz

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
print("Questions Attempted:", (totalQuestions-1))
print("Questions Correct:", currScore)
grade = currScore/(totalQuestions-1)
if grade > .89:
    print("You recieved an A with a score of", format(grade,"2.0%"))
elif grade > .79:
    print("You recieved a B with a score of", format(grade,"2.0%"))
elif grade > .69:
    print("You recieved a C with a score of", format(grade,"2.0%"))
elif grade > .59:
    print("You recieved a D with a score of", format(grade,"2.0%"))
elif grade <= .59:
    print("You recieved a F with a score of", format(grade,"2.0%"))
    
        
