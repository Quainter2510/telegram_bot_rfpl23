from loader import bot, base
from config_data import config
from telebot.types import Message 
from keyboards.reply import my_marcup


@bot.message_handler(commands=["start"])
def start(message: Message):
    if base.get_now_tour() > 1:
        bot.send_message(message.chat.id, "Вы не можете принять участие в турнире")
        return
    if base.check_player_in_tournament(message.chat.id):
        bot.send_message(message.chat.id, "Вы уже зарегистрированы в турнире",
                         reply_markup=my_marcup.main_menu_marcup())
        return
    bot.send_message(message.chat.id, "Введите имя, которое будет выводиться в таблицу")
    bot.register_next_step_handler(message, set_nickname)

def set_nickname(message: Message):
    bot.send_message(message.chat.id, config.start_info_msg)
    bot.send_message(config.ADMIN_ID, str(message.chat.id) + " " + message.text)
    




