from tkinter import *

def get_name(event):
    name = ent.get()
    lab['text'] = 'Привет, ' + name

root = Tk()
ent = Entry(width=20)
but = Button(text='OK')
lab = Label(width=20, text="Привет")

but.bind('<Button-1>', get_name)

ent.pack()
but.pack()
lab.pack()

root.mainloop()