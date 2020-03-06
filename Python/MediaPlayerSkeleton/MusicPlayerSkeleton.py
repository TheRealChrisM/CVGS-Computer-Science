#Imports pygame for music functionality.
import pygame
#Imports tkinter for GUI functionality.
from tkinter import *
#Imports the PhotoImageLibrary for album covers.
from PIL import ImageTk

#Sets up the main GUI window for later.
root = Tk()
#Titles the GUI Window as "Music Player".
root.title('Music Player')
#Makes the window a set size so users can't change it's dimensions.
root.resizable(False, False)

################################################################################

#A class to contain song metadata for the music player to use.
class Song:

    ####################

    #Initilizes the class object taking in a song name, artist, album, location, and art location.
    def __init__(self, nameIn, artistIn, albumIn, locIn, artIn):
        #Sets the song name as the name that was input into the function.
        self.songName = nameIn
        #Sets the artist as the artist that was input into the function.
        self.artist = artistIn
        #Sets the music location as the location that was input into the function.
        self.location = locIn
        #Sets the art location as the art location that was input into the function.
        self.artLoc = artIn
        #Sets the art based on a PhotoImage object which is based on the adjusted location from the inputted art location.
        self.art = ImageTk.PhotoImage(file = self.getArtLocation())
        #Sets the album name based on the album that was input into the fucntion.
        self.album = albumIn

    ####################
        
    #Returns the location of the song file.
    def getSongLocation(self):
        #Returns the variable which represents the song location.
        return self.location

    ####################

    #Returns the location of the song's album art.
    def getArtLocation(self):
        #Takes the current saved location of the album art and adds the location of the folder infront of it.
        return ("AlbumArt/"+self.artLoc)

    ####################

    #Returns the variable that hold the name of the album art.
    def getAlbumArt(self):
        #Directly returns the variable holding the location of the album art.
        return self.art

    ####################

    #Returns the name of the song's album.
    def getAlbumName(self):
        #Returns the variable that holds the album the song is a part of.
        return self.album

    ####################
    
    #Returns the name of the song.
    def getSongName(self):
        #Returns the variable holding the name of the song.
        return self.songName

    ####################

    #Returns the artist of the song.
    def getSongArtist(self):
        #Returns the variable containing the artist of the song.
        return self.artist

    ####################

    #Overloads the string function. This function was primarily used for testing as it easily allows for the identifying metadata of a song to be output into the console.
    def __str__(self):
        #Returns a string that contains a song's artist and name.
        return ("["+self.artist+"] "+ self.songName)

################################################################################

#A class which represents a single node that will be used in a circularly linked list
class LinkedListNode:
    
    ####################

    #Initilizes the linked node object taking in a data "object", a "pointer" towards the next node, and a "pointer" towards the previous node.
    def __init__(self, myData, myNext, myPrevious):
        #The data object that is being saved in the node.
        self.data = myData
        #A reference to the next node in the circular list.
        self.next = myNext
        #A reference to the previous node in the linked list.
        self.previous = myPrevious
        return

