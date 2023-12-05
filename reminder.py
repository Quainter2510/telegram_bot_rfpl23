from config_data.config import ADMIN_ID
from loader import bot, base

bot.send_message(ADMIN_ID, "reminder start")
players = base.reminder(base.get_now_tour())
for elem in players:
    bot.send_message(elem[0], "Матчи скоро начнутся. Не забудьте сделать прогноз")
    bot.send_message(ADMIN_ID, base.get_nickname_player(elem[0]) + " не сделал прогноз")
bot.send_message(ADMIN_ID, "reminder finish")