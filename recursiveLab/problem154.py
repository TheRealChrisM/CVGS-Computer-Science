#Christopher Marotta
#15.4 Recursive
#January 14, 2019

def f(x):
    if x == 1:
        returnNum = 1
    else:
        returnNum = (1/x) + f(x-1)
    return returnNum

print(f(5))
print(f(2))
print(f(1))
