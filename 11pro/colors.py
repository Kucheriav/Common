from tkinter import *

# def set_text(event, n):
#     lab1['text'] = colors[n][1]
#     lab2['text'] = colors[n][0]

root = Tk()

# frames = [Frame(), Frame()]
lab1 = Label(width=20,text='label1')
lab2 = Label(width=20, text='label2')
# print(lab1.keys())
# colors = [['#ff0000', 'красный'],
#           ['#ff7d00', 'оранжевый'],
#           ['#ffff00', 'желтый'],
#           ['#00ff00', 'зеленый'],
#           ['#007dff', 'голубой'],
#           ['#0000ff', 'синий'],
#           ['#7d00ff', 'фиолетовый']
#           ]
frame1 = Frame()
frame2 = Frame()
but1 = Button(frame1, text='1', width=5)
but2 = Button(frame1, text='2', width=5)
but3 = Button(frame1, text='3', width=5)
but4 = Button(frame2, text='4', width=5)
but5 = Button(frame2, text='5', width=5)
but6 = Button(frame2, text='6', width=5)

# buttons = []
# for i in range(6):
#     buttons.append(Button(frames[i % 2], text=f'{i + 1}', width=5, bg=colors[i][0]))
#     buttons[i].bind('<Button-1>', lambda e, n=i: set_text(e,n))

lab1.pack()
lab2.pack()
frame1.pack()
frame2.pack()
but1.pack(side=LEFT)
but2.pack(side=LEFT)
but3.pack(side=LEFT)
but4.pack(side=LEFT)
but5.pack(side=LEFT)
but6.pack(side=LEFT)


# for frame in frames:
#     frame.pack()
# for button in buttons:
#     button.pack(side=LEFT)



root.mainloop()