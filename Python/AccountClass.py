#Christopher Marotta
#Lab E Part 2 (Account Class)

class Account:
    #Sets up the Account Object
    def __init__(self, newID=0, startingBal = 100.00, startingAnnualInterestRate = 0.00):
        self.__id = newID
        self.__balance = startingBal
        self.__annualInterestRate = startingAnnualInterestRate

    #Returns the ID of the account.
    def getID(self):
        return self.__id

    #Returns the current Balance of the account.
    def getBalance(self):
        return self.__balance

    #Returns the Annual Interest Rate for the account.
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    #Sets a new ID for the account.
    def setID(self, newID):
        self.__id = newID
        return

    #Sets a new Balance for the account.
    def setBalance(self, newBalance):
        self.__balance = newBalance
        return

    #Sets a new Annual Interest Rate for the account.
    def setAnnualInterestRate(self, newAnnualInterestRate):
        self.__annualInterestRate = newAnnualInterestRate
        return

    #Returns the Monthly Interest Rate for the account.
    def getMonthlyInterestRate(self):
        return ((self.getAnnualInterestRate()/100) / 12)

    #Returns the Monthly Interest for the account.
    def getMonthlyInterest(self):
        return (self.getBalance() * self.getMonthlyInterestRate())

    #Withdrawns n ammount of money from the account.
    def withdraw(self, n=0):
        newBalance = self.getBalance() - n
        self.setBalance(newBalance)
        return

    #Deposits n ammount of money to the account.
    def deposit(self, n=0):
        newBalance = self.getBalance() + n
        self.setBalance(newBalance)
        return

    #Overloads the str method to return important account information.
    def __str__(self):
        returnStatement = "ID" + str(self.getID()) + ": \n"
        returnStatement += "    Balance: $" + str(format(self.getBalance(), ".2f")) + "\n"
        returnStatement += "    Monthly Interest Rate: " + str(self.getMonthlyInterestRate()) + "\n"
        returnStatement += "    Monthly Interest: " + str(self.getMonthlyInterest())
        return returnStatement

#Constructs the Account Object with set parameters.
x = Account(1122, 20000, 4.5)
#Withdraws $2,500
x.withdraw(2500)
#Deposits $3,000
x.deposit(3000)
#Makes sure that the getMonthlyInterestRate function works.
x.getMonthlyInterestRate()
#Makes sure that the getMonthlyInterest function works.
x.getMonthlyInterest()
#Prints out account information.
print("Fetching account information for ID" + str(x.getID()) + "...")
print(x)