################################################################################


        
class LinkedList:

    ####################

    #An initilizer that creates a new circularly linked list.
    def __init__(self):
        #Starts off the first node of the list as "blank" node to result in an empty list.
        self.firstNode = None #LinkedListNode(None, None)
        #Sets the last node as the first node.
        self.lastNode = self.firstNode
        #Sets the list size to zero.
        self.size = 0
        #Sets a pointer which tracks the current position something is looking at in the list.
        self.currentPlace = self.firstNode
        return

    ####################

    #A function which adds a node to the end of the list taking in a data object.
    def addToRear(self, data):
        #Creates a placeholder node.
        node = LinkedListNode(data, None, None)
        #Checks to see if there are not any nodes in the list yet.
        if self.firstNode == None: #.data == None:
            #Sets the placeholder node as the first node.
            self.firstNode = node
            #Sets the placeholder node as the last node.
            self.lastNode = node
            #Sets the firstNode's next pointer towards the firstNode.
            self.firstNode.next = self.firstNode
            #Sets the firstNode's previous pointer towards the firstNode.
            self.firstNode.previous = self.firstNode
            #Makes the currentPlace tracker focus on the newly added firstNode.
            self.currentPlace = self.firstNode
        #Checks to see if there is one node in the list.
        elif (self.firstNode.next == self.firstNode):
            #Sets the firstNode's next pointer towards the new node.
            self.firstNode.next = node
            #Sets the firstNode's previous pointer towards the new node.
            self.firstNode.previous = node
            #Sets the lastNode pointer to the new node.
            self.lastNode = node
            #Makes the lastNode's next pointer point towards the firstNode.
            self.lastNode.next = self.firstNode
            #Makes the lastNode's previous pointer point towards the firstNode.
            self.lastNode.previous = self.firstNode
        #Checks to see if there is more than one node in the list.
        else:
            #Sets the lastNode to the placeholder node.
            self.lastNode.next = node
            #Sets the next node after the next node's pointer to the first node.
            self.lastNode.next.next = self.firstNode
            #Sets the previous pointer of the next node after the last node to the new last node.
            self.lastNode.next.previous = self.lastNode
            #Sets the last node equal to the node that the previous last node was pointing to.
            self.lastNode = self.lastNode.next
        #Increases the list size by one.
        self.size += 1
        return

    ####################

    #Adds a data object that is input into the function to the front of the circularly linked list.
    def addToFront(self, data):
        #Creates a placeholder node.
        node = LinkedListNode(data, self.firstNode, self.lastNode)
        #Checks to see if there are no nodes in the list yet.
        if self.firstNode == None: #.data == None:
            #Sets the firstNode to the newly created node.
            self.firstNode = node
            #Sets the lastNode as the newly created node.
            self.lastNode = node
            #Makes the firstNode's next pointer point to the firstNode.
            self.firstNode.next = self.firstNode
            #Makes the firstNode's previous pointer point to the firstNode.
            self.firstNode.previous = self.firstNode
            #Makes the currentPlace tracker point towards the firstNode.
            self.currentPlace = self.firstNode
        #Checks to see if there is one node in the list.
        elif (self.firstNode.next == self.firstNode):
            #Sets the first node as the placeholder node.
            self.firstNode = node
            #Makes the last node's next pointer point towards the firstNode.
            self.lastNode.next = self.firstNode
            #Makes the lastNode's previous pointer point towards the firstNode.
            self.lastNode.previous = self.firstNode
        #Checks to see if there is more than one node in the list.
        else:
            #Sets the firstNode as the placeholder node.
            self.firstNode = node
            #Makes the firstNode's next pointer's previous pointer point towards the firstNode.
            self.firstNode.next.previous = self.firstNode
            #Makes the lastNode's next pointer point towards the firstNode.
            self.lastNode.next = self.firstNode
        #Increases the size variable by one.
        self.size += 1
        return

    ####################

    #Removes the node from the "front" of the circular list.
    def removeFromFront(self):
        #Checks to see if the circular list is currently empty.
        if self.size == 0:
            #Prints out the fact that the circular list is empty.
            print ("Linked List is empty")
            #Sets the frontData variable to None to prevent errors within this function.
            frontData = None
        #Checks to see if the size of the circular list is greater than zero.
        else:
            #Sers the currentNode tracker within this function to the firstNode of the list.
            currentNode = self.firstNode
            #Sers the frontData that will be returned to the currentNode tracker for this function.
            frontData = currentNode.data
            # This is the case where we have only one node in the list.
            if currentNode.next == currentNode:
                #Sers the firstNode to None.
                self.firstNode = None #LinkedListNode(None, None)
                #Sets the lastNode to None.
                self.lastNode = self.firstNode
                #Decreases the size of the list by one effectively making it zero.
                self.size = self.size - 1
            # Here there are more than one nodes in the list.
            else:
                #Sets the currentNode tracker to the "next" node in the list.
                currentNode = currentNode.next
                #Sets the firstNode to the currentNode tracker position.
                self.firstNode = currentNode
                #Sets the firstNode's previous pointer to the current lastNode.
                self.firstNode.previous = self.lastNode
                #Makes the lastNode's next pointer point towards the new firstNode.
                self.lastNode.next = self.firstNode
                #Decreases the list size by one.
                self.size = self.size - 1
        #Returns whatever was previously the data object stored in the firstNode.
        return frontData

    ####################

    #Removes the node from the "end" of the circular list.
    def removeFromRear(self):
        #Checks to see if the circular list is currently empty.
        if self.size == 0:
            #Prints out the fact that the circular list is empty.
            print ("Linked List is empty")
            #Sets the frontData variable to None to prevent errors within this function.
            frontData = None
        #Checks to see if the size of the circular list is greater than zero.
        else:
            #Sets the currentNode to the firstNode in the list.
            currentNode = self.firstNode
            #Saves the data from the lastNode in the circular list.
            rearData = self.lastNode.data
            # This is the case where we have only one node in the list
            if currentNode.next == currentNode:
                #Sets the firstNode to None.
                self.firstNode = None #LinkedListNode(None, None)
                #Sets the lastNode to None.
                self.lastNode = self.firstNode
                #Decreases the current size of the list by one.
                self.size = self.size - 1
            #Checks to see if the size of the list is greater than one.
            else:
                #Run while the node the tracker is pointing to is not the last node.
                while not(currentNode.next == self.lastNode):
                    #Moves the node tracker to the next node.
                    currentNode = currentNode.next
                #Makes the lastNode equal to what the currentNode tracker is.
                self.lastNode = currentNode
                #Makes the new lastNode point towards the current firstNode.
                self.lastNode.next = self.firstNode
                #Makes the firstNode's previous pointer point towards the new lastNode.
                self.firstNode.previous = self.lastNode
                #Decreases the list size by one.
                self.size = self.size - 1
        #Returns the data from the rear of the list.
        return rearData

    ####################

    #Returns the data from the node the currentPlace tracker is pointing towards.
    def getCurrentPlace(self):
        #Returns information stored in the data variable from the node object.
        return self.currentPlace.data

    ####################

    #Moves the currentPlace tracker forward one node.
    def moveForward(self):
        #Makes the currentPlace tracker equal to what it is pointing to as the next node.
        self.currentPlace = self.currentPlace.next
        return

    ####################

    #Moves the currentPlace tracker backward one node.
    def moveBackward(self):
        #Makes the currentPlace tracker equal to what it is pointing to as the previous node.
        self.currentPlace = self.currentPlace.previous
        return
    
    ####################

    #Locates songs with the input searchTerm. (searchType 1: Artist | searchType 0: Title)
    def search(self, searchType, searchTerm):
        #Converts all characters in the inputted search term to lowercase to make future comparisons more accurate.
        compareTerm = searchTerm.upper().lower()
        #Creates an empty list of all song items that will be found in the search.
        foundItems = []
        #Sets the current place the list is looking at to the one after the first.
        currentIndex = self.firstNode.next
        #Checks to see if the user is trying to search for song title.
        if (searchType == 0):
            #Checks to see while the currentIndex tracker is not currently pointing towards the firstNode in the list.
            while(currentIndex != self.firstNode):
                #Grabs the song name from the currentNode, then converts it from upper to lowercase to make comparisons easier.
                currentSongName = currentIndex.data.getSongName().upper().lower()
                #Checks to see if the current song's information matches with the search term.
                if (compareTerm in currentSongName):
                    #Adds the matching song to the list of songs that are matched to the search term.
                    foundItems.append(currentIndex)
                #Moves to the next song.
                currentIndex = currentIndex.next
            #Grabs the song name from the currentNode (firstNode), then converts it from upper to lowercase to make comparisons easier.
            currentSongName = self.firstNode.data.getSongName().upper().lower()
            #Checks to see if the current song's information matches with the search term.
            if (compareTerm in currentSongName):
                #Adds the matching song to the list of songs that are matched to the search term.
                    foundItems.append(currentIndex)
        #Checks to see if the user is trying to search for song artist.
        elif (searchType == 1):
            #Checks to see while the currentIndex tracker is not currently pointing towards the firstNode in the list.
            while(currentIndex != self.firstNode):
                #Grabs the artist name from the currentNode, then converts it from upper to lowercase to make comparisons easier.
                currentSongName = currentIndex.data.getSongArtist().upper().lower()
                #Checks to see if the current song's information matches with the search term.
                if (compareTerm in currentSongName):
                    #Adds the matching song to the list of songs that are matched to the search term.
                    foundItems.append(currentIndex)
                #Moves to the next song.
                currentIndex = currentIndex.next
            #Grabs the artist name from the currentNode (firstNode), then converts it from upper to lowercase to make comparisons easier.
            currentSongName = self.firstNode.data.getSongArtist().upper().lower()
            #Checks to see if the current song's information matches with the search term.
            if (compareTerm in currentSongName):
                #Adds the matching song to the list of songs that are matched to the search term.
                    foundItems.append(currentIndex)
        #Returns the list of all the song objects that were found to match the search term.
        return foundItems

    ####################

    #A function that takes in a number to iterate through then begins printing the data objects of the list.count
    def printCircularly(self, numToPrint):
        #Sets up an empty variable to hold the return information.
        returnVar = ""
        #Sets the currentNode tracker equal to the firstNode.
        currentNode = self.firstNode
        #Runs for as many times as was indicated in the function input.
        for x in range(numToPrint):
            #Adds the data string to the return variable then ends it with a new line.
            returnVar += str(currentNode.data) + "\n"
            #Makes the currentNode tracker move to the next node.
            currentNode = currentNode.next
        #Returns all of the object data that was put into the return variable as a string.
        return returnVar
    
    ####################

    #Overloads the string method for the linked list to make testing functionality easier.
    def __str__(self):
        #Sets the currentNode tracker to the first node in the list.
        currentNode =  self.firstNode
        #Goes through each object in the list based on the size of the list.
        for i in range(self.size):
            #Prints out the data of the node it is currently on.
            print (currentNode.data)
            #Moves the current node tracker to the next object.
            currentNode = currentNode.next
        #Indicate that the function has reached the end of the list before exiting.
        return "Reached end of list.\n"

