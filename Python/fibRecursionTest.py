#Christopher Marotta
#15.7 Recursive
#January 14, 2019

fibCount = 0

def fib(num):
    global fibCount
    fibCount = fibCount + 1
    if num==1:
        result = 1
    elif num == 0:
        result = 0
    else:
        result = fib(num-1) + fib(num-2)
    return result

playAgain = True
while(playAgain):
    fibCount = 0
    chosenNumber = int(input("Please input a number and it will calculate the Fibonacci value at that index: "))
    print(fib(chosenNumber), " (Took " , fibCount, " calls to the fib function.)", sep = "")
    
