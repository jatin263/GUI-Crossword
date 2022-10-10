from tkinter import *
def go():
    text = e1.get()[0]  
    e1.delete(0, END)  
    e1.insert(0, text)
root = Tk()
root.geometry("1000x1000")
button = Button(root, text='bbb', bg='black' ,state=DISABLED)
button.grid(row=0, column=0)
button1 = Button(root, text='bbb', bg='black' ,state=DISABLED)
button1.grid(row=1, column=0)
button2 = Button(root, text='bbb', bg='black' ,state=DISABLED)
button2.grid(row=4, column=7)
e1 = Entry(root,width=2,font=2)
e1.grid(row = 2, column = 1)
root.mainloop()