################################################################################

#A function which takes in the current status of the song and either plays or pauses the song based on that.
def togglePlay():
    #Checks to see if the text of the button currently says "Play".
    if (playButton["text"] == "Play"):
        #Plays the song.
        playsong()
        #Sets the text of the button to a pause button.
        playButton["text"] = ("\u23F8")
    #Checks if the button text is a pause button.
    elif (playButton["text"] == ("\u23F8")):
        #Pauses the song.
        pausesong()
        #Sets the text of the button to a play button.
        playButton["text"] = ("\u25B6")
    #Checks to see if the button text is a play button.
    elif (playButton["text"] == ("\u25B6")):
        #Unpauses the song.
        unpausesong()
        #Sets the text of the button to a pause button.
        playButton["text"] = ("\u23F8")
    return

####################

#Starts playing the song.
def playsong():
    #Uses a pyGame built in function to begin music playback.
    pygame.mixer.music.play()

####################

#Pauses the song.
def pausesong():
    #Uses a built in pyGame function to pause music playback.
    pygame.mixer.music.pause()

####################

#Unpauses the song.
def unpausesong():
    #Uses a built in pyGame function to unpause the song.
    pygame.mixer.music.unpause()

####################

#Stops the song.
def stopsong():
    #Uses a built in pyGame function to stop the song.
    pygame.mixer.music.stop()
    #Changes button text to "Play" to indicate that the song has not begun.
    playButton["text"] = ("Play")

