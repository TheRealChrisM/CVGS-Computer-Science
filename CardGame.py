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
        #Gets rid of face value information through integer division.
        suitNo = self.getNumber()//13
        #Sets a base case of SUITERR to indicate an issue calculating the suit of a card.
        suitName = "SUITERR"
        #Sets four cases which encompass the four suits in a typical deck of cards. This sets the first set of cards as Hearts, then Diamonds, then Clubs, and finally Spades.
        #However it is important to note that the order of the suits in this part doesn't make any major affects to the program. It simply decides which numbers will be which suit.
        if (suitNo == 0):
            suitName = "Hearts"
        elif (suitNo == 1):
            suitName = "Diamonds"
        elif (suitNo == 2):
            suitName = "Clubs"
        elif (suitNo == 3):
            suitName = "Spades"
        #Returns the calculated string of the suit name for the card.
        return suitName
    
    #returns a string of the face value of the card
    def findFace(self):
        #Gets rid of the suit value information through the modulus function. This adds one to translate from a range of 0-51 to 1-52.
        faceNo = (self.getNumber()+1)%13
        #Sets a base case of FACEERR to indicate an issue calculating the face value of a card.
        faceName = "FACEERR"
        #These numbers represent the possible values of the card and then what their face value would be if they matched that number.
        if (faceNo == 1):
            faceName = "Ace"
        elif (faceNo == 11):
            faceName = "Jack"
        elif (faceNo == 12):
            faceName = "Queen"
        #Important that the faceNo for a King is 0 as the one is added before the modulus this ensures that the fact that it will equal 0 is accounted for.
        elif (faceNo == 0):
            faceName = "King"
        #This handles the all the normal, "non-face" value cards.
        elif ((faceNo > 1) and (faceNo < 11)):
            faceName = str(faceNo)
        #Returns the calculated string of the face value for the card.
        return faceName

    #returns the string of the common identifier for a card.
    def __str__(self):
        #Pairs the face value and the suit of the card in one string.
        returnString = self.findFace() + " of " + self.findSuit()
        #Returns the string of the face value and the suit.
        return returnString

#Returns a random number between 0 and 51 which will represent drawing a card.
def draw():
    #Picks a random number between 0 and 51.
    card = random.randint(0,51)
    #Returns that random number.
    return card

#Returns a boolean which is True if card has been selected and false if it has not been selected.
def isDrawn(card):
    #Checks the index of the card inputted and responds with a boolean depending if it has been selected yet.
    return cardsDrawn[card]

#Resets the cards which have been drawn to represent a shuffling of the deck.
def shuffle():
    #Goes through the entire list of cards in cardsDrawn.
    for i in range(52):
        #Sets each index equal to false representing a shuffled deck.
        cardsDrawn[i] = False
        return
    
#Takes in a Player object along with a desired amount of cards and deals that amount of cards to the player.    
def deal(cardList, numCards):
    #Saves the desired number of cards the user wants.
    i = numCards
    #Sets up a loop to go while the desired number of cards has not been drawn and there are still cards in the deck to draw.
    while(i>0) and (False in cardsDrawn):
        #Draws a card and temporarily saves it as drewCard.
        drewCard = draw()
        #Makes sure that card has not been drawn yet.
        if not(isDrawn(drewCard)):
            #If it hasn't it will put that card in the player's hand indicated by cardList.
            cardList.setCardHand(Card(drewCard))
            #Then it will set the card's index in cardsDrawn equal to True to indicate it has been drawn.
            cardsDrawn[drewCard] = True
            #Decreases the number of cards that need to be drawn by one.
            i = i-1
    return

#Creates an empty list which will be used to track which cards have been drawn
cardsDrawn = []

#Loops through indexes 0 to 51.
for i in range(52):
    #Fills with the boolean False representing an unpicked card.
    cardsDrawn.append(False)

#Takes in each players first and last name individually to create the Player objects.
playerOneFirstName = input("What is Player 1's first name? ")
playerOneLastName = input("What is Player 1's last name? ")
playerTwoFirstName = input("What is Player 2's first name? ")
playerTwoLastName = input("What is player 2's last name? ")

