from tkinter import *

def plus(event):
    a = ent1.get()
    b = ent2.get()
    lab['text'] = int(a) + int(b)

def minus(event):
    a = ent1.get()
    b = ent2.get()
    lab['text'] = int(a) - int(b)

def umnozh(event):
    a = ent1.get()
    b = ent2.get()
    lab['text'] = int(a) * int(b)

def delete(event):
    a = ent1.get()
    b = ent2.get()
    if b != 0:
        lab['text'] = int(a) / int(b)
    else:
        lab['text'] = 'ERROR'

root = Tk()
print(root.keys())
frame1 = Frame(width=150)
frame2 = Frame()
ent1 = Entry(frame1, width=10)
ent2 = Entry(frame1, width=10)
but1 = Button(frame2, text='+', width=5)
but2 = Button(frame2, text='-', width=5)
but3 = Button(frame2, text='*', width=5)
but4 = Button(frame2, text='/', width=5)
lab = Label(width=20)

but1.bind('<Button-1>', plus)
but2.bind('<Button-1>', minus)
but3.bind('<Button-1>', umnozh)
but4.bind('<Button-1>', delete)

frame1.pack()
ent1.pack(side=LEFT)
ent2.pack(side=RIGHT)
frame2.pack()
but1.pack(side=LEFT)
but2.pack(side=LEFT)
but3.pack(side=LEFT)
but4.pack(side=LEFT)
lab.pack()

root.mainloop()