from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')
root.title('Simple Interest')
p = IntVar()
r = IntVar()
t = IntVar()

def clicked():
    P = p.get()
    R = r.get()
    T = t.get()
    si = (P*R*T)/100
    messagebox.showinfo("Simple Interest", "Your interest is"+str(si))

Label(root, text = "Principal Value: ").grid(column=0,row=0)
Label(root, text=  "Rate Value: ").grid(column=0, row =1)
Label(root, text = "Time Value: ").grid(column=0, row =2)

Entry(root, textvariable=p).grid(column=1,row=0)
Entry(root, textvariable=r).grid(column=1,row=1)
Entry(root, textvariable=t).grid(column=1, row=2)

Button(root, text="click me", command=clicked).grid(column=1, row=3)

root.mainloop()