from loader import bot, base
from keyboards.reply import keyboards
from config_data import config
from telebot.types import Message
from helper_function import helper_function
from image_creator import table_creator



def check_result_tour(message: Message):
    if not config.ALL_FUNCTION_READY:
        bot.send_message(id, "Функция временно недоступна", reply_markup=keyboards.main_menu_marcup())
        return

    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.send_message(message.chat.id, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    if not helper_function.check_correct_tour(message.text):
        bot.send_message(message.chat.id, "Тур указан неверно")
        bot.register_next_step_handler(message, check_result_tour)
        return
    res = base.get_result_tour(config.HUMAN_DCT[message.text])
    points = 0
    data = []
    currtour = config.HUMAN_DCT[message.text]
    for match in res:
        self_res = base.get_forecast_match(message.chat.id, match[0])
        points += helper_function.counting_of_points(match[1], self_res[0])
        data.append([match[0], match[1], self_res[0], helper_function.counting_of_points(match[1], self_res[0])])
    table_creator.result_tour(data, message.text, points)
    img = open("result_tour.png", 'rb')
    bot.send_photo(message.chat.id, img, reply_markup=keyboards.main_menu_marcup())
    table_creator.points_tour(base.get_points_of_tour(config.TOUR_DCT[currtour]), config.TOUR_DCT[currtour])
    img = open("points_tour.png", 'rb')
    bot.send_photo(message.chat.id, img, reply_markup=keyboards.main_menu_marcup())