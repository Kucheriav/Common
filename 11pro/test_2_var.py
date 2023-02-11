from tkinter import *

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000

def draw(event):
    n, m, z = map(int, entry.get().split())
    x0 = 50
    y0 = 50
    c.create_rectangle((x0, y0), (x0 + n, y0 + m))
    step = n // (z + 1)
    for i in range(z):
        x0 += step
        c.create_line((x0, y0), (x0, y0 + m), fill='blue', width=5)


root = Tk()
frame = Frame()
label = Label(frame, text='Введите размеры через пробел')
entry = Entry(frame)
button = Button(frame, text='ОК')
button.bind('<Button-1>', draw)
c = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
frame.pack()
label.pack(side=LEFT)
entry.pack(side=LEFT)
button.pack(side=LEFT)
c.pack()
root.mainloop()
