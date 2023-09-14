from config_data import relations
from typing import List

def check_correct_tour(str: str) -> bool:
    if str in relations.HUMAN_DCT.keys():
        return True
    return False


def counting_of_points(one: str, two: str) -> int:
    if one == "–:–" or two == "–:–":
        return 0
    one = list(map(int, one.split(":")))
    two = list(map(int, two.split(":")))
    if one == two and sum(one) >= 4:
        return 4
    elif one == two and sum(one) < 4 or ((one[0] == two[0] and abs(one[1] - two[1]) == 1 or
                                          one[1] == two[1] and abs(one[0] - two[0]) == 1) and
                                         sum(one) >= 4 and (one[0] > one[1]) == (two[0] > two[1]) and
                                         (one[0] < one[1]) == (two[0] < two[1])):
        return 3
    elif one[0] == one[1] and two[0] == two[1] and abs(one[0] - two[0]) == 1 or one[0] - one[1] == \
            two[0] - two[1] and one[0] != one[1] or (
            (one[0] == two[0] and abs(one[1] - two[1]) == 1 or
             one[1] == two[1] and abs(one[0] - two[0]) == 1) and
            sum(one) < 4 and (one[0] > one[1]) == (two[0] > two[1]) and
            (one[0] < one[1]) == (two[0] < two[1])):
        return 2
    elif one[0] > one[1] and two[0] > two[1] or one[0] == one[1] and two[0] == two[1] or one[0] < \
            one[1] and two[0] < two[1]:
        return 1
    return 0

def check_correct_score(score: List[int]) -> bool:
    if (len(score) == 2 and score[0].isdigit() and score[1].isdigit() and int(score[0]) >= 0 and int(
            score[1]) >= 0):
        return True
    return False
