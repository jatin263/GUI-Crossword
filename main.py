from tkinter import *
root = Tk()
root.geometry("1000x1000")
button = Button(root, text='bbb', bg='black' ,state=DISABLED)
button.grid(row=0, column=0)
button1 = Button(root, text='bbb', bg='black' ,state=DISABLED)
button1.grid(row=1, column=0)
e1 = Entry(root,width=2,font=2)
e1.grid(row = 2, column = 1)
root.mainloop()
#hello jatin