from telebot import TeleBot
# from telebot.storage import StateMemoryStorage
from config_data import config
from database.common import MyDataBase

# storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN)
base = MyDataBase()