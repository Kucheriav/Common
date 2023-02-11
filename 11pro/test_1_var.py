from tkinter import *

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000

def draw(event):
    n, m = map(int, entry.get().split())
    x0 = 50
    y0 = 50
    a = 50
    b = 50
    for y in range(m):
        for x in range(n):
            c.create_oval((x0, y0), (x0 + a, y0 + b), fill='green')
            x0 += a
        x0 = 50
        y0 += b

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
