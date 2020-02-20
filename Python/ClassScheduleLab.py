#Christopher Marotta
#October 29th, 2019
#Lab I - Part I (Class Schedule Program)
from tkinter import *
from tkinter import ttk

#setting up tkinker stuff
window = Tk()
inputFrame = Frame(window)
window.title("Class Schedule")
summaryFrame = Frame(window)

#setup the processSelection function
def processSelection():
    nameString = lastNameVar.get() + ", " + firstNameVar.get() + " [Session " + str(sessionSelected.get()) + "]" + " :"
    nameLabel = Label(summaryFrame, text = nameString)
    mathString = "Math: " + mathSelectedCourse.get()
    scienceString = "Science: " + scienceSelectedCourse.get()
    seniorSeminarString = "Senior Seminar: " + seniorSeminarSelectedCourse.get()
    mathLabel = Label(summaryFrame, text = mathString)
    scienceLabel = Label(summaryFrame, text = scienceString)
    seniorSeminarLabel = Label(summaryFrame, text = seniorSeminarString)

    nameLabel.grid(row = 0, column = 0, sticky = W)
    mathLabel.grid(row = 1, column = 0, sticky = W, padx = 20)
    scienceLabel.grid(row = 2, column = 0, sticky = W, padx = 20)
    seniorSeminarLabel.grid(row = 3, column = 0, sticky = W, padx = 20)
    
    inputFrame.pack_forget()
    summaryFrame.pack()
    return

#setting up entry boxes
firstNameLabel = Label(inputFrame, text="First Name:")
firstNameVar = StringVar()
firstNameEntry = Entry(inputFrame, textvariable = firstNameVar)
lastNameLabel = Label(inputFrame, text="Last Name:")
lastNameVar = StringVar()
lastNameEntry = Entry(inputFrame, textvariable = lastNameVar)
firstNameLabel.grid(row = 0, column = 0, pady = 10, sticky = E, padx = 10)
firstNameEntry.grid(row = 0, column = 1, pady = 10)
lastNameLabel.grid(row = 1, column = 0, pady = 10, sticky = E, padx = 10)
lastNameEntry.grid(row = 1, column = 1, pady = 10)

#Setup course selection
mathCourses = ["Calculus I", "Calculus I/II", "Calculus II/III", "Connections in Mathmatics"]
scienceCourses = ["Computer Science", "Anatomy and Physiology"]
seniorSeminarCourses = ["3D Printing and Design", "Drone Technology", "Photoshop", "Video Editing"]
mathSelectedCourse = StringVar()
scienceSelectedCourse = StringVar()
seniorSeminarSelectedCourse = StringVar()
mathSelectedCourse.set("Choose Math")
scienceSelectedCourse.set("Choose Science")
seniorSeminarSelectedCourse.set("Choose Tech Lab")
mathDropdown = ttk.Combobox(inputFrame, values = mathCourses, textvariable = mathSelectedCourse, state = "readonly")
scienceDropdown = ttk.Combobox(inputFrame, values = scienceCourses, textvariable = scienceSelectedCourse, state = "readonly")
seniorSeminarDropdown = ttk.Combobox(inputFrame, values = seniorSeminarCourses, textvariable = seniorSeminarSelectedCourse, state = "readonly")
mathDropdown.grid(row = 2, column = 0, padx = 10, pady = 10)
scienceDropdown.grid(row = 2, column = 1, padx = 10, pady = 10)
seniorSeminarDropdown.grid(row = 2, column = 2, padx = 10, pady = 10)

#setup session selection
sessionSelected = IntVar()
sessionOneButton = Radiobutton(inputFrame, text="Session 1", variable = sessionSelected, value = 1)
sessionTwoButton = Radiobutton(inputFrame, text="Session 2", variable = sessionSelected, value = 2)
sessionOneButton.grid(row = 3, columnspan = 3)
sessionTwoButton.grid(row = 4, columnspan = 3)

#setup button
finishButton = Button(inputFrame, text="Click to Select", command = processSelection)
finishButton.grid(row = 5, columnspan = 3, pady = 10)

inputFrame.pack()
window.mainloop()
