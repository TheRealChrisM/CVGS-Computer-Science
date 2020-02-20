#Christopher Marotta
#Financial Application: Payroll

#Collect Information
eName = input("Enter employee's name: ")
hoursWorked = eval(input("Enter number of hours worked in a week: "))/1
payRate = eval(input("Enter hourly pay rate: "))/1
fedTaxRate = eval(input("Enter federal tax witholding rate: "))
stateTaxRate = eval(input("Enter state tax witholding rate: "))

#print general info
print("\nEmployee Name: ", eName, sep="")
print("Hours Worked: ", hoursWorked, sep="")
print("Pay Rate: $", format(payRate, ".2f"), sep="")
grossPay = payRate*hoursWorked
print("Gross Pay: $", format(grossPay,".2f") , sep="")

#print deduction info
print("Deductions:")
fedWitheld = grossPay * fedTaxRate
print("  Federal Witholding (",format(fedTaxRate, "3.1%"), "): $", format(fedWitheld, ".2f"), sep="")
stateWitheld = grossPay * stateTaxRate
print("  State Witholding (",format(stateTaxRate, "3.1%"), "): $", format(stateWitheld, ".2f"), sep="")
totalWitheld = fedWitheld + stateWitheld
print("  Total Deduction: $", format(totalWitheld, ".2f"), sep="")
netPay = grossPay-totalWitheld
print("Net Pay: $", format(netPay, "4.2f"), sep="")
