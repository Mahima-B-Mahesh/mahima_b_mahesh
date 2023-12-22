from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look I clicked a Button!",)
    myLabel.pack(side=LEFT, fill=X)

myButton = Button(
    root,
    text="Click Me!", command = myClick ,fg = "blue", bg = "green")

myButton.pack()

root.mainloop()