####################

#A function which moves to the next song.
def nextSong():
    #Stops the song that is currently playing.
    stopsong()
    #Tells the music database to move forward one song.
    songDB.moveForward()
    #Saves the song the currentPlace tracker is currently on.
    currentSong = songDB.getCurrentPlace()
    #Extracts the song location of the current song.
    curSongLoc = currentSong.getSongLocation()
    #Displays the name of the current song.
    songNameLabel["text"] = currentSong.getSongName()
    #Displays the artist of the current song.
    songArtistLabel["text"] = currentSong.getSongArtist()
    #Displays the album art of the current song.
    albumArtPhoto["image"] = currentSong.getAlbumArt()
    #Displays the album name of the current song.
    songAlbumLabel["text"] = currentSong.getAlbumName()
    #Queues up the current song.
    pygame.mixer.music.load(curSongLoc)
    #Begins playback of the new song.
    togglePlay()
    return

####################

#A function which moves to the previous song.
def lastSong():
    #Stops the song that is currently playing.
    stopsong()
    #Tells the music database to move backward one song.
    songDB.moveBackward()
    #Saves the song the currentPlace tracker is currently on.
    currentSong = songDB.getCurrentPlace()
    #Extracts the song location of the current song.
    curSongLoc = currentSong.getSongLocation()
    #Displays the name of the current song.
    songNameLabel["text"] = currentSong.getSongName()
    #Displays the artist of the current song
    songArtistLabel["text"] = currentSong.getSongArtist()
    #Displays the album art of the current song.
    albumArtPhoto["image"] = currentSong.getAlbumArt()
    #Displays the album name of the current song.
    songAlbumLabel["text"] = currentSong.getAlbumName()
    #Queues up the current song.
    pygame.mixer.music.load(curSongLoc)
    #Begins playback of the new song.
    togglePlay()
    return

