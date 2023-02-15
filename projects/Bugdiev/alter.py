from tkinter import *
from tkinter import ttk


CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
font = ('Times New Roman', 14)

root = Tk()

inputs_frame = Frame()
functions = ['Линейная', 'Квадратичная', 'Кубическая']
label1 = Label(inputs_frame, text='Выберите тип функции', font=font)
function_dropdown = ttk.Combobox(inputs_frame, values=functions, font=font)
label2 = Label(inputs_frame, text='Подставьте коэфициенты', font=font)

label_frame = Frame(inputs_frame, borderwidth=3, relief=RIDGE)
label_a = Label(label_frame, text='a', font=font)
label_b = Label(label_frame, text='b', font=font, anchor=CENTER)
label_c = Label(label_frame, text='c', font=font, anchor=E)

entry_frame = Frame(inputs_frame, borderwidth=3, relief=RIDGE)
entry_a = Entry(entry_frame, width=5, font=font)
entry_b = Entry(entry_frame, width=5, font=font)
entry_c = Entry(entry_frame, width=5, font=font)

button = Button(inputs_frame, text='Рассчитать', font=font)

canvas_frame = Frame()
graphics_canvas = Canvas(canvas_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')


label1.pack(side=TOP)
function_dropdown.pack(side=TOP)
label2.pack(side=TOP)
label_a.pack(side=LEFT, expand=True)
label_b.pack(side=LEFT, expand=True)
label_c.pack(side=LEFT, expand=True)
label_frame.pack(side=TOP, fill=X)
entry_a.pack(side=LEFT, expand=True)
entry_b.pack(side=LEFT, expand=True)
entry_c.pack(side=LEFT, expand=True)
entry_frame.pack(side=TOP, fill=X)
inputs_frame.pack(side=LEFT)
button.pack(side=TOP, pady=10)
graphics_canvas.pack()
canvas_frame.pack(side=LEFT)
root.mainloop()