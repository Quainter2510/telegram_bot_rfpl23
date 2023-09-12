from loader import bot
from telebot.types import Message
from keyboards.reply import keyboards


@bot.message_handler(commands=["home"])
def home(message: Message):
    bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=keyboards.main_menu_marcup())