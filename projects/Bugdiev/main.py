# импортируем tkinter
import tkinter
# размеры сетки
N_X = 50
N_Y = 40
# сторона квадрата в сетке
step = 25
# начальная формула
graphs = []
intersection_points = []


# функция прекращения работы которую будем использовать в кнопке
def stop_the_program():
    # следующая строчка нужна для закрытия окна
    window.destroy()


# функция для удаления всех графиков
def del_all_graphs():
    global graphs, intersection_points
    for graph in graphs:
        canvas.delete(graph[0])
    graphs = []
    text2.set('Графики:'.ljust(30, ' '))
    for point in intersection_points:
        canvas.delete(point[1])
    intersection_points = []
    text1.set('Точки пересечения:')


# функция для создания формулы через кнопки
def add_member(member):
    # строка для сохранения текста из строки ввода
    expression = entry.get()
    entry.delete(0, 'end')
    if member in ('+', '-', 'x', 'x^2', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        entry.insert(0, expression + member)


# поиск точек пересечения
def draw_show_intersection_points():
    # проверяем больше ли 2 кол-во графиков
    if len(graphs) > 1:
        text1.set('Точки пересечения:')
        # цикл для взятия графика
        for i in range(len(graphs) - 1):
            # цикл для взятия другого графика и поиска точек пересечения с первым
            for j in range(i + 1, len(graphs)):
                new_formula = {'x^2': 0,  'x': 0, '': 0}
                # цикл для приравнивания графиков
                for coefficient in new_formula:
                    new_formula[coefficient] = graphs[i][1][coefficient] - graphs[j][1][coefficient]
                poses = []
                if new_formula['x^2'] and new_formula['x']:
                    d = (new_formula['x'] ** 2) - (4 * new_formula['x^2'] * new_formula[''])
                    if d < 0:
                        continue
                    else:
                        for a in range(-1, 2, 2):
                            poses.append([])
                            poses[-1].append(((-new_formula['x']) + a * (d ** 0.5)) / (2 * new_formula['x^2']))
                            poses[-1].append(
                                poses[a][0] ** 2 * graphs[i][1]['x^2'] +
                                + poses[a][0] * graphs[i][1]['x'] + graphs[i][1][''])
                elif new_formula['x^2']:
                    if -new_formula[''] / new_formula['x^2'] >= 0:
                        for a in range(-1, 2, 2):
                            poses.append([])
                            poses[-1].append(a * (-new_formula[''] / new_formula['x^2']) ** 0.5)
                            poses[-1].append(poses[a][0] ** 2 * graphs[i][1]['x^2'] + graphs[i][1][''])
                    else:
                        continue
                elif new_formula['x']:
                    poses.append([])
                    poses[-1].append(-new_formula[''] / new_formula['x'])
                    poses[-1].append(graphs[i][1]['x'] * poses[-1][0] + graphs[i][1][''])
                for a in range(len(poses)):
                    intersection_points.append((canvas.create_oval(
                        (N_X * step // 2 - -(poses[a][0] * step) - 3, (N_Y * step) // 2 - (poses[a][1] * step) - 3),
                        (N_X * step // 2 - -(poses[a][0] * step) + 3, (N_Y * step) // 2 - (poses[a][1] * step) + 3),
                        fill='green')))
                    new_text = text1.get() + '\n'
                    text1.set(new_text + f'{(poses[a][0], poses[a][1])}')


# функция для складывания членов формулы функции
def calculator(expression):
    # создание формулы функции
    formula = {'x^2': 0,  'x': 0, '': 0}
    try:
        # удаление пробелов если таковые имеются
        # замена минуса на плюс и минус (особенности программы)
        expression = expression.replace(' ', '').replace('-', '+-').split('+')
        # обнуление формулы
        for coef in formula:
            formula[coef] = 0
        # читание членов функции
        for member in expression:
            # *особенность программы*
            if not member:
                continue
            # поиск квадратов
            elif 'x^2' in member or 'x*x' in member:
                if not member[:-3]:
                    formula['x^2'] += 1
                elif member[:-3] == '-':
                    formula['x^2'] -= 1
                else:
                    formula['x^2'] += float(member[:-3])
            # поиск x
            elif 'x' in member:
                if not member[:-1]:
                    formula['x'] += 1
                elif member[:-1] == '-':
                    formula['x'] -= 1
                else:
                    formula['x'] += float(member[:-1])
            # поиск чисел
            else:
                formula[''] += float(member)
    except:
        pass
    return formula


# функция для рисования графика
def draw_graph():
    # получение формулы
    formula = calculator(entry.get())
    # список точек по которым мы будем рисовать график
    points = []
    # цикл для определения точек
    for x in range(-N_X * 4, N_X * 4):
        x /= 4
        y = 0
        y += x ** 2 * formula['x^2']
        y += x * formula['x']
        y += formula['']
        # добавление позиции точки
        points.append((N_X * step // 2 - -(x * step), N_Y * step // 2 - y * step))
    # отрисовываем график и добовляем его в список с графиками
    graphs.append([canvas.create_line(*points, fill='red', width=2), formula])
    new_text = text2.get() + '\n'
    formula_text = []
    for m in formula:
        if not formula[m] - int(formula[m]):
            formula[m] = int(formula[m])
        if formula[m] < 0:
            formula_text.append(f'({str(formula[m]) + m})')
        elif formula[m]:
            formula_text.append(f'{str(formula[m]) + m}')
    text2.set(new_text + ' + '.join(formula_text))


# определяем функцию где будет весь основной код
def main():
    global graphs
    # основные кнопки
    # создаём кнопку для закрытия окна
    tkinter.Button(window, text='Прекратить работу', command=stop_the_program).place(x=0, y=200)
    # кнопка для рисования графика
    tkinter.Button(window, text='Нарисовать график', command=draw_graph).place(x=0, y=350)
    # кнопка для удаления всех графиков
    tkinter.Button(window, text='Удалить все графики', command=del_all_graphs).place(x=0, y=400)
    # кнопка для рисования и показа точек пересечения
    tkinter.Button(window, text='Нарисовать и показать пересечения',
                   command=draw_show_intersection_points).place(x=0, y=450)

    # кнопка +
    tkinter.Button(window, text='+', command=lambda: add_member('+')).place(x=0, y=500)
    # кнопка -
    tkinter.Button(window, text='-', command=lambda: add_member('-')).place(x=30, y=500)
    # кнопка для добавления x
    tkinter.Button(window, text='X', command=lambda: add_member('x')).place(x=0, y=550)
    # кнопка для добавления квадрата x
    tkinter.Button(window, text='X^2', command=lambda: add_member('x^2')).place(x=30, y=550)

    # цифры
    tkinter.Button(window, text='1', command=lambda: add_member('1')).place(x=0, y=600)
    tkinter.Button(window, text='2', command=lambda: add_member('2')).place(x=30, y=600)
    tkinter.Button(window, text='3', command=lambda: add_member('3')).place(x=60, y=600)
    tkinter.Button(window, text='4', command=lambda: add_member('4')).place(x=0, y=650)
    tkinter.Button(window, text='5', command=lambda: add_member('5')).place(x=30, y=650)
    tkinter.Button(window, text='6', command=lambda: add_member('6')).place(x=60, y=650)
    tkinter.Button(window, text='7', command=lambda: add_member('7')).place(x=0, y=700)
    tkinter.Button(window, text='8', command=lambda: add_member('8')).place(x=30, y=700)
    tkinter.Button(window, text='9', command=lambda: add_member('9')).place(x=60, y=700)

    # отрисовываем линии
    for i in range(1, N_X):
        if i == N_X // 2:
            canvas.create_line(
                (i * step, 0), (i * step, N_Y * step), fill='grey')
        else:
            canvas.create_line(
                (i * step, 0), (i * step, N_Y * step), fill='black')
        # метка для оси Ox
        canvas.create_text(
            i * step, N_Y // 2 * step + 10, text=str(i - N_X // 2), fill='white')
    # отрисовываем линии
    for i in range(1, N_Y):
        if i == N_Y // 2:
            canvas.create_line(
                (0, i * step), (N_X * step, i * step), fill='grey')
        else:
            canvas.create_line(
                (0, i * step), (N_X * step, i * step), fill='black')
        # метка для оси Oy
        canvas.create_text(
            N_X // 2 * step + 10, i * step, text=str(N_Y // 2 - i), fill='white')


# создаём окно
window = tkinter.Tk()
# меняем цвет заднего фона окна
window['bg'] = '#101010'

text1 = tkinter.StringVar()
text1.set('Точки пересечения:')
text2 = tkinter.StringVar()
text2.set('Графики:'.ljust(30, ' '))

# создаём окно ввода
entry = tkinter.Entry(window, width=30)
# отображаем окно ввода в окне программы
entry.pack(side='top', pady=1)

# создём холст в котором мы и будем отрисовывать график
canvas = tkinter.Canvas(window, bg='#101010', height=N_Y * step, width=N_X * step)
# вызываем фунцию main
main()
# добавляем холст в окно
canvas.pack()

# текст
label1 = tkinter.Label(window, textvariable=text1)
label2 = tkinter.Label(window, textvariable=text2)
# отображаем текст
label1.place(x=1600, y=10)
label2.place(x=1600, y=700)

# следующая строчка отвечает за полноэкранный режим окна
window.attributes('-fullscreen', True)
# основной цикл
window.mainloop()
