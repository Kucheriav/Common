from tkinter import *
from tkinter import ttk

def show_message():
    try:
        gender = combobox_gender.get()
        weight = int(weight_entry.get())
        height = int(height_entry.get())
        age = int(age_entry.get())
        goal = goal_combobox.get()
        activity = level_combobox.get()
    except Exception:
        label["text"] = "Введено не число"
        return
    gender_dict = {'мужской': 5, 'женский': -161}
    goal_dict = {"поддержание массы": 1, "набор массы": 1.2, "похудение": 0.8}
    activity_dict = {"низкая": 1.2, "высокая": 1.9, "средняя": 1.4}
    weight_k = 10
    height_k = 6.25
    age_k = 5
    try:
        a = ((weight_k * weight + height_k * height - age_k * age + gender_dict[gender]) * activity_dict[activity]) * goal_dict[goal]
    except Exception:
        label["text"] = 'Не вся информация указана'
        return
    label["text"] = str(a), 'ккал в день'



root = Tk()
root.title('Калькулятор calories')
root.geometry("400x400+700+50")
root.resizable(width=True, height=True)


ttk.Label(text="Введите пол").pack(anchor=NW, padx=4, pady=4) # список для пола
gender = ['мужской', 'женский']
combobox_gender = ttk.Combobox(values=gender)
combobox_gender.pack(anchor=NW, padx=4, pady=4)


ttk.Label(text='введите массу').pack(anchor=NW, padx=4, pady=4) # поле ввода для массы
weight_entry = ttk.Entry()
weight_entry.pack(anchor=NW, padx=4, pady=4)


ttk.Label(text='Введите рост').pack(anchor=NW, padx=4, pady=4) # поле ввода для роста
height_entry = ttk.Entry()
height_entry.pack(anchor=NW, padx=4, pady=4)


ttk.Label(text="Введите возраст").pack(anchor=NW, padx=4, pady=4) # поле ввода для возраста
age_entry = ttk.Entry()
age_entry.pack(anchor=NW, padx=4, pady=4)


ttk.Label(text="Введите цель").pack(anchor=NW, padx=4, pady=4) # список для цели
goal = ['поддержание массы', 'набор массы', "похудение"]
goal_combobox = ttk.Combobox(values=goal)
goal_combobox.pack(anchor=NW, padx=4, pady=4)


ttk.Label(text="Введите уровень физической активности").pack(anchor=NW, padx=4, pady=4) # список для уровня нагрузки
level = ['низкая', 'средняя', 'высокая']
level_combobox = ttk.Combobox(values=level)
level_combobox.pack(anchor=NW, padx=4, pady=4)




btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=4, pady=4)


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)


root.mainloop()