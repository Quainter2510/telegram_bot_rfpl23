from loader import bot, base
from config_data import config
from telebot.types import Message 
from keyboards.reply import keyboards

@bot.message_handler(commands = ["add"])
def add_player(message: Message) -> None:
    # Админ добавляет пользователя после оплаты
    if message.chat.id != config.ADMIN_ID:
        return
    user_id = message.text.split()[1]
    user_nickname = " ".join(message.text.split()[2:])
    if base.check_player_in_tournament(user_id):
        bot.send_message(config.ADMIN_ID, "Этот игрок уже в турнире",
                        reply_markup=keyboards.main_menu_marcup())
        return
    base.add_player(user_id, user_nickname)
    bot.send_message(user_id, "Вы зарегистрированы в турнире",
                    reply_markup=keyboards.main_menu_marcup())
    bot.send_message(config.ADMIN_ID, "Игрок добавлен",
                    reply_markup=keyboards.main_menu_marcup())
