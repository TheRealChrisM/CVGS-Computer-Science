# Christopher Marotta
# pg 57 #2.9

#input section
tempIn = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
windSpeedIn = eval(input("Enter the wind speed in miles per hour: "))

#calculation



windChill = 35.74 + (.6215*tempIn) - (35.75*(windSpeedIn**.16)) + (.4275*tempIn*(windSpeedIn**.16))

#output
print("The wind chill index is", windChill)