####################

#Creates a string variable which will be used by the search function.
searchStr = StringVar()

####################

#Searches through the music database by artist.
def searchByArtist():
    #Sets the "popup" window and the searchString variable as global so they can be used across functions.
    global searchStr, popup
    #Creates the popup window to display the search lookup widgets.
    popup = Toplevel()
    #Makes the title of the popup window "Search".
    popup.title("Search")
    #Prompts the user with a label to enter their search terms.
    promptLabel = Label(popup, text = "Enter Artist to Find:")
    #Creates an entry box for the user to enter their search terms.
    entryBox = Entry(popup, textvariable = searchStr)
    #Creates a button for the user to submit their search terms.
    goButton = Button(popup, text = "Submit", command = lambda:[findArtist(), popup.destroy()])
    #Displays the label on the popup window.
    promptLabel.grid(row = 0, column = 0)
    #Displays the entry box on the popup window.
    entryBox.grid(row = 1, column = 0)
    #Displays the button on the window.
    goButton.grid(row = 2, columnspan = 1)
    return

####################

#A function that finds a song by it's artist.
def findArtist():
    #Sets the "popup" window, the searchString, the songSelected, songsList and also songList label variables as global so they can be used across functions.
    global searchStr, popup, songSelected, songs, songList
    #Pulls in the information from the searchString the user inputted into the entry box.
    searchParam = searchStr.get()
    #Searches for the songs based on artist check by the search term entered.
    songs = songDB.search(1, searchParam)
    #Resets the entrybox for next time that it is used.
    searchStr.set("")
    #Closes the popup window.
    popup.destroy()
    #Makes sure that there is more than one song.
    if (len(songs)>0):
        #Creates a new popup window to display the found songs.
        songList = Toplevel()
        #Creates an IntVar to track which song the user has chosen.
        songSelected = IntVar()
        #Goes through each song in the list.
        for i in range(len(songs)):
            #Creates a radio button for the song.
            Radiobutton(songList, variable = songSelected, value = i).grid(row = i, column = 0)
            #Creates a label for the song with the artist's name.
            Label(songList, text = ("["+songs[i].data.getSongArtist())+"]").grid(row = i, column = 1)
            #Creates a label for the song with the song's name.
            Label(songList, text = songs[i].data.getSongName()).grid(row = i, column = 2)
        #Creates a button that once clicked will begin playback of the selected song.
        Button(songList, text = "Play", command = playSelectedSong).grid(row = (len(songs)+1), columnspan = 4)
    #Checks to see if the search didn't find anything.
    else:
        #Displays a messagebox that indicates the fact that nothing was found from the search.
        messagebox.showinfo("Error", "Artist not found!")
    return

####################

