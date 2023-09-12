from loader import bot
import json
from config_data import config, load_settings
from telebot.types import Message

@bot.message_handler(commands=["settings"])
def set_settings(message: Message):
    if message.chat.id != config.ADMIN_ID:
        return
    setting = message.split()[1]
    value = " ".join(message.split()[2:])
    with open("settings.json", "r+") as settings:
        setup = json.load(settings)
        if setting not in setup.keys():
            bot.reply_to(message, "Параметр не найден")
            bot.reply_to(message, "\n".join(setup.keys()))
            return
        setup[setting] = value
        json.dump(setup, settings)
    load_settings()
