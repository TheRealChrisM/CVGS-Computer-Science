#Christopher Marotta
#Mersenne Prime Finder (Pg. 209 6.26)

def isPrime(number):
    divideBy = 2
    curNum = number
    isPrime = True
    while (divideBy <= number**.5) and (number != 2) and (isPrime):
        if (curNum % divideBy == 0):
            isPrime = False
        divideBy = divideBy + 1
            
    return isPrime

def mersennePrimeCalc(number):
    mCalc = ((2**number)-1)
    return mCalc

#print out all Mersenne Primes up to 31
curNum = 2
endOnNum = 31
print(format("p", "^10s"), format("2^p - 1", "^10s"), sep="")
while(curNum <= endOnNum):
    if(isPrime(mersennePrimeCalc(curNum))):
        print(format(curNum, "^10d"), format(mersennePrimeCalc(curNum), "^10d"), sep="")
        curNum = curNum + 1
    else:
        curNum = curNum + 1
