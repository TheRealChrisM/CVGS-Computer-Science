#Christopher Marotta
#Pascal's Triangle Creator

rowSize = 9
maxSize = 5
sideInput = -1
curSize = 1

#prompt user to input the desired size of Pascal's Triangle
while (sideInput > maxSize) or (sideInput <= 0):
    sideInput = eval(input("How many rows would you like for this triangle to be? [1-5]: "))

#Print first row
print(format("1", "^9s"))
                     
while curSize < sideInput:
    if curSize == 1:
        print(format("1 1", "^9s"))
        curSize += 1
    if curSize == 2:
        print(format("1 2 1", "^9s"))
        curSize += 1
    if curSize == 3:
        print(format("1 3 3 1", "^9s"))
        curSize += 1
    if curSize == 4:
        print(format("1 4 6 4 1", "^9s"))
        curSize += 1
