from tkinter import *

root = Tk()
c = Canvas(root, width=500, height=500, bg='white')
a = 300
b = 200
x = 10
y = 10

n = int(input())
c.create_rectangle((x, y), (x + a, y + b))
step = a // (n + 1)
for i in range(n):
    x += step
    c.create_line((x, y), (x, y + b), width=5, fill="green")
c.pack()
root.mainloop()