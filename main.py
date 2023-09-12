from loader import bot
from config_data import config
from keyboards.reply import keyboards
import handlers



if __name__ == '__main__':
    while True:
        try:
            bot.send_message(config.ADMIN_ID, "qwe")
            bot.polling(none_stop=True)
        except Exception as exc:
            bot.send_message(config.ADMIN_ID, exc, reply_markup=keyboards.main_menu_marcup())

# bot.polling(non_stop=True, interval=0)