from tkinter import *

def openFile():
    ftypes = [("Text files","*.txt"),
            ("Python files", "*.py"),
            ("HTML files","*.htm"),
            ("All files","*.*")]
    
    filenameforReading = filedialog.askopenfilename(filetypes = ftypes)
    infile = open(filenameforReading, 'r')
    text.delete("1.0", END)
    text.insert(END, infile.read())
    infile.close()
    return

def openEncryptedFile():
    offset = 5
    ftypes = [("Encrypted files","*.encrypt"),
            ("Text files","*.txt"),
            ("HTML files","*.htm"),
            ("Python files", "*.py"),
            ("All files","*.*")]
    filenameforReading = filedialog.askopenfilename(filetypes = ftypes)
    inputFile = open(filenameforReading, 'r')
    text.delete("1.0", END)
    encryptedText = inputFile.read()
    newString = ""
    for i in range(len(encryptedText)):
        newChrInt = ord(encryptedText[i]) - offset
        newChr = chr(newChrInt)
        newString = newString + newChr
    text.insert(END, newString)
    inputFile.close()
    return

def saveFile():
    filenameforWriting = filedialog.asksaveasfilename(defaultextension='.txt')
    outfile = open(filenameforWriting, 'w')
    outfile.write(text.get(1.0, END))
    outfile.close()
    return

def saveEncryptedFile():
    offset = 5
    filenameforWriting = filedialog.asksaveasfilename(defaultextension='.encrypt')
    outfile = open(filenameforWriting, 'w')
    originalString = text.get(1.0, END)
    newString = ""
    for i in range(len(originalString)):
        newChrInt = ord(originalString[i]) + offset
        newChr = chr(newChrInt)
        newString = newString + newChr
    outfile.write(newString)
    outfile.close()
    return

def exitEditor():
    window.destroy()
    return

window=Tk()
window.title('Simple Text Editor')

menubar = Menu(window)
window.config(menu=menubar)

operationMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = operationMenu)
operationMenu.add_command(label = 'New')
operationMenu.add_command(label = 'Open', command = openFile)
operationMenu.add_command(label = 'Open Encrypted File', command = openEncryptedFile)
operationMenu.add_command(label = 'Save', command = saveFile)
operationMenu.add_command(label = 'Save as Encrypted', command = saveEncryptedFile)
operationMenu.add_separator()
operationMenu.add_command(label = 'Exit', command = exitEditor)

helpMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = helpMenu)
helpMenu.add_command(label = 'You will not find help here!')


frame1 = Frame(window)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = Y)
text = Text(frame1, width=40, height=20, wrap = WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

frame1.pack()

window.mainloop()
   
