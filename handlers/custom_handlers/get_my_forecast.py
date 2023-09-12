from loader import bot, base
from keyboards.reply import keyboards
from config_data import config
from helper_function import helper_func
from telebot.types import Message


def check_forecast_tour(message: Message) -> None:
    if message.text.lower() in ("вернуться в меню", "сброс"):
        bot.reply_to(message, "Вы вернулись в главное меню",
                         reply_markup=keyboards.main_menu_marcup())
        return
    if not helper_func.check_correct_tour(message.text):
        bot.reply_to(message, "Тур указан неверно")
        bot.register_next_step_handler(message, check_forecast_tour)
        return
    output_forecast(message.text, message.chat.id)

def output_forecast(selected_tour: str, id: int) -> None:
    ans = f"Ваш прогноз на {selected_tour}:\n"
    res = base.get_forecast_tour(id, relations.HUMAN_DCT[selected_tour])
    for match in res:
        name = match.split("—")
        ans += name[0] + " " + name[2] + " " + name[1] + '\n'
    bot.reply_to(id, ans, reply_markup=keyboards.main_menu_marcup())