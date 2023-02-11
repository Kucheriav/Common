from tkinter import *

root = Tk()
x = 4
c = Canvas(root, width=300, height=300, bg='white')
c.create_rectangle((50 * x, 50 * x),(90 * x, 100 * x), fill='green', outline='black')
c.create_polygon((40 * x, 50 * x), (100 * x, 50 * x), (70 * x, 20 * x), fill='blue')
c.create_rectangle((60 * x, 60 * x),(80 * x, 85 * x), fill='black', outline='white', width=5)
c.pack()
root.mainloop()