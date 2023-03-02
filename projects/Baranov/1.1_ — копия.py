
def oleg_talk(text: str):
    print(f"[Олег]: {text}")

def user_talk(name: str):
    return input(f"[{name}]:").lower()

oleg_talk("Привет. Как тебя зовут? ")
name = user_talk("Переменная").title()
oleg_talk("приятно познакомится.Меня зовут Олег")

oleg_talk(f"{name}, где вы живете?")
city = user_talk(name).title()

while True:
    answer = user_talk(name)
    if "погод" in answer or "температура" in answer:
        talk_abaut_weather(city)
    elif "выход" in answer or "пока" in answer:
        break

