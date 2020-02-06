#Recursion

def factorial(n):
    if n == 1:
        result = 1
    else:
        result = n * factorial(n-1)

    return result

print("4! = ", factorial(4), sep ="")
