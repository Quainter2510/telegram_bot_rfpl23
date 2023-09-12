from loader import bot, base
from typing import NoReturn
from telebot.types import Message
from keyboards.reply import keyboards
from config_data import config


@bot.message_handler(commands=["update"])
def update(message: Message):
    if not config.ALL_FUNCTION_READY:
        bot.reply_to(message, "Функция временно недоступна", reply_markup=keyboards.main_menu_marcup())
        return
    currtour = base.get_now_tour()
    for id in base.get_all_id_player():
        base.update_tournament_table(id[0], currtour - 1, base.number_of_points_per_tour(id[0], currtour - 1))
        base.update_tournament_table(id[0], currtour, base.number_of_points_per_tour(id[0], currtour))

    bot.reply_to(message, "Таблица успешно обновлена")