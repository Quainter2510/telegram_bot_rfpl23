from telebot import types
from config_data import config
from loader import base


def main_menu_marcup() -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup()
    marcup.add(types.KeyboardButton("Сделать прогноз"),
               types.KeyboardButton("Изменить прогноз"),
               types.KeyboardButton("Посмотреть итог тура"),
               types.KeyboardButton("Посмотреть турнирную таблицу"),
               types.KeyboardButton("Посмотреть свой прогноз"),
               types.KeyboardButton("Обновить"),
               types.KeyboardButton("Сброс"),
               types.KeyboardButton("Посмотреть прогноз всех участников"))
    return marcup


def tour_menu_marcup() -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marcup.add(types.KeyboardButton("Вернуться в меню"))
    for i in config.HUMAN_DCT.keys():
        marcup.add(types.KeyboardButton(f"{i}"))
    return marcup


def short_tour_menu_marcup() -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marcup.add(types.KeyboardButton("Вернуться в меню"))
    now_tour = base.get_now_tour()[0]
    for i in list(config.HUMAN_DCT.keys())[now_tour - 3:min(now_tour + 3, max(config.TOUR_DCT.keys()) - 1)]:
        marcup.add(types.KeyboardButton(f"{i}"))
    return marcup


def matches_tour_marcup(mathes) -> types.ReplyKeyboardMarkup:
    marcup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marcup.add(types.KeyboardButton("Вернуться в меню"))
    for match in mathes:
        marcup.add(types.KeyboardButton(*match))
    return marcup