#Constructs player one's object based on the names provided.
playerOne = Player(playerOneFirstName, playerOneLastName)
#Constructs player two's object based on the names provided.
playerTwo = Player(playerTwoFirstName, playerTwoLastName)

#Sets the round counter, which will be used to determine who's turn it is along with when there is a need to shuffle, equal to 0.
roundNo = 0

#Displays a formatted version of the balance of both players before the game begins.
print()
print("-------------------")
print(playerOne.getFirstName()," ", playerOne.getLastName(), "'s Balance: ", playerOne.getBalance(),sep="")
print(playerTwo.getFirstName()," ", playerTwo.getLastName(), "'s Balance: ", playerTwo.getBalance(),sep="")
print("-------------------")
print()

#This is the while loop for the main game loop, which will continue to loop while the players both have a balance greater than zero. 
while((playerOne.getBalance()>0) and (playerTwo.getBalance()>0)):
    #Ensures the round is less than or equal to 13 which means that the deck does not need to be shuffled yet.
    if(roundNo<13):
        #Determines that playerOne will start this round. This occurs on even numbered rounds.   
        if((roundNo%2)==0):
            #Sets the player who starts as the playerOne object.
            startingPlayer = playerOne
            #Sets the second player as the playerTwo object.
            followingPlayer = playerTwo
        #Determines that playerTwo will start this round. This occurs on odd numbered rounds. 
        else:
            #Sets the player who starts as the playerTwo object.
            startingPlayer = playerTwo
            #Sets the second player as the playerOne object.
            followingPlayer = playerOne
        #Deals one card to the starting player.
        deal(startingPlayer, 1)
        #Deals one card to the second player.
        deal(followingPlayer, 1)

        #This actually begins the round.
        print(startingPlayer.getFirstName(), "here is your hand. How much would you like to bet?")
        #Shows the player their hand along with some simple formatting from separators to make the output easier to read.
        print("************************")
        print(startingPlayer.showHand())
        print("************************")
        print()

        #Asks the player how much they would like to bet for that round.
        betQuestion = startingPlayer.getFirstName() + " please input the amount you would like to bet: "
        #Saves the users response as an integer in the betAmount variable.
        betAmount = eval(input(betQuestion))

        #Checks to see if the starting players bet amount is greater than their balance.
        if (betAmount > startingPlayer.getBalance()):
            #If it is the game will inform the user of this.
            print(startingPlayer.getFirstName(), "has bet greater than their current balance. The bet has now been set to their total balance.")
            #Then the game sets the bet value to their entire balance.
            betAmount = startingPlayer.getBalance()

        #New line to separate starting player's information from the second player's.
        print()
        #This begins second player's portion of the round.
        print(followingPlayer.getFirstName(), " here is your hand. ", startingPlayer.getFirstName(), " has bet ", betAmount, ".", sep="")
        #Shows the player their hand along with some simple formatting from separators to make the output easier to read.
        print("************************")
        print(followingPlayer.showHand())
        print("************************")
        print()

        #Asks the player if they would like to accept the bet, continuing that round, or fold, which ends the round.
        acceptBetQuestion = followingPlayer.getFirstName() + " do you accept " + startingPlayer.getFirstName() + "'s bet(y = yes | n = no)? "
        #Saves the response of the second player.
        acceptBet = input(acceptBetQuestion)

        #Checks if the input for the second player was equal to "y" which represents the second player's desire to continue the round.
        if (acceptBet == "y"):
            #Deals the starting player an additional card.
            deal(startingPlayer, 1)
            #Deals the second player an additional card.
            deal(followingPlayer, 1)
            
            #Prints out the starting player's hand at the end of the round.
            print()
            print(startingPlayer.getFirstName(), "'s hand:")
            print("************************")
            print(startingPlayer.showHand())
            print("************************")

            print()

            #Prints out the second player's hand at the end of the round.
            print(followingPlayer.getFirstName(), "'s hand:")
            print("************************")
            print(followingPlayer.showHand())
            print("************************")
            print()

            #Makes a check to see if playerOne's hand contained cards of a greater value.
            if (playerOne.totalCardValue() > playerTwo.totalCardValue()):
                #If they did the playerOne object is set as the winner.
                winner = playerOne
                #Then the playerTwo object is set as the loser.
                loser = playerTwo

                #Prints out a statement indicating that playerOne has won the round and how much playerTwo will pay them.
                print(winner.getFirstName(), " has won! ", loser.getFirstName(), " will pay them $", betAmount, ".", sep="")
                print()

                #Calculates the new total balance of the loser.
                newLoserBal = loser.getBalance() - betAmount
                #Calculates the new total balance of the winner.
                newWinnerBal = winner.getBalance() + betAmount
                #Sets the new balance of the loser.
                loser.setBalance(newLoserBal)
                #Sets the new balance of the winner.
                winner.setBalance(newWinnerBal)
                
                #Discards all the cards in the starting players's hand.
                startingPlayer.discardHand()
                #Discards all the cards in the second players's hand.
                followingPlayer.discardHand()
                
            #Makes a check to see if playerTwo's hand contained cards of a greater value.   
            elif (playerOne.totalCardValue() < playerTwo.totalCardValue()):
                #If they did the playerTwo object is set as the winner.
                winner = playerTwo
                #Then the playerOne object is set as the loser.
                loser = playerOne

                #Prints out a statement indicating that playerTwo has won the round and how much playerOne will pay them.
                print(winner.getFirstName(), " has won! ", loser.getFirstName(), " will pay them $", betAmount, ".", sep="")
                print()
                
                #Calculates the new total balance of the loser.
                newLoserBal = loser.getBalance() - betAmount
                #Calculates the new total balance of the winner.
                newWinnerBal = winner.getBalance() + betAmount
                #Sets the new balance of the loser.
                loser.setBalance(newLoserBal)
                #Sets the new balance of the winner.
                winner.setBalance(newWinnerBal)

                #Discards all the cards in the starting players's hand.
                startingPlayer.discardHand()
                #Discards all the cards in the second players's hand.
                followingPlayer.discardHand()
                
            #If neither player appeared to win the game checks for a tie condition.      
            else:
                #Informs the players that their scores have tied.
                print("Both players have tied!")

                #Discards all the cards in the starting players's hand.
                startingPlayer.discardHand()
                #Discards all the cards in the second players's hand.
                followingPlayer.discardHand()

            #Increases the round count by one.
            roundNo = roundNo + 1

            #Informs the players of their balance with some simple formatting at the end of the round.
            print()
            print("-------------------")
            print(playerOne.getFirstName()," ", playerOne.getLastName(), "'s Balance: ", playerOne.getBalance(),sep="")
            print(playerTwo.getFirstName()," ", playerTwo.getLastName(), "'s Balance: ", playerTwo.getBalance(),sep="")
            print("-------------------")
            print()
            
        #This applies if the second player inputs anything other than "y" accepting the bet. This means they want to fold their hand.
        else:
            #Calculates the new balance of the second player, which is their current balance minus one.
            newBal = followingPlayer.getBalance() - 1
            #Sets the second player's new balance.
            followingPlayer.setBalance(newBal)

            #Discards all the cards in the starting players's hand.
            startingPlayer.discardHand()
            #Discards all the cards in the second players's hand.
            followingPlayer.discardHand()

            #Increases the round count by one.
            roundNo = roundNo + 1

            #Informs the players of their balance with some simple formatting at the end of the round.
            print()
            print("-------------------")
            print(playerOne.getFirstName()," ", playerOne.getLastName(), "'s Balance: ", playerOne.getBalance(),sep="")
            print(playerTwo.getFirstName()," ", playerTwo.getLastName(), "'s Balance: ", playerTwo.getBalance(),sep="")
            print("-------------------")
            print()
            
    else:
        #Uses print lines to separate the shuffle statement from the rest of the game information.
        print()
        #Informs players that it is now time to shuffle the cards.
        print("13 rounds have now passed, the cards will be shuffled.")
        print()
        print()
        
        #Runs the function which suffles the cards.
        shuffle()

        #Resets the round counter back to zero.
        roundNo = 0
