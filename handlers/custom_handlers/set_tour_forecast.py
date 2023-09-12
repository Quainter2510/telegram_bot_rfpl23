from loader import bot, base
from config_data import config
from keyboards.reply import keyboards
from typing import List
from telebot.types import Message
from helper_function import helper_func
from handlers.custom_handlers.get_my_forecast import output_forecast

def set_tour_forecast(message: Message):
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.reply_to(message, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.reply_to(message, "Тур указан неверно")
        bot.register_next_step_handler(message, set_tour_forecast)
        return

    selected_tour = relations.HUMAN_DCT[message.text]
    matches = base.get_tour_matches(int(selected_tour))
    if not len(matches):
        bot.reply_to(message, "Время прогонза истекло", reply_markup=keyboards.main_menu_marcup())
        return
    bot.reply_to(message, matches[0])
    bot.register_next_step_handler(message, set_result, matches, selected_tour)


def set_result(message: Message, matches: List, selected_tour: int):
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    res = message.text.split()
    if not helper_func.check_correct_score(res):
        bot.reply_to(message, "Прогноз некорректен")
        bot.reply_to(message, matches[0])
        bot.register_next_step_handler(message, set_result, matches, selected_tour)
        return
    score = ':'.join(message.text.split())
    if not base.change_forecast(message.chat.id, matches[0][0], score):
        bot.reply_to(message, "Время прогонза истекло")
    del matches[0]
    if len(matches):
        bot.send_message(message.chat.id, matches[0][0])
        bot.register_next_step_handler(message, set_result, matches, selected_tour)
    else:
        output_forecast("", message.chat.id)
