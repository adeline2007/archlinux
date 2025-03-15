import subprocess
import os
from random import randint, choice
import time

# https://copypastas.ru/image/   website where you can do ascii art


def make_random_text():
    # Здесь можно в список добавлять текст и он случайно будет выбираться при запуске
    list_text = [
        "Crede firmiter et pecca fortiter )",
        "Хорошего дня тебе солнце!)",
        "Мучений с проектом!",
        "C++ and Python in my heart )",
        "Не бойся одиночества. Ты всегда один",
        "Ебануться, это Arch linux!!!",
        "Точно кодить хочешь? Может в кс?)"
    ]
    return list_text[randint(0, len(list_text)-1)]
    #return list_text[6]

# Сюда можно добавлять иконки разные, тоже будут случайно запускаться
lambda_icons = ['''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀#######⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀#######⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙####⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹####⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈#####⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾######⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾#######⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰#####⢻####⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴####⡿⠁⠀⢿####⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾####⠟⠀⠀⠀⠈#####⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠#####⠋⠀⠀⠀⠀⠀⠘####⣷⡀⠀⠀⠀⡀⠀⠀
⠀⠀⠀⠀⣰####⡿⠃⠀⠀⠀⠀⠀⠀⠀⠹####⣷⣶##⣷⠀⠀
⠀⠀⠀⣼####⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻########⡆⠀
⠀⠀⠚⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿#⡿⠿⠛⠋⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀\n''',
'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣴⣶⣶⣦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⠟⠛⠉⠁⠀⠀⠀⠀⠈⠈⠛⠿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⢀⣾⣿⣿⡿⠋⠁⠀⠐⣶⣶⣶⣶⣆⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⡀⠀⠀
⠀⠀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠿⠿⢿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⡄⠀
⠀⣼⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⡂⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣧⠀
⠠⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀
⠠⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡿⢻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇
⠐⣿⣿⣿⠀⠀⠀⠀⠀⠀⣸⣿⣿⡟⠀⠈⣿⣿⣿⡦⠀⠀⠀⠀⠀⢀⣿⣿⣿⠁
⠀⢿⣿⣿⣇⠀⠀⠀⢀⣾⣿⣿⠏⠀⠀⠀⠈⣿⣿⣿⣤⣴⣆⠀⠀⣼⣿⣿⡟⠀
⠀⠐⢿⣿⣿⣦⠀⢠⣾⣿⣿⠇⠀⠀⠀⠀⠀⠘⣿⣿⣿⡿⠿⠀⣴⣿⣿⡿⠁⠀
⠀⠀⠈⢻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠁⢀⣠⣾⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣶⣄⣀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠟⠟⠿⠿⠻⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
                             \n''']



# Вот эти названия тоже можно менять
img_directory = '/home/adeline/Documents_my/img/wallpaper'
hyprpaper_config = '/home/adeline/.config/hypr/hyprpaper.conf'



#---------------- don't change please) --------------


# Работа с hyprpaper и меняем обои

def get_random_image(directory):
    # Просматриваем фотографии которые есть и выбираем случайную фотку
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif','.PNG')): # Поддерживаемые форматы
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                image_files.append(filepath)

    if not image_files:
        return None

    random_image = choice(image_files)
    return random_image


def create_hyprpaper_config(image_path, config_path):
    config = f"""
    preload = {image_path}
    wallpaper = ,{image_path}
    """
    
    with open(config_path, 'w') as f:
        f.write(config)


# img_directory = '/home/adeline/Documents_my/img/wallpaper'
# hyprpaper_config = '/home/adeline/.config/hypr/hyprpaper.conf'

random_img = get_random_image(img_directory)
create_hyprpaper_config(random_img, hyprpaper_config)



# Оранжевый цвет
orange_color = "\033[38;5;214m"  # ANSI код для оранжевого цвета
reset_color = "\033[0m"  # Сброс цвета

lambda_icon = lambda_icons[randint(0, len(lambda_icons)-1)]
dop_text = dop_text = "\033[1;36m\033[3m" + make_random_text() + "\033[0m\n\n"

time.sleep(6)

subprocess.run(["kitty", "-e", "fish", "-c", f"cd ~; echo '{orange_color}{lambda_icon}{reset_color}{dop_text}'; exec fish"])
#               терминал        фиш   открываем началью директорию,       _текст_                           оставляем открытым
