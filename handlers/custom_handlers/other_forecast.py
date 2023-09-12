from loader import bot, base
from telebot.types import Message
from keyboards.reply import keyboards
from helper_function import helper_function
from config_data import config
from image_creator import table_creator

def get_other_forecasts(message: Message):
    if not config.ALL_FUNCTION_READY:
        bot.send_message(id, "Функция временно недоступна", reply_markup=keyboards.main_menu_marcup())
        return
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.reply_to(message, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    if not helper_function.check_correct_tour(message.text):
        bot.reply_to(message, "Тур указан неверно")
        bot.register_next_step_handler(message, get_other_forecasts)
        return
    tour = config.HUMAN_DCT[message.text]
    if base.get_now_tour() < tour:
        bot.reply_to(message, "Дождитесь начала тура", reply_markup=keyboards.main_menu_marcup())
        return
    
    players = base.get_all_id_player()
    for id, nickname in players:
        res = base.get_result_tour(tour)
        points = 0
        data = []
        for match in res:
            self_res = base.get_other_forecast_match(id, match[0])
            points += helper_function.counting_of_points(match[1], self_res)
            data.append([match[0], match[1], self_res, helper_function.counting_of_points(match[1], self_res)])
        table_creator.result_tour(data, message.text, points, nickname)
        img = open("result_tour.png", 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=keyboards.main_menu_marcup())