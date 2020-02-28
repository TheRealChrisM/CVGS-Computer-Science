class LinkedListNode:

    def __init__(self, myData, myNext, myPrevious):
        #Construct a new Linked List Node
        self.data = myData
        self.next = myNext
        self.previous = myPrevious
        return
        

class LinkedList:

    def __init__(self):
        #Construct a new LinkedList. The first node and last node are the same. Size is 0        self.firstNode = LinkedListNode(None, None)
        self.firstNode = None #LinkedListNode(None, None)
        self.lastNode = self.firstNode
        self.size = 0
        return

    def addToRear(self, data):
        #Add a node to the front of the list
        node = LinkedListNode(data, None, None)
        if self.firstNode == None: #.data == None:
            self.firstNode = node
            self.lastNode = node
            self.firstNode.next = self.firstNode
            self.firstNode.previous = self.firstNode
        elif (self.firstNode.next == self.firstNode):
            self.firstNode.next = node
            self.firstNode.previous = node
            self.lastNode = node
            self.lastNode.next = self.firstNode
            self.lastNode.previous = self.firstNode
        else:
            self.lastNode.next = node
            self.lastNode.next.next = self.firstNode
            self.lastNode.next.previous = self.lastNode
            self.lastNode = self.lastNode.next
        self.size += 1
        return

    def addToFront(self, data):
        #Add a node to the end of the list
        node = LinkedListNode(data, self.firstNode, self.lastNode)
        if self.firstNode == None: #.data == None:
            self.firstNode = node
            self.lastNode = node
            self.firstNode.next = self.firstNode
            self.firstNode.previous = self.firstNode
        elif (self.firstNode.next == self.firstNode):
            self.firstNode = node
            self.lastNode.next = self.firstNode
            self.lastNode.previous = self.firstNode
        else:
            self.firstNode = node
            self.firstNode.next.previous = self.firstNode
            self.lastNode.next = self.firstNode
        self.size += 1
        return

    def removeFromFront(self):
        #Remove a node from the front of the list
        if self.size == 0:
            print ("Linked List is empty")
            frontData = None
        else:
            currentNode = self.firstNode
            frontData = currentNode.data
            # This is the case where we have only one node in the list
            if currentNode.next == currentNode:
                self.firstNode = None #LinkedListNode(None, None)
                self.lastNode = self.firstNode
                self.size = self.size - 1
            else:
                # Here there are more than one nodes in the list
                currentNode = currentNode.next
                self.firstNode = currentNode
                self.firstNode.previous = self.lastNode
                self.lastNode.next = self.firstNode
                self.size = self.size - 1
        return frontData

    def removeFromRear(self):
        #Remove a node from the end of the list
        if self.size == 0:
            print ("Linked List is empty")
            rearData = None
        else:
            currentNode = self.firstNode
            rearData = self.lastNode.data
            # This is the case where we have only one node in the list
            if currentNode.next == currentNode:
                self.firstNode = None #LinkedListNode(None, None)
                self.lastNode = self.firstNode
                self.size = self.size - 1
            else:
                while not(currentNode.next == self.lastNode):
                    currentNode = currentNode.next
                # Here there are more than one nodes in the list
                self.lastNode = currentNode
                self.lastNode.next = self.firstNode
                self.firstNode.previous = self.lastNode
                self.size = self.size - 1
        return rearData

    def printCircularly(self, numToPrint):
        returnVar = ""
        currentNode = self.firstNode
        for x in range(numToPrint):
            returnVar += currentNode.data + "\n"
            currentNode = currentNode.next
        return returnVar

    def __str__(self):
        currentNode =  self.firstNode
        for i in range(self.size):
            print (currentNode.data)
            currentNode = currentNode.next
        return "Reached end of list.\n"

    

##theLL = LinkedList()
##theLL.addToFront('Testing my Function...')
##theLL.addToRear('Apple')
##theLL.addToRear('Candy')
##theLL.addToRear('Zoo')
##theLL.addToFront('This should be first.')
##print (theLL)
##theLL.removeFromFront()
##theLL.removeFromRear()
##print (theLL)
##theLL.removeFromFront()
##theLL.removeFromRear()
##print (theLL)
##theLL.addToRear('Ranger')
##theLL.addToFront('Put me in front!')
##print (theLL)
##theLL.removeFromFront()
##theLL.removeFromRear()
##print (theLL)
##theLL.removeFromFront()
##theLL.removeFromRear()
##print (theLL)
##theLL.addToRear('Ranger')
##print(theLL)
##theLL.removeFromRear()
##theLL.addToRear('This is another test.')
##print(theLL)

theLL = LinkedList()
theLL.addToRear('Apple')
theLL.addToRear('Candy')
theLL.addToRear('Zoo')
print(theLL.printCircularly(8))
print()
theLL.addToFront('Ranger')
theLL.addToFront('Doctor')
theLL.addToFront('Lawyer')
print(theLL.printCircularly(8))
print()
theLL.removeFromFront()
print(theLL.printCircularly(8))
print()
theLL.removeFromRear()
print(theLL.printCircularly(8))
print()
theLL.addToRear('Water')
theLL.addToFront('Coffee')
theLL.addToRear('Soda')
print(theLL.printCircularly(8))
print()
