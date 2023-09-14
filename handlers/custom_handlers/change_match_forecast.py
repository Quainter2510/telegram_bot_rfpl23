from loader import bot, base
from keyboards.reply import my_marcup
from typing import List
from telebot.types import Message
from helper_function import helper_func
from config_data import config, relations


def change_choice_tour(message: Message) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.send_message(message.chat.id, "Тур указан неверно")
        bot.register_next_step_handler(message, change_choice_tour)
        return

    gtour = relations.HUMAN_DCT[message.text]
    matches = base.get_tour_matches(gtour)
    if not len(matches):
        bot.send_message(message.chat.id, "Время прогноза истекло", reply_markup=my_marcup.main_menu_marcup())
        return
    bot.send_message(message.chat.id, "Выберите матч", reply_markup=my_marcup.matches_tour_marcup(matches))
    bot.register_next_step_handler(message, match_selection, matches)


def match_selection(message: Message, matches: List) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    if (message.text,) not in matches:
        bot.send_message(message.chat.id, "Матч указан неверно")
        bot.register_next_step_handler(message, match_selection)
        return
    matches = message.text
    bot.send_message(message.chat.id, "Введите счет")
    bot.register_next_step_handler(message, set_match_score, matches)



def set_match_score(message: Message, matches: List) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    res = message.text.split()
    if not helper_func.check_correct_score(res):
        bot.send_message(message.chat.id, "Прогноз некорректен, введите еще раз")
        bot.register_next_step_handler(message, set_match_score, matches)
        return
    player_score = ':'.join(message.text.split())
    if not base.change_forecast(message.chat.id, matches, player_score):
        bot.send_message(message.chat.id, "Время прогноза истекло", reply_markup=my_marcup.main_menu_marcup())
    bot.send_message(message.chat.id, "Прогноз изменен", reply_markup=my_marcup.main_menu_marcup())