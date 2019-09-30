import random

class Player:
    def __init__(self, fn="First", ln="Last", hand=[]):
        self.__firstName = fn
        self.__lastName = ln
        self.__cardHand = hand
        return

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getCardHand(self):
        return self.__cardHand

    def setFirstName(self, newName):
        self.__firstName = newName
        return

    def setLastName(self, newName):
        self.__lastName = newName
        return

    def setDiscard(self, newCard, index):
        self.__cardHand[index] = newCard
        return

    def setCardHand(self, newVal):
        self.__cardHand.append(newVal)
        return
    
    def showHand(self):
        for card in self.__cardHand:
            suit = card//13
            face = card%13
            print("Suit: ",suit, "\nFace: ", face, sep="")
        return

def draw():
    card = random.randint(0,51)
    return card

def inHand(card, cardHand):
    if card in cardHand:
        result = True
    else:
        result = False
    return result

def deal(cardList, numCards):
    for i in range(numCards):
        cardList.setCardHand(draw())
    return
