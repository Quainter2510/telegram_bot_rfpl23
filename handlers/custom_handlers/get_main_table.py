from loader import bot, base
from keyboards.reply import my_marcup
from image_creator import table_creator
from config_data import config
# from handlers.default_handlers.player_list import show_player_list


def show_player_list(id: int):
    msg = 'Текущий список участников: \n'
    for num, player in enumerate(base.get_all_id_player(), start=1):
        msg += str(num) + " " + player[1] + '\n'
    bot.send_message(id, msg)

def check_result_tournament(id: int) -> None:
    if not config.ALL_FUNCTION_READY:
        bot.send_message(id, "Функция временно недоступна", reply_markup=my_marcup.main_menu_marcup())
        show_player_list(id)
        return
    
    res = base.get_result_tournament()
    res.sort(key=lambda x: x[config.SUM_COLUMN], reverse=True)
    ans = []
    # player: nick, id, last_pos, tourN, sum
    for player in res:
        user_data = [str(player[config.NICKNAME_COLUMN])] + list(map(str, player[config.TOUR1_COLUMN:config.TOUR1_COLUMN + 15])) + [str(player[config.SUM_COLUMN])]
        ans.append(user_data)
    table_creator.main_table(ans, base.get_now_tour())
    bot.send_photo(id, open("images/ready_tables/main_table.png", 'rb'))