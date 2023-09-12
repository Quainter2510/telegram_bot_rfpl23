from loader import bot, base
from keyboards.reply import keyboards
from typing import List
from telebot.types import Message
from helper_function import helper_func
from config_data import config, relations


def change_choice_tour(message: Message) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.reply_to(message, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.reply_to(message, "Тур указан неверно")
        bot.register_next_step_handler(message, change_choice_tour)
        return

    gtour = relations.HUMAN_DCT[message.text]
    matches = base.get_tour_matches(gtour)
    if not len(matches):
        bot.reply_to(message, "Время прогноза истекло", reply_markup=keyboards.main_menu_marcup())
        return
    bot.reply_to(message, "Выберите матч", reply_markup=keyboards.matches_tour_marcup(matches))
    bot.register_next_step_handler(message, match_selection, matches)


def match_selection(message: Message, matches: List) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.reply_to(message, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    if (message.text,) not in matches:
        bot.reply_to(message, "Матч указан неверно")
        bot.register_next_step_handler(message, match_selection)
        return
    matches = message.text
    bot.reply_to(message, "Введите счет")
    bot.register_next_step_handler(message, set_match_score, matches)



def set_match_score(message: Message, matches: List) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.reply_to(message, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    res = message.text.split()
    if not helper_func.check_correct_score(res):
        bot.reply_to(message, "Прогноз некорректен, введите еще раз")
        bot.register_next_step_handler(message, set_match_score, matches)
        return
    player_score = ':'.join(message.text.split())
    if not base.change_forecast(message.chat.id, matches, player_score):
        bot.reply_to(message, "Время прогноза истекло", reply_markup=keyboards.main_menu_marcup())
    bot.reply_to(message, "Прогноз изменен", reply_markup=keyboards.main_menu_marcup())