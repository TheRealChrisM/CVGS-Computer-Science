#Christopher Marotta
#Lab D - Binary Tree Class
#February 4, 2020

class BinaryLinkedListNode:
    def __init__(self, myData):
        #Construct a new Linked List Node
        self.data = myData
        self.left = None
        self.right = None
        return
        

class BinaryLinkedList:

    def __init__(self):
        #Construct a new LinkedList. The first node and last node are the same. Size is 0        self.firstNode = LinkedListNode(None, None)
        self.root = None #LinkedListNode(None, None)
        self.size = 0
        return

    def addData(self, data):
        if self.root == None:
            node = BinaryLinkedListNode(data)
            self.root = node
        else:
            foundPlacement = False
            currPointer = self.root
            while(foundPlacement == False):
                if(data > currPointer.data):
                    if(currPointer.right == None):
                        newNode = BinaryLinkedListNode(data)
                        currPointer.right = newNode
                        foundPlacement = True
                    else:
                        currPointer = currPointer.right
                elif(data <= currPointer.data):
                    if(currPointer.left == None):
                        newNode = BinaryLinkedListNode(data)
                        currPointer.left = newNode
                        foundPlacement = True
                    else:
                        currPointer = currPointer.left
                else:
                    print("Error in adding new data.")
        self.size += 1
        return
    
    def listInorder(self):
        orderedList = self.recursiveInorder(self.root)
        return orderedList

    def recursiveInorder(self, curRoot):
        curList = []
        if (not(curRoot.left == None)):
            curList += self.recursiveInorder(curRoot.left)
        curList.append(curRoot.data)
        if (not(curRoot.right == None)):
            curList += self.recursiveInorder(curRoot.right)
        return curList

    def listPreorder(self):
        orderedList = self.recursivePreorder(self.root)
        return orderedList

    def recursivePreorder(self, curRoot):
        curList = []
        curList.append(curRoot.data)
        if (not(curRoot.left == None)):
            curList += self.recursivePreorder(curRoot.left)
        if (not(curRoot.right == None)):
            curList += self.recursivePreorder(curRoot.right)
        return curList
    
    def listPostorder(self):
        orderedList = self.recursivePostorder(self.root)
        return orderedList

    def recursivePostorder(self, curRoot):
        curList = []
        if (not(curRoot.left == None)):
            curList += self.recursivePostorder(curRoot.left)
        if (not(curRoot.right == None)):
            curList += self.recursivePostorder(curRoot.right)
        curList.append(curRoot.data)
        return curList

binList = BinaryLinkedList()
newData = ""
#Requests new data from user.
while(not (newData == "end")):
    newData = str(input("Please enter a word (input 'end' when you have input desired words): "))
    if(not(newData == "end")):
        binList.addData(newData)



    
