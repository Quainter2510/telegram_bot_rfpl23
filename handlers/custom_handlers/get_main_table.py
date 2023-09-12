from loader import bot, base
from typing import NoReturn
from keyboards.reply import keyboards
from config_data import config
from default_handlers import player_list


def check_result_tournament(id: int) -> None:
    if not config.ALL_FUNCTION_READY:
        bot.send_message(id, "Функция временно недоступна", reply_markup=keyboards.main_menu_marcup())
        player_list(id)
        return
    
    res = base.get_result_tournament()
    res.sort(key=lambda x: x[config.SUM_COLUMN], reverse=True)
    ans = []
    # player: nick, id, last_pos, tourN, sum
    for player in res:
        user_data = [str(player[config.NICKNAME_COLUMN])] + list(map(str, player[config.TOUR1_COLUMN:config.TOUR1_COLUMN + 15])) + [str(player[config.SUM_COLUMN])]
        ans.append(user_data)
    main_table(ans, base.get_now_tour())
    bot.send_photo(id, open("main_table.png", 'rb'))