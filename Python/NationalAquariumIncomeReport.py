#Christopher Marotta
#Lab Assignment 8/20/19 Part 1

#Request Information
month = input("Please enter the Month: ")
day = input("Please enter the Date: ")
year = input("Please enter the year: ")
adultSales = eval(input("How many tickets were sold to adults: "))
seniorSales = eval(input("How many tickets were sold to adults over 60 years old: "))
childSales = eval(input("How many tickets were sold to children between 3 and 11 years old: "))
toddlerSales = eval(input("How many tickets were sold to children under 3 years old: "))
totalSales = adultSales+seniorSales+childSales+toddlerSales

#calculate ticket revenue
totalRev = 0
adultRev = adultSales*21.95
seniorRev = seniorSales*20.95
childRev = childSales*12.95
toddlerRev = toddlerSales*0
totalRev = adultRev+seniorRev+childRev+toddlerRev

#calculate ticket percentages
adultPercent = format(adultSales/totalSales, "2.0%")
seniorPercent = format(seniorSales/totalSales, "2.0%")
childPercent = format(childSales/totalSales, "2.0%")
toddlerPercent = format(toddlerSales/totalSales, "2.0%")

#create string vars
adultSalesString = str(adultSales)
seniorSalesString = str(seniorSales)
childSalesString = str(childSales)
toddlerSalesString = str(toddlerSales)
totalSalesString = str(totalSales)
adultRevString = "$" + str(format(adultRev, "4.2f"))
seniorRevString = "$" + str(format(seniorRev, "4.2f"))
childRevString = "$" + str(format(childRev, "4.2f"))
toddlerRevString = "$" + str(format(toddlerRev, "4.2f"))
totalRevString = "$" + str(format(totalRev, "4.2f"))

#print table
print()
print(format("Baltimore National Aquarium", "^50s"))
print(format("Admissions Data", "^50s"))
dateString = str(month) + " " + str(day) + ", " + str(year)
print(format(dateString, "^50s"))
print()

print(format("", "<14s"), end="")
print(format("Number", "^12s"), end="")
print(format("Percent", "^12s"), end="")
print(format("Fees", ">11s"))

print(format("Adults", "<14s"), end="")
print(format(adultSalesString, "^12s"), end="")
print(format(adultPercent, "^12s"), end="")
print(format(adultRevString, ">12s"))

print(format("Adults 60+", "<14s"), end="")
print(format(seniorSalesString, "^12s"), end="")
print(format(seniorPercent, "^12s"), end="")
print(format(seniorRevString, ">12s"))

print(format("Children 3-11", "<14s"), end="")
print(format(childSalesString, "^12s"), end="")
print(format(childPercent, "^12s"), end="")
print(format(childRevString, ">12s"))

print(format("Children <3", "<14s"), end="")
print(format(toddlerSalesString, "^12s"), end="")
print(format(toddlerPercent, "^12s"), end="")
print(format(toddlerRevString, ">12s"))

print()
print(format("Total", ">12s"), end="")
print(format(totalSalesString, "^15s"), end="")
print(format("", "11s"), end="")
print(format(totalRevString, ">12s"))
