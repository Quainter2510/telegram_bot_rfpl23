from loader import bot, base
from telebot.types import Message

@bot.message_handler(commands=["delete"])
def delete_user(message: Message):
    base.delete_player(message.chat.id)
    bot.reply_to(message, "Вы успешно удалены")