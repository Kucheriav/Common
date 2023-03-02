import telebot
import pyowm
from pyowm.utils.config import get_default_config

api_token = "5910410294:AAE-As5x0JC1ezZ0MpxVizE-hTF05dwYfDA"
bot = telebot.TeleBot(api_token)
waiting_for_city = False

def weather_now(name_of_citi):
    config_dick = get_default_config()
    config_dick["language"] = "ru"
    owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc", config_dick)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(name_of_citi)
    return observation.weather

@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(commands=["weather"])
def weather(message):
    global waiting_for_city
    bot.send_message(message.chat.id, "Укажи свой город")
    waiting_for_city = True


@bot.message_handler(func=lambda message: True)
def repeat(message):
    global waiting_for_city
    if waiting_for_city:
        try:
            weather = weather_now(message.text)
            waiting_for_city = False
            bot.send_message(message.chat.id, weather)
        except Exception:
            bot.send_message(message.chat.id, "Ошибка")
        # temp = int(weather.temperature("celsius")["temp"])
        # res = ''
        # res += f"на улице {weather.detailed_status}"
        # res += f"Температура {temp}"
        # if temp < -20:
        #     oleg_talk(f"советую одется очень тепло, на улице очень холодно")
        # elif -20 <= temp < -10:
        #     oleg_talk(f"советую тепло одется, на улице холодно")
        # elif -10 <= temp < 0:
        #     oleg_talk(f"советую хорошо одется, на улице холодновато")
        # elif 0 <= temp < 10:
        #     oleg_talk(f"советую одется потеплее, на улице прохладно")
        # elif 10 <= temp <= 20:
        #     oleg_talk(f"советую легко одеться, на улице тепло")
        # elif 20 <= temp < 30:
        #     oleg_talk(f"советую одеть легкую одежду так как на удице жара")
        # elif temp >= 30:
        #     oleg_talk(f"на улице жарища, одень шорты и майку")


bot.infinity_polling()