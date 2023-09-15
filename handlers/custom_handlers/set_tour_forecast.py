from loader import bot, base
from config_data import relations
from keyboards.reply import my_marcup
from typing import List
from telebot.types import Message
from helper_function import helper_func
from handlers.custom_handlers.get_my_forecast import output_forecast


def set_tour_forecast(message: Message):
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.send_message(message.chat.id, "Тур указан неверно")
        bot.register_next_step_handler(message, set_tour_forecast)
        return

    selected_tour = relations.HUMAN_DCT[message.text]
    matches = base.get_tour_matches(int(selected_tour))
    if not len(matches):
        bot.send_message(message.chat.id, "Время прогонза истекло", reply_markup=my_marcup.main_menu_marcup())
        return
    
    bot.send_message(message.chat.id, matches[0])
    bot.register_next_step_handler(message, set_result, matches, selected_tour)


def set_result(message: Message, matches: List, selected_tour: int):
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    res = message.text.split()
    if not helper_func.check_correct_score(res):
        bot.send_message(message.chat.id, "Прогноз некорректен")
        bot.send_message(message.chat.id, matches[0])
        bot.register_next_step_handler(message, set_result, matches, selected_tour)
        return
    score = ':'.join(message.text.split())
    if not base.change_forecast(message.chat.id, matches[0][0], score):
        bot.send_message(message.chat.id, "Время прогонза истекло")
    del matches[0]
    if len(matches):
        bot.send_message(message.chat.id, matches[0][0])
        bot.register_next_step_handler(message, set_result, matches, selected_tour)
    else:
        output_forecast(selected_tour, message.chat.id)
