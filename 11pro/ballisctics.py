from tkinter import *
import math


W = 1250
H = 1000
# metres in 1 px
grid_step = 25
g = 9.8


def calculate(event):
    scale = float(scale_entry.get())
    angle = int(angle_entry.get())
    v0 = int(speed_entry.get())
    raw_points = list()
    points = list()
    t = 0
    x = y = 0
    while y >= 0:
        x = v0 * math.cos(math.radians(angle)) * t
        y = v0 * math.sin(math.radians(angle)) * t - g * t ** 2 / 2
        t += 1
        raw_points.append((x, y))
        x1, y1 = transform_coords(scale, x, y)
        create_point(3, x1, y1)
        canvas.create_text(x1 - grid_step, y1 - grid_step, text=f'{int(x)}; {int(y)}', fill='black')
        points.append((x1, y1))
    canvas.create_line(*points, fill='red', width=2)


def create_point(size, x, y):
    canvas.create_oval(x - size, y - size, x + size, y + size, fill='black')


def transform_coords(scale, *coords):
    x = int(coords[0] * scale)
    y = H - int(coords[1] * scale)
    return x, y


def draw_grid(canvas):
    for x in range(0, W, grid_step):
        canvas.create_line((x, 0), (x, H), fill='black')
    for y in range(0, H, grid_step):
        canvas.create_line((0, y), (W, y), fill='black')


root = Tk()
canvas_frame = Frame()
input_frame = Frame()
canvas = Canvas(canvas_frame, height=H, width=W)
draw_grid(canvas)

speed_label = Label(input_frame, text='Введите начальную скорость')
speed_entry = Entry(input_frame)
angle_label = Label(input_frame, text='Введите угол')
angle_entry = Entry(input_frame)
scale_label = Label(input_frame, text='Укажите масштаб')
scale_entry = Entry(input_frame)
start_button = Button(input_frame, text='Рассчитать')
start_button.bind('<Button-1>', calculate)

speed_label.pack()
speed_entry.pack()
angle_label.pack()
angle_entry.pack()
scale_label.pack()
scale_entry.pack()
start_button.pack()
input_frame.pack(side=LEFT)

canvas.pack()
canvas_frame.pack(side=LEFT)

root.mainloop()