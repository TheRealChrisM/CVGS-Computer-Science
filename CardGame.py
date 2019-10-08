#Christopher Marotta
#October 8th, 2019
#Description: Allows two players to play against each other in a "simplified Blackjack-ish game" along with  
#             also having the framework needed to allow for more advanced card games to be developed.

import random

#A class which represents a player in the game. This class includes data representing their name, balance, and current hand.
class Player:
    #Initilizes the object with a name and balance. By default this creates a player with the name "First Last" who has a balance of $10.
    def __init__(self, fn="First", ln="Last", bal=10):
        #Sets the name and balance equal to what was chosen when the object's initilizer was called.
        self.__firstName = fn
        self.__lastName = ln
        self.__balance = bal
        #Initilizes a player's hand so that cards can be stored within it.
        self.__cardHand = []
        return
    
    #This method returns the first name of the player.
    def getFirstName(self):
        return self.__firstName

    #This method returns the last name of the player.
    def getLastName(self):
        return self.__lastName

    #This method returns the number values of the cards in their hand. (Integers between 0 and 51)
    def getCardHand(self):
        #Sets up a temporary list which will hold the number values of the cards.
        cardHandTemp = []
        #Appends the number values to the temporary list.
        for i in range(len(self.__cardHand)):
            cardHandTemp.append(self.__cardHand[i].getNumber())
        #Returns the completed list containing all card number values in a player's hand.
        return cardHandTemp
    
    #Returns the current balance of the player
    def getBalance(self):
        return self.__balance

    #Sets a new balance for the player based on what is input into newBal.
    def setBalance(self, newBal):
        self.__balance = newBal
        return

    #Sets a new first name for the player based on what is input into newName.
    def setFirstName(self, newName):
        self.__firstName = newName
        return

    #Sets a new last name for the player based on what is input into newName.
    def setLastName(self, newName):
        self.__lastName = newName
        return

    #Rsets the cardHand list which represents the players hand.
    def discardHand(self):
        self.__cardHand.clear()
        return

    #Adds a card to a player's hand
    def setCardHand(self, newVal):
        self.__cardHand.append(newVal)
        return

    #Returns the player's current hand
    def showHand(self):
        #Begins with a new line to separate the cards from any other text.
        cardReturn = "\n"
        #Looks at all cards in the cardHand list.
        for card in self.__cardHand:
            #Adds each card in the cardHand list to a string variable.
            cardReturn += str(card) + "\n"
        #Returns the string variable.
        return cardReturn

    #Calculates the "value" of a players hand by adding up the face values of all the cards in their hand.
    def totalCardValue(self):
        #Sets up a variable, cardValue, and sets it equal to 0.
        cardValue = 0
        #Goes through each card in the player's hand.
        for card in self.__cardHand:
            #Adds the value returned from the .getValue() function in the Card class to the cardValue variable.
            cardValue += card.getValue()
        #Returns the total value of all the player's cards in their hand.
        return cardValue

#A class which represents a card in the game.
class Card:
    #Takes in a number between 0 and 51, then saves it to allow for it's use by functions specifically made for performing actions with the cards.
    def __init__(self, number):
        #Saves the number of the card.
        self.__cardNum = number

    #Returns the saved card number, between 0 and 51.
    def getNumber(self):
        return self.__cardNum

    #Returns the "Value" of a card which is related to the face value of the card.
    def getValue(self):
        #Divides the card's number by 13 and gets the remainder to isolate the information needed to get the suite of the card from it's face value.
        cardVal = self.getNumber()%13
        #Adds one to the card to represent the fact that the cards are stored with a number between 0 and 51.
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

            print()
            print("-------------------")
            print(playerOne.getFirstName()," ", playerOne.getLastName(), "'s Balance: ", playerOne.getBalance(),sep="")
            print(playerTwo.getFirstName()," ", playerTwo.getLastName(), "'s Balance: ", playerTwo.getBalance(),sep="")
            print("-------------------")
            print()
        else:
            newBal = followingPlayer.getBalance() - 1
            followingPlayer.setBalance(newBal)
            startingPlayer.discardHand()
            followingPlayer.discardHand()
            roundNo = roundNo + 1

            print()
            print("-------------------")
            print(playerOne.getFirstName()," ", playerOne.getLastName(), "'s Balance: ", playerOne.getBalance(),sep="")
            print(playerTwo.getFirstName()," ", playerTwo.getLastName(), "'s Balance: ", playerTwo.getBalance(),sep="")
            print("-------------------")
            print()
            
    else:
        print("Shuffling Cards!!!")
        shuffle()
        roundNo = 0
