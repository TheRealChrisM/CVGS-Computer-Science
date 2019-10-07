import random

class Player:
    def __init__(self, fn="First", ln="Last", bal=10):
        self.__firstName = fn
        self.__lastName = ln
        self.__balance = bal
        self.__cardHand = []
        return
    #Getter and Setter methods
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getCardHand(self):
        cardHandTemp = []
        for i in range(len(self.__cardHand)):
            cardHandTemp.append(self.__cardHand[i].getNumber())
        return cardHandTemp

    def getBalance(self):
        return self.__balance

    def setBalance(self, newBal):
        self.__balance = newBal
        return

    def setFirstName(self, newName):
        self.__firstName = newName
        return

    def setLastName(self, newName):
        self.__lastName = newName
        return
    
    def discardHand(self):
        self.__cardHand.clear()
        return

    #Adds a card to a player's hand
    def setCardHand(self, newVal):
        self.__cardHand.append(newVal)
        return

    #Returns the player's current hand
    def showHand(self):
        cardReturn = "\n"
        for card in self.__cardHand:
            cardReturn += str(card) + "\n"
        return cardReturn

    def totalCardValue(self):
        cardValue = 0
        for card in self.__cardHand:
            cardValue += card.getValue()
        return cardValue
        
class Card:
    def __init__(self, number):
        self.__cardNum = number

    def getNumber(self):
        return self.__cardNum

    def getValue(self):
        cardVal = self.getNumber()%13
        return cardVal + 1
    
    #returns a string of the suit of the card
    def findSuit(self):
        suitNo = self.getNumber()//13
        suitName = "SUITERR"
        if (suitNo == 0):
            suitName = "Hearts"
        elif (suitNo == 1):
            suitName = "Diamonds"
        elif (suitNo == 2):
            suitName = "Clubs"
        elif (suitNo == 3):
            suitName = "Spades"
        return suitName
    
    #returns a string of the face value of the card
    def findFace(self):
        faceNo = (self.getNumber()+1)%13
        faceName = "FACEERR"
        if (faceNo == 1):
            faceName = "Ace"
        elif (faceNo == 11):
            faceName = "Jack"
        elif (faceNo == 12):
            faceName = "Queen"
        elif (faceNo == 0):
            faceName = "King"
        elif ((faceNo > 1) and (faceNo < 11)):
            faceName = str(faceNo)
        return faceName

    #returns the string of the common identifier for a card
    def __str__(self):
        returnString = self.findFace() + " of " + self.findSuit()
        return returnString

#Returns a random number between 0 and 51 which will represent drawing a card.
def draw():
    card = random.randint(0,51)
    return card

#Returns a boolean which is True if card has been selected and false if it has not been selected.
def isDrawn(card):
    return cardsDrawn[card]

#Resets the cards which have been drawn to represent a shuffling of the deck.
def shuffle():
    for i in range(52):
        cardsDrawn[i] = False
    
#Takes in a Player object along with a desired amount of cards and deals that amount of cards to the player.    
def deal(cardList, numCards):
    i = numCards
    while(i>0) and (False in cardsDrawn):
        drewCard = draw()
        if not(isDrawn(drewCard)):
            cardList.setCardHand(Card(drewCard))
            cardsDrawn[drewCard] = True
            i = i-1
    return

#Creates an empty list which will be used to track which cards have been drawn
cardsDrawn = []

#Fills indexes 0-51 with the boolean False representing an unpicked card
for i in range(52):
    cardsDrawn.append(False)

#Takes in the names of both players
playerOneFirstName = input("What is Player 1's first name? ")
playerOneLastName = input("What is Player 1's last name? ")
playerTwoFirstName = input("What is Player 2's first name? ")
playerTwoLastName = input("What is player 2's last name? ")

#Constructs a player object based on the names provided
playerOne = Player(playerOneFirstName, playerOneLastName)
playerTwo = Player(playerTwoFirstName, playerTwoLastName)

#Sets the round counter equal to 0
roundNo = 0

#Displays the balance of both players before the game begins
print()
print("-------------------")
print(playerOne.getFirstName()," ", playerOne.getLastName(), "'s Balance: ", playerOne.getBalance(),sep="")
print(playerTwo.getFirstName()," ", playerTwo.getLastName(), "'s Balance: ", playerTwo.getBalance(),sep="")
print("-------------------")
print()

while((playerOne.getBalance()>0) and (playerTwo.getBalance()>0)):
    if(roundNo<=13):
           
        if((roundNo%2)==0):
            startingPlayer = playerOne
            followingPlayer = playerTwo
        else:
            startingPlayer = playerTwo
            followingPlayer = playerOne
        deal(startingPlayer, 1)
        deal(followingPlayer, 1)

        print(startingPlayer.getFirstName(), "here is your hand. How much would you like to bet?")
        print("************************")
        print(startingPlayer.showHand())
        print("************************")
        print()
        
        betQuestion = startingPlayer.getFirstName() + " please input the amount you would like to bet: "
        betAmount = eval(input(betQuestion))

        if (betAmount > startingPlayer.getBalance()):
            print(startingPlayer.getFirstName(), "has bet greater than their current balance. The bet has now been set to their total balance.")
            betAmount = startingPlayer.getBalance()

        print()
        print(followingPlayer.getFirstName(), " here is your hand. ", startingPlayer.getFirstName(), " has bet ", betAmount, ".", sep="")
        print("************************")
        print(followingPlayer.showHand())
        print("************************")
        print()
        
        acceptBetQuestion = followingPlayer.getFirstName() + " do you accept " + startingPlayer.getFirstName() + "'s bet(y = yes | n = no)? "
        acceptBet = input(acceptBetQuestion)

        if (acceptBet == "y"):
            deal(startingPlayer, 1)
            deal(followingPlayer, 1)
            
            print()
            print(startingPlayer.getFirstName(), "'s hand:")
            print("************************")
            print(startingPlayer.showHand())
            print("************************")
            print()
            print(followingPlayer.getFirstName(), "'s hand:")
            print("************************")
            print(followingPlayer.showHand())
            print("************************")
            print()
            
            if (playerOne.totalCardValue() > playerTwo.totalCardValue()):
                winner = playerOne
                loser = playerTwo

                print(winner.getFirstName(), " has won! ", loser.getFirstName(), " will pay them $", betAmount, ".", sep="")
                print()
                newLoserBal = loser.getBalance() - betAmount
                newWinnerBal = winner.getBalance() + betAmount
                loser.setBalance(newLoserBal)
                winner.setBalance(newWinnerBal)

                startingPlayer.discardHand()
                followingPlayer.discardHand()
                
            elif (playerOne.totalCardValue() < playerTwo.totalCardValue()):
                winner = playerTwo
                loser = playerOne

                print(winner.getFirstName(), " has won! ", loser.getFirstName(), " will pay them $", betAmount, ".", sep="")
                print()
                newLoserBal = loser.getBalance() - betAmount
                newWinnerBal = winner.getBalance() + betAmount
                loser.setBalance(newLoserBal)
                winner.setBalance(newWinnerBal)

                startingPlayer.discardHand()
                followingPlayer.discardHand()
                  
            else:
                print("Both players have tied!")

                startingPlayer.discardHand()
                followingPlayer.discardHand()
            roundNo = roundNo + 1
        else:
            newBal = followingPlayer.getBalance() - 1
            followingPlayer.setBalance(newBal)
            startingPlayer.discardHand()
            followingPlayer.discardHand()
            roundNo = roundNo + 1
    #else:
        #shuffle code
