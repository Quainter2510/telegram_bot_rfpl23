from PIL import Image, ImageDraw, ImageFont
from config_data import config


def main_table(table, tour):
    img = Image.open("images/table_templates/template_main_table.png")
    imdraw = ImageDraw.Draw(img)
    dx = [66, 426, 495, 564, 633, 702, 771, 840, 909, 978, 1047, 1117, 1186, 1255, 1323]
    start_y = 78  # Начало таблицы по y без шапки
    dy = 44  # Разница между строками по y
    font = ImageFont.truetype("images/Fonts/consolas.ttf", size=28)
    for i in range(config.NUMBER_OF_PLAYERS):
        for j in range(len(table[0])):
            if j < tour or j == len(table[0]) - 1:
                msg = str(table[i][j]) 
            else:
                msg = "-"
            _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
            imdraw.text((dx[j] + (dx[j + 1] - dx[j] - w) // 2, start_y + dy * i + (dy - h) // 2), msg, font=font)
    img.save("images/ready_tables/main_table.png")


def result_tour(res, tour, points, nickname=""):
    img = Image.open("images/table_templates/template_result_tour.png")
    imdraw = ImageDraw.Draw(img)
    dx = [0, 683, 941, 1179, 1323]
    dy = 68  # Разница между строками по y
    width = 1323  # ширина таблицы
    result_start_x = 1179  # начало окна итога очков по х
    result_start_y = 676  # начало окна итога очков по у
    result_finish_x = 1323  # конец окна итога очков по х

    if nickname == "":
        font = ImageFont.truetype("images/Fonts/consolas.ttf", size=54)
        msg = f'Итог {tour}'
    else:
        font = ImageFont.truetype("images/Fonts/consolas.ttf", size=42)
        msg = f'Прогноз {tour} от {nickname}'
    _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
    imdraw.text(((width - w) // 2, (dy - h) // 2), msg, font=font, fill=(255, 255, 255), stroke_width=1)
    msg = f'{points}'
    font = ImageFont.truetype("images/Fonts/BRITANIC.TTF", size=52)
    _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
    imdraw.text((result_start_x + (result_finish_x - result_start_x - w) // 2, result_start_y + (dy - h) // 2), msg, font=font)
    font = ImageFont.truetype("images/Fonts/consolas.ttf", size=40)
    for i in range(config.COUNT_MATCHES_IN_TOUR):
        for j in range(4):
            msg = str(res[i][j])
            _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
            imdraw.text((dx[j] + (dx[j + 1] - dx[j] - w) // 2, dy * 2 + dy * i + (dy - h) // 2), msg,
                        font=font)
    img.save("images/ready_tables/result_tour.png")


def points_tour(data, tour):
    img = Image.open("images/table_templates/template_points_tour.png")
    imdraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("images/Fonts/consolas.ttf", size=50)
    dx = [187, 1127, 1323]
    dy = 47  # Разница между строками по y
    font = ImageFont.truetype("images/Fonts/consolas.ttf", size=30)
    for i in range(config.NUMBER_OF_PLAYERS):
        for j in range(2):
            msg = str(data[i][j])
            _, _, w, h = imdraw.textbbox((0, 0), msg, font=font)
            imdraw.text((dx[j] + (dx[j + 1] - dx[j] - w) // 2, dy + dy * i + (dy - h) // 2), msg,
                        font=font)
    img.save("images/ready_tables/points_tour.png")