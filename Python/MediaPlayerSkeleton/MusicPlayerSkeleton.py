import pygame
from tkinter import *
from PIL import ImageTk

root = Tk()
root.title('Music Player')
root.resizable(False, False)

class Song:
    def __init__(self, nameIn, artistIn, albumIn, locIn, artIn):
        self.songName = nameIn
        self.artist = artistIn
        self.location = locIn
        self.artLoc = artIn
        self.art = ImageTk.PhotoImage(file = self.getArtLocation())
        self.album = albumIn

    def getSongLocation(self):
        return self.location

    def getArtLocation(self):
        return ("AlbumArt/"+self.artLoc)
    
    def getAlbumArt(self):
        return self.art

    def getAlbumName(self):
        return self.album

    def getSongName(self):
        return self.songName

    def getSongArtist(self):
        return self.artist

    def __str__(self):
        return ("["+self.artist+"] "+ self.songName)

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
        self.currentPlace = self.firstNode
        return

    def addToRear(self, data):
        #Add a node to the front of the list
        node = LinkedListNode(data, None, None)
        if self.firstNode == None: #.data == None:
            self.firstNode = node
            self.lastNode = node
            self.firstNode.next = self.firstNode
            self.firstNode.previous = self.firstNode
            self.currentPlace = self.firstNode
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
            self.currentPlace = self.firstNode
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

    def getCurrentPlace(self):
        return self.currentPlace.data

    def moveForward(self):
        self.currentPlace = self.currentPlace.next
        return

    def moveBackward(self):
        self.currentPlace = self.currentPlace.previous
        return

    #Locates songs with the input searchTerm. (searchType 1: Artist | searchType 0: Title)
    def search(self, searchType, searchTerm):
        compareTerm = searchTerm.upper().lower()
        foundItems = []
        currentIndex = self.firstNode.next
        if (searchType == 0):
            while(currentIndex != self.firstNode):
                currentSongName = currentIndex.data.getSongName().upper().lower()
                if (compareTerm in currentSongName):
                    foundItems.append(currentIndex)
                currentIndex = currentIndex.next
            currentSongName = self.firstNode.data.getSongName().upper().lower()
            if (compareTerm in currentSongName):
                    foundItems.append(currentIndex)
        elif (searchType == 1):
            while(currentIndex != self.firstNode):
                currentSongName = currentIndex.data.getSongArtist().upper().lower()
                if (compareTerm in currentSongName):
                    foundItems.append(currentIndex)
                currentIndex = currentIndex.next
            currentSongName = self.firstNode.data.getSongArtist().upper().lower()
            if (compareTerm in currentSongName):
                    foundItems.append(currentIndex)
        return foundItems

    def printCircularly(self, numToPrint):
        returnVar = ""
        currentNode = self.firstNode
        for x in range(numToPrint):
            returnVar += str(currentNode.data) + "\n"
            currentNode = currentNode.next
        return returnVar

    def __str__(self):
        currentNode =  self.firstNode
        for i in range(self.size):
            print (currentNode.data)
            currentNode = currentNode.next
        return "Reached end of list.\n"


def togglePlay():
    if (playButton["text"] == "Play"):
        playsong()
        playButton["text"] = ("\u23F8")
    elif (playButton["text"] == ("\u23F8")):
        pausesong()
        playButton["text"] = ("\u25B6")
    elif (playButton["text"] == ("\u25B6")):
        unpausesong()
        playButton["text"] = ("\u23F8")
    return

def playsong():
    pygame.mixer.music.play()

def pausesong():
    pygame.mixer.music.pause()

def unpausesong():
    pygame.mixer.music.unpause()

def stopsong():
    pygame.mixer.music.stop()
    playButton["text"] = ("Play")

def nextSong():
    stopsong()
    songDB.moveForward()
    currentSong = songDB.getCurrentPlace()
    curSongLoc = currentSong.getSongLocation()
    songNameLabel["text"] = currentSong.getSongName()
    songArtistLabel["text"] = currentSong.getSongArtist()
    albumArtPhoto["image"] = currentSong.getAlbumArt()
    songAlbumLabel["text"] = currentSong.getAlbumName()
    pygame.mixer.music.load(curSongLoc)
    togglePlay()
    return

def lastSong():
    stopsong()
    songDB.moveBackward()
    currentSong = songDB.getCurrentPlace()
    curSongLoc = currentSong.getSongLocation()
    songNameLabel["text"] = currentSong.getSongName()
    songArtistLabel["text"] = currentSong.getSongArtist()
    albumArtPhoto["image"] = currentSong.getAlbumArt()
    songAlbumLabel["text"] = currentSong.getAlbumName()
    pygame.mixer.music.load(curSongLoc)
    togglePlay()
    return

searchStr = StringVar()

def searchByArtist():
    global searchStr, popup
    popup = Toplevel()
    popup.title("Search")
    promptLabel = Label(popup, text = "Enter Artist to Find:")
    stringTest = StringVar(popup)
    entryBox = Entry(popup, textvariable = stringTest)
    entryBox.config(textvariable=searchStr)
    goButton = Button(popup, text = "Submit", command = lambda:[findArtist(), popup.destroy()])
    promptLabel.grid(row = 0, column = 0)
    entryBox.grid(row = 1, column = 0)
    goButton.grid(row = 2, columnspan = 1)
    return

