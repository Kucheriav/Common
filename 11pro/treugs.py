from tkinter import *

root = Tk()
c = Canvas(root, width=500, height=500, bg='white')
a = 50
b = 50
x = 10
y = 10

n = int(input())

for j in range(n):
    for i in range(j + 1):
        c.create_oval((x, y), (x + a, y + b), fill="green")
        x += a + a // 2
    y += b + b // 2
    x = 10
c.pack()
root.mainloop()