#Christopher Marotta
#Random Numbers

import random
import time

x = 1

while x == 1:
    for i in range(50):
        print(random.randint(0,9), sep="",end="")
        time.sleep(.01)
    print("\n", sep="", end="")
    
