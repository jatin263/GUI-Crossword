#Import the Tkinter library
from tkinter import *
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry
win.geometry("750x250")
def callback(var):
   content= var.get()[0]
   e.delete(0, END)   #deletes everything
   e.insert(0, content)
   print(content)
#Create an variable to store the user-input
var = StringVar()
var.trace("w", lambda name, index,mode, var=var: callback(var))
#Create an Entry widget
e = Entry(win, textvariable=var)
e.pack()
win.mainloop()