#Christopher Marotta
#Lab Assignment 8/20/19 Part 2

#import modules
import random

#global variables
numCorrect = 0

#Generate first problem
firstNum = random.randint(1,9)
secondNum = random.randint(1,9)
#print first problem
problem = str(firstNum) + " x " + str(secondNum) + " = "
answer = eval(input(problem))
#check first problem
if answer == (firstNum*secondNum):
    numCorrect = numCorrect + 1

#Generate second problem
firstNum = random.randint(1,9)
secondNum = random.randint(1,9)
#print second problem
problem = str(firstNum) + " x " + str(secondNum) + " = "
answer = eval(input(problem))
#check second problem
if answer == (firstNum*secondNum):
    numCorrect = numCorrect + 1

#Generate third problem
firstNum = random.randint(1,9)
secondNum = random.randint(1,9)
#print third problem
problem = str(firstNum) + " x " + str(secondNum) + " = "
answer = eval(input(problem))
#check third problem
if answer == (firstNum*secondNum):
    numCorrect = numCorrect + 1

#Generate fourth problem
firstNum = random.randint(1,9)
secondNum = random.randint(1,9)
#print fourth problem
problem = str(firstNum) + " x " + str(secondNum) + " = "
answer = eval(input(problem))
#check fourth problem
if answer == (firstNum*secondNum):
    numCorrect = numCorrect + 1

#Generate fifth problem
firstNum = random.randint(1,9)
secondNum = random.randint(1,9)
#print fifth problem
problem = str(firstNum) + " x " + str(secondNum) + " = "
answer = eval(input(problem))
#check fifth problem
if answer == (firstNum*secondNum):
    numCorrect = numCorrect + 1

#calculate score
score = numCorrect/5
simplifiedScore = format(score, "2.0%")

#print score
if score >= .89:
    print()
    print("Congratulations!")
    print("You got an A with a score of", simplifiedScore)
elif score >= .79:
    print()
    print("Nice Work!")
    print("You got an B with a score of", simplifiedScore)
elif score >= .69:
    print()
    print("You might need a bit of practice!")
    print("You got an C with a score of", simplifiedScore)
elif score >= .59:
    print()
    print("Uh oh!")
    print("You got an D with a score of", simplifiedScore)
else:
    print()
    print("You might need a bit of practice!")
    print("You got an F with a score of", simplifiedScore)
