from loader import base


base.update_result_tour()
currtour = base.get_now_tour()
for id in base.get_all_id_player():
    base.update_tournament_table(id[0], currtour - 1, base.number_of_points_per_tour(id[0], currtour - 1))
    base.update_tournament_table(id[0], currtour, base.number_of_points_per_tour(id[0], currtour))