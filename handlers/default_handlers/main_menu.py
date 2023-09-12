from loader import bot
from keyboards.reply.keyboards import short_tour_menu_marcup, main_menu_marcup
from handlers.custom_handlers import *


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == "Сделать прогноз":
        bot.send_message(message.chat.id, "Выберите тур", reply_markup=short_tour_menu_marcup())
        bot.register_next_step_handler(message, set_tour_forecast)
    elif message.text == "Изменить прогноз":
        bot.send_message(message.chat.id, "Выберите тур", reply_markup=short_tour_menu_marcup())
        bot.register_next_step_handler(message, change_match_forecast)
    elif message.text == "Посмотреть итог тура":
        bot.send_message(message.chat.id, "Выберите тур", reply_markup=short_tour_menu_marcup())
        bot.register_next_step_handler(message, get_result_tour)
    elif message.text == "Посмотреть свой прогноз":
        bot.send_message(message.chat.id, "Выберите тур", reply_markup=short_tour_menu_marcup())
        bot.register_next_step_handler(message, get_my_forecast)
    elif message.text == "Посмотреть турнирную таблицу":
        get_main_table(message.chat.id)
    elif message.text == "Посмотреть прогноз всех участников":
        bot.send_message(message.chat.id, "Выберите тур", reply_markup=short_tour_menu_marcup())
        bot.register_next_step_handler(message, other_forecast)
    elif message.text == "Обновить":
        update(message)
    elif message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=main_menu_marcup())