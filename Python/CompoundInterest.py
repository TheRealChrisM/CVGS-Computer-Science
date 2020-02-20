def futureValue(p, apr, n, t):
    futureVal = (p)*((1+(apr/n))**(n*t))
    return futureVal

principle = eval(input("Please enter the starting amount: "))
annualPercent = eval(input("Please enter your APR: "))
timesCompounded  = eval(input("Please enter the number of times anually compounded: "))
time = eval(input("Please input the amount of time: "))                        
print(futureValue(principle, annualPercent, timesCompounded, time))
