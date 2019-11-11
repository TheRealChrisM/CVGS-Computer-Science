#Christopher Marotta
#November 11, 2019
#Create a program which allows you to choose between displaying two pictures
from tkinter import *
from PIL import ImageTk

window = Tk()
frame = Frame(window)
buttonFrame = Frame(window)
def pickFortnite():
    canvas.lift(rectangle)
    canvas.lift(fortniteLogoImage)
    return

def pickMinecraft():
    canvas.lift(rectangle)
    canvas.lift(minecraftLogoImage)
    return

#creates canvas for image
canvas = Canvas(frame, bg = "grey", height = 600, width = 600)
canvas.grid(row = 0, column = 0)

#creates image variables
minecraftLogo = ImageTk.PhotoImage(file = 'images/minecraft-logo.png')
fortniteLogo = ImageTk.PhotoImage(file = 'images/fortnite-logo.png')

#creates images and rectangle within canvas
fortniteLogoImage = canvas.create_image(300,300, image = fortniteLogo)
minecraftLogoImage = canvas.create_image(300,300, image = minecraftLogo)
rectangle = canvas.create_rectangle(0,0,600,600, fill = "grey")

#creates buttons to choose image
fortniteButton = Button(buttonFrame, text = "Fortnite", command = pickFortnite)
minecraftButton = Button(buttonFrame, text = "Minecraft", command = pickMinecraft)

#grids buttons
fortniteButton.grid(row = 1, column = 0)
minecraftButton.grid(row = 1, column = 1)

#grids frames
frame.grid(row = 0, column = 0)
buttonFrame.grid(row = 1, column = 0)

window.mainloop()