#A function that begins search for a song by it's title.
def searchByTitle():
    #Sets the "popup" window and the searchString variable as global so they can be used across functions.
    global searchStr, popup
    #Creates the popup window to display the search lookup widgets.
    popup = Toplevel()
    #Makes the title of the popup window "Search".
    popup.title("Search")
    #Prompts the user with a label to enter their search terms.
    promptLabel = Label(popup, text = "Enter Song to Find:")
    #Creates an entry box for the user to enter their search terms.
    entryBox = Entry(popup, textvariable = searchStr)
    #Creates a button for the user to submit their search terms.
    goButton = Button(popup, text = "Submit", command = findSong)
    #Displays the label on the popup window.
    promptLabel.grid(row = 0, column = 0)
    #Displays the entry box on the popup window.
    entryBox.grid(row = 1, column = 0)
    #Displays the button on the window.
    goButton.grid(row = 2, columnspan = 1)
    return

####################

#A function that locates a song by it's title.
def findSong():
    #Sets the "popup" window, the searchString, the songSelected, songsList and also songList label variables as global so they can be used across functions.
    global searchStr, popup, songSelected, songs, songList
    #Pulls in the information from the searchString the user inputted into the entry box.
    searchParam = searchStr.get()
    #Searches for the songs based on title check by the search term entered.    
    songs = songDB.search(0, searchParam)
    #Resets the entrybox for next time that it is used.    
    searchStr.set("")
    #Closes the popup window.
    popup.destroy()
    #Makes sure that there is more than one song.
    if (len(songs)>0):
        #Creates a new popup window to display the found songs.
        songList = Toplevel()
        #Creates an IntVar to track which song the user has chosen.
        songSelected = IntVar()
        #Goes through each song in the list.
        for i in range(len(songs)):
            #Creates a radio button for the song.
            Radiobutton(songList, variable = songSelected, value = i).grid(row = i, column = 0)
            #Creates a label for the song with the artist's name.
            Label(songList, text = ("["+songs[i].data.getSongArtist())+"]").grid(row = i, column = 1)
            #Creates a label for the song with the song's name.
            Label(songList, text = songs[i].data.getSongName()).grid(row = i, column = 2)
        #Creates a button that once clicked will begin playback of the selected song.            
        Button(songList, text = "Play", command = playSelectedSong).grid(row = (len(songs)+1), columnspan = 4)
    #Checks to see if the search didn't find anything.    
    else:
        #Displays a messagebox that indicates the fact that nothing was found from the search.
        messagebox.showinfo("Error", "Song not found!")
    return

####################

#A function that plays a song once it has been found through a search.
def playSelectedSong():
    #Makes the songSelected, song list, and also songList window global so they may be easily accessed between functions.
    global songSelected, songs, songList
    #Finds the song that was picked.
    songDB.currentPlace = songs[songSelected.get()]
    #Stops playback of the current song.
    stopsong()
    #Sets the currentSong tracker to the newly located song.
    currentSong = songDB.currentPlace.data
    #Finds the location of the new song.
    curSongLoc = currentSong.getSongLocation()
    #Displays the name of the new song.
    songNameLabel["text"] = currentSong.getSongName()
    #Displays the artist of the new song.
    songArtistLabel["text"] = currentSong.getSongArtist()
    #Sets the album art of the new song.
    albumArt = ImageTk.PhotoImage(file = currentSong.getArtLocation())
    #Displays the album art of the new song.
    albumArtPhoto["image"] = currentSong.getAlbumArt()
    #Displays the album of the new song.
    songAlbumLabel["text"] = currentSong.getAlbumName()
    #Queues up the new song for playback.
    pygame.mixer.music.load(curSongLoc)
    #Closes the window that had the song choices on it.
    songList.destroy()
    #Begins playback.
    togglePlay()
    #Resets the variable that stores the song that was selected.
    songSelected.set(-1)
    #Resets the list of the found songs.
    songs = []

####################

#Creates a menubar to allow the user to search for a song.
menubar = Menu(root)
#Displays the menubar in the main window.
root.config(menu=menubar)
#Sets up the menubar.
operationMenu = Menu(menubar, tearoff = 0)
#Creates a search option in the menubar.
menubar.add_cascade(label = 'Search', menu = operationMenu)
#Creates the option to search by the song's artist.
operationMenu.add_command(label = 'By Artist', command = searchByArtist)
#Creates the option to search by song title.
operationMenu.add_command(label = 'By Song Title', command = searchByTitle)

