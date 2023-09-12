from loader import bot, base
from telebot.types import Message
from config_data import config

@bot.message_handler(commands=["delete_user"])
def delete_user(message: Message) -> None:
    if message.chat.id != config.ADMIN_ID:
        return
    user_id = message.text.split()[1]
    base.delete_player(user_id)
    bot.send_message(user_id, "Вы удалены из турнира")
    bot.send_message(config.ADMIN_ID, "Аккаунт удален")