def findArtist():
    global searchStr, popup, songSelected, songs, songList
    searchParam = searchStr.get()
    songs = songDB.search(1, searchParam)
    searchStr.set("")
    popup.destroy()
    if (len(songs)>0):
        songList = Toplevel()
        songSelected = IntVar()
        for i in range(len(songs)):
            Radiobutton(songList, variable = songSelected, value = i).grid(row = i, column = 0)
            Label(songList, text = ("["+songs[i].data.getSongArtist())+"]").grid(row = i, column = 1)
            Label(songList, text = songs[i].data.getSongName()).grid(row = i, column = 2)
        Button(songList, text = "Play", command = playSelectedSong).grid(row = (len(songs)+1), columnspan = 4)
    else:
        messagebox.showinfo("Error", "Artist not found!")
    return

def searchByTitle():
    global searchStr, popup
    popup = Toplevel()
    popup.title("Search")
    promptLabel = Label(popup, text = "Enter Song to Find:")
    entryBox = Entry(popup, textvariable = searchStr)
    goButton = Button(popup, text = "Submit", command = findSong)
    promptLabel.grid(row = 0, column = 0)
    entryBox.grid(row = 1, column = 0)
    goButton.grid(row = 2, columnspan = 1)
    return

def findSong():
    global searchStr, popup, songSelected, songs, songList
    searchParam = searchStr.get()
    songs = songDB.search(0, searchParam)
    searchStr.set("")
    popup.destroy()
    if (len(songs)>0):
        songList = Toplevel()
        songSelected = IntVar()
        for i in range(len(songs)):
            Radiobutton(songList, variable = songSelected, value = i).grid(row = i, column = 0)
            Label(songList, text = ("["+songs[i].data.getSongArtist())+"]").grid(row = i, column = 1)
            Label(songList, text = songs[i].data.getSongName()).grid(row = i, column = 2)
        Button(songList, text = "Play", command = playSelectedSong).grid(row = (len(songs)+1), columnspan = 4)
    else:
        messagebox.showinfo("Error", "Song not found!")
    return

def playSelectedSong():
    global songSelected, songs, songList
    songDB.currentPlace = songs[songSelected.get()]
    stopsong()
    currentSong = songDB.currentPlace.data
    curSongLoc = currentSong.getSongLocation()
    songNameLabel["text"] = currentSong.getSongName()
    songArtistLabel["text"] = currentSong.getSongArtist()
    albumArt = ImageTk.PhotoImage(file = currentSong.getArtLocation())
    albumArtPhoto["image"] = currentSong.getAlbumArt()
    songAlbumLabel["text"] = currentSong.getAlbumName()
    pygame.mixer.music.load(curSongLoc)
    songList.destroy()
    togglePlay()
    songSelected.set(-1)
    songs = []

menubar = Menu(root)
root.config(menu=menubar)
operationMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Search', menu = operationMenu)
operationMenu.add_command(label = 'By Artist', command = searchByArtist)
operationMenu.add_command(label = 'By Song Title', command = searchByTitle)

pygame.mixer.init()
songDB = LinkedList()
inputFile = open("songlist.txt", "r")
importDB = inputFile.readlines()
inputFile.close()

for song in importDB:
    newSong = song.strip()
    songMeta = newSong.split(",")
    songDB.addToFront(Song(songMeta[0], songMeta[1], songMeta[2], songMeta[3], songMeta[4]))

#Album Art 250x250px
albumArt = ImageTk.PhotoImage(file = "AlbumArt/ArtNotFound.jpg")

songInfoFrame = Frame(root)
controlFrame = Frame(root)

songNameLabel = Label(songInfoFrame, text="placeholder")
songArtistLabel = Label(songInfoFrame, text="placeholder")
songAlbumLabel = Label(songInfoFrame, text ="placeholder")
albumArtPhoto = Label(songInfoFrame, image = albumArt)
playButton = Button(controlFrame, text='Play', command = togglePlay)
stopButton = Button(controlFrame, text="\u25A0", command = stopsong)
lastButton = Button(controlFrame, text = "\u2190", command = lastSong)
nextButton = Button(controlFrame, text = "\u2192", command = nextSong)



albumArtPhoto.grid(row = 0, columnspan = 4)
songNameLabel.grid(row = 1, columnspan = 4)
songArtistLabel.grid(row = 2, columnspan = 4)
songAlbumLabel.grid(row = 3, columnspan = 4)
playButton.grid(row = 0, column = 1)
stopButton.grid(row = 0, column = 2)
lastButton.grid(row = 0, column = 0)
nextButton.grid(row = 0, column = 3)

songDB.moveForward()
currentSong = songDB.getCurrentPlace()
curSongLoc = currentSong.getSongLocation()
songNameLabel["text"] = currentSong.getSongName()
songArtistLabel["text"] = currentSong.getSongArtist()
albumArt = ImageTk.PhotoImage(file = currentSong.getArtLocation())
albumArtPhoto["image"] = currentSong.getAlbumArt()
songAlbumLabel["text"] = currentSong.getAlbumName()
pygame.mixer.music.load(curSongLoc)
togglePlay()

songInfoFrame.pack()
controlFrame.pack()

root.mainloop()

