from loader import bot, base

def player_list(id: int):
    msg = 'Текущий список участников: \n'
    for num, player in enumerate(base.get_all_id_player(), start=1):
        msg += str(num) + " " + player[1] + '\n'
    bot.send_message(id, msg)