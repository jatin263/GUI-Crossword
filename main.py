from cProfile import label
from tkinter import *
def callback(var):
   content= var.get()[0]
   if content.isalpha():
      e1.delete(0, END)   
      e1.insert(0, content)
   else:
      e1.delete(0,END)
root = Tk()
root.geometry("1000x1000")
root.config(bg="blue")
user_name = Label(root,text = "Username",font=20,width=20,height=5).grid(row =0,column=20) 
button = Button(root, text='bbb', bg='black' ,state=DISABLED)
button.grid(row=1, column=0)
button1 = Button(root, text='bbb', bg='black' ,state=DISABLED)
button1.grid(row=2, column=0)
button2 = Button(root, text='bbb', bg='black' ,state=DISABLED)
button2.grid(row=4, column=7)
var = StringVar()
var.trace("w", lambda name, index,mode, var=var: callback(var))
#Create an Entry widget
e1 = Entry(root, textvariable=var,width=2,font=2)
e1.grid(row=2,column=1)
root.mainloop()
