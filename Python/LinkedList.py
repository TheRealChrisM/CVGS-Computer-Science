class LinkedListNode:

    def __init__(self, myData, myNext):
        #Construct a new Linked List Node
        self.data = myData
        self.next = myNext
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
        node = LinkedListNode(data, None)
        if self.firstNode == None: #.data == None:
            self.firstNode = node
            self.lastNode = node
        else:
            self.lastNode.next = node
            self.lastNode = node
        self.size += 1
        return

    def addToFront(self, data):
        #Add a node to the end of the list
        node = LinkedListNode(data, self.firstNode)
        if self.firstNode == None: #.data == None:
            self.firstNode = node
            self.lastNode = node
        else:
            self.firstNode = node
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
            if currentNode.next == None:
                self.firstNode = None #LinkedListNode(None, None)
                self.lastNode = self.firstNode
                self.size = self.size - 1
            else:
                # Here there are more than one nodes in the list
                currentNode = currentNode.next
                self.firstNode = currentNode
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
            if currentNode.next == None:
                self.firstNode = None #LinkedListNode(None, None)
                self.lastNode = self.firstNode
                self.size = self.size - 1
            else:
                while not(currentNode.next == self.lastNode):
                    currentNode = currentNode.next
                # Here there are more than one nodes in the list
                self.lastNode = currentNode
                self.size = self.size - 1
        return rearData


    def __str__(self):
        currentNode =  self.firstNode
        for i in range(self.size):
            print (currentNode.data)
            currentNode = currentNode.next
        return "Reached end of list.\n"

theLL = LinkedList()
theLL.addToFront('Testing my Function...')
theLL.addToRear('Apple')
theLL.addToRear('Candy')
theLL.addToRear('Zoo')
theLL.addToFront('This should be first.')
print (theLL)
theLL.removeFromFront()
theLL.removeFromRear()
print (theLL)
theLL.removeFromFront()
theLL.removeFromRear()
print (theLL)
theLL.addToRear('Ranger')
theLL.addToFront('Put me in front!')
print (theLL)
theLL.removeFromFront()
theLL.removeFromRear()
print (theLL)
theLL.removeFromFront()
theLL.removeFromRear()
print (theLL)
theLL.addToRear('Ranger')
print(theLL)
theLL.removeFromRear()
theLL.addToRear('This is another test.')
print(theLL)
