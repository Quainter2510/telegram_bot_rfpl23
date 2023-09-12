from loader import bot, base
from states.castom_states import CustomStates
from config_data import config
from telebot.types import Message 
from keyboards.reply import keyboards


@bot.message_handler(commands=["start"])
def start(message: Message):
    if base.get_now_tour() > 1:
        bot.reply_to(message, "Вы не можете принять участие в турнире")
        return
    if base.check_player_in_tournament(message.chat.id):
        bot.send_message(message.chat.id, "Вы уже зарегистрированы в турнире",
                         reply_markup=keyboards.main_menu_marcup())
        return
    bot.set_state(message.from_user.id, CustomStates.nickname, message.chat.id)
    bot.send_message(message.chat.id, "Введите имя, которое будет выводиться в таблицу")

@bot.message_handler(state=CustomStates.nickname)
def set_nickname(message: Message):
    bot.reply_to(message, config.start_info_msg)
    bot.send_message(config.ADMIN_ID, str(message.chat.id) + " " + message.text)
    




