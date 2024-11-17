from tkinter import *

#create a root window
root = Tk()

root.title("Welcome to Tkinter GUI")
root.geometry('350x400')

lbl = Label(root, text="How are you?")
lbl.grid()

root.mainloop()