####################

#Prepares pyGames music library for use.
pygame.mixer.init()
#Sets up the linkedList for use.
songDB = LinkedList()
#Declares the file that should be used to store song metadata.
inputFile = open("songlist.txt", "r")
#Takes in and saves the information for the database file.
importDB = inputFile.readlines()
#Closes the database file to prevent corrouption.
inputFile.close()

####################

#Goes through the lines in the database file.
for song in importDB:
    #Strips extra characters from the file.
    newSong = song.strip()
    #Splits it up as a CSV.
    songMeta = newSong.split(",")
    #Creates a song objects based on the metadata and adds it to the front of the circular list.
    songDB.addToFront(Song(songMeta[0], songMeta[1], songMeta[2], songMeta[3], songMeta[4]))

####################

#Creates the placeholder album art incase there is an error. (Album Art MUST BE 250x250px)
albumArt = ImageTk.PhotoImage(file = "AlbumArt/ArtNotFound.jpg")

####################

#Creates a frame in the main window for the song info.
songInfoFrame = Frame(root)
#Creates a frame in the main window for the user controls.
controlFrame = Frame(root)
#Creates a label for the song name with placeholder text.
songNameLabel = Label(songInfoFrame, text="placeholder")
#Creates a label for the song's artist with placeholder text.
songArtistLabel = Label(songInfoFrame, text="placeholder")
#Creates a label for the song's album with placeholder text.
songAlbumLabel = Label(songInfoFrame, text ="placeholder")
#Creates a label for the album art with a placeholder image.
albumArtPhoto = Label(songInfoFrame, image = albumArt)
#Creates the play button for the controls.
playButton = Button(controlFrame, text='Play', command = togglePlay)
#Creates the stop button for the controls.
stopButton = Button(controlFrame, text="\u25A0", command = stopsong)
#Creates the button to go back a song for the controls.
lastButton = Button(controlFrame, text = "\u2190", command = lastSong)
#Creates a button to go forward a song for the controls.
nextButton = Button(controlFrame, text = "\u2192", command = nextSong)
#Places the album art into the window.
albumArtPhoto.grid(row = 0, columnspan = 4)
#Places the song name label into the window.
songNameLabel.grid(row = 1, columnspan = 4)
#Places the artist name label into the window.
songArtistLabel.grid(row = 2, columnspan = 4)
#Places the album name label into the window.
songAlbumLabel.grid(row = 3, columnspan = 4)
#Places the play button into the window.
playButton.grid(row = 0, column = 1)
#Places the stop button into the window.
stopButton.grid(row = 0, column = 2)
#Places the last song button into the window.
lastButton.grid(row = 0, column = 0)
#places the next song button into the window.
nextButton.grid(row = 0, column = 3)

####################

#Moves the song tracker in the circular list forward one. (Moves it from the end to the beginning)
songDB.moveForward()
#Gets the song object from the current song tracker.
currentSong = songDB.getCurrentPlace()
#Gets the location of the current song.
curSongLoc = currentSong.getSongLocation()
#Displays the name of the current song.
songNameLabel["text"] = currentSong.getSongName()
#Displays the artist of the current song.
songArtistLabel["text"] = currentSong.getSongArtist()
#Saves the album art of the current song.
albumArt = ImageTk.PhotoImage(file = currentSong.getArtLocation())
#Displays the album art of the current song.
albumArtPhoto["image"] = currentSong.getAlbumArt()
#Displays the album name of the current song.
songAlbumLabel["text"] = currentSong.getAlbumName()
#Queues the music up so it is ready to play.
pygame.mixer.music.load(curSongLoc)
#Begins music playback.
togglePlay()

####################

#Packs and displays the frame that contains song info into the main window.
songInfoFrame.pack()
#Packs and displays the frame that contains song controls into the main window.
controlFrame.pack()

####################

#Begins "animating" the GUI of the main window so it updates.
root.mainloop()
