#Christopher Marotta
#January 21, 2019
#Iterative Binary Search

def find(listInput, targetNumber):
    listBegin = 0
    listEnd = len(listInput)-1
    returnNum = -1
    if (listBegin > listEnd):
        returnNum = -1
    elif (listBegin <= listEnd):
        middleIndex = (listBegin+listEnd)//2
        middleNumber = listInput[middleIndex]
        if (middleNumber == targetNumber):
            returnNum = middleIndex
        elif (middleNumber > targetNumber):
            newList = listInput[:middleIndex]
            returnNum = find(newList, targetNumber)
        elif (middleNumber < targetNumber):
            newList = listInput[middleIndex+1:]
            returnedNum = find(newList, targetNumber)
            if(returnedNum >= 0):
                returnNum = returnedNum+middleIndex+1
            else:
                returnNum = -1
    return returnNum

testList = [1,2,3,4,5,6,7]
print("RESULT [1]:", find(testList, 1))
print("RESULT [2]:", find(testList, 2))
print("RESULT [3]:", find(testList, 3))
print("RESULT [4]:", find(testList, 4))
print("RESULT [5]:", find(testList, 5))
print("RESULT [6]:", find(testList, 6))
print("RESULT [7]:", find(testList, 7))
print("RESULT [8]:", find(testList, 8))
print("RESULT [0]:", find(testList, 0))

