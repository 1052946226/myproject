from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry('300x200')


frm = Frame(root)
Label(frm, text='校训', font=('Arial', 20)).pack(side=TOP)


root.mainloop()