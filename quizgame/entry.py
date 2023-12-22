from tkinter import *

root = Tk()

e = Entry(root, text="", width=50, borderwidth=5)
e.pack(side=TOP, fill=X)
e.insert(0, "Enter your name: ")

def myClick():
    myLabel = Label(
        root,
        text="Hello" + e.get(),
    )
    myLabel.pack(side=LEFT, fill=X)


myButton = Button(root, text="Submit", command=myClick, fg="blue", bg="green")

myButton.pack()

root.mainloop()
