from tkinter import *
def callback(var):
   content= var.get()[0]
   if content.isalpha():
      e1.delete(0, END)   
      e1.insert(0, content)
   else:
      e1.delete(0,END)
root = Tk()
root.geometry("275x275")
root.config(bg="red")
user_name = Label(root,text = "Crossword",font=20,width=10,height=2).grid(row =0,column=100) 
button = Button(root, text='    ', bg='black' ,state=DISABLED)
button.grid(row=0, column=1)
button1 = Button(root, text='    ', bg='black' ,state=DISABLED)
button1.grid(row=1, column=3)
button2 = Button(root, text='    ', bg='black' ,state=DISABLED)
button2.grid(row=2, column=3)
button2 = Button(root, text='    ', bg='black' ,state=DISABLED)
button2.grid(row=3, column=2)
button2 = Button(root, text='    ', bg='black' ,state=DISABLED)
button2.grid(row=4, column=0)
var = StringVar()
var.trace("w", lambda name, index,mode, var=var: callback(var))
#Create an Entry widget
e1 = Entry(root, textvariable=var,width=2,font=2)
e1.grid(row=0,column=0)
e1 = Entry(root, textvariable=var,width=2,font=2)
e1.grid(row=0,column=2)
e1 = Entry(root, textvariable=var,width=2,font=2)
e1.grid(row=0,column=3)
e1 = Entry(root, textvariable=var,width=2,font=2)
e1.grid(row=0,column=4)
root.mainloop()
