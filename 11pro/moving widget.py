from tkinter import *

class MyButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_picked = False

def set_state(event):
    # print(event)
    if event.widget.is_picked:
        event.widget.is_picked = False
    else:
        event.widget.is_picked = True


def move(event):
    x = event.x
    y = event.y
    if but.is_picked:
        but.place(relx=0, rely=0,x=event.x, y=event.y, anchor='nw')
    s = "Движение мышью {}x{}".format(x, y)
    lab1['text'] = s



def move_button(event):
    if event.keycode == 37:
        but.place(x=but.winfo_x() - 5)


root = Tk()
root.minsize(width=500, height=400)
lab1 = Label()
lab2 = Label()
lab3 = Label()
but = MyButton(root, text='Тащи меня')
but.bind('<Button-1>', set_state)
root.bind('<Motion>', move)
# root.bind('<Up>', move_button)
# root.bind('<Down>', move_button)
# root.bind('<Right>', move_button)
# root.bind('<Left>', move_button)
lab1.place(relx=0.5, rely=0.1, anchor=CENTER)
but.place(relx=0.1, rely=0.1, anchor=CENTER)
root.mainloop()