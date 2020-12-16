# -----------------------------------------------------------------------------
#  Программная инженерия
#  Лабораторная 4 от 15.12.2020
#
#  Задание 1. Пусть дана некоторая директория (папка). Посчитайте количество
#  файлов в данной директории (папке) и выведите на экран
# -----------------------------------------------------------------------------

import os

def get_files_count(p: str) -> int:
    return len(os.listdir(p))

path = r'C:\Users\HP\Desktop\test'
files_count = get_files_count(path)

print(files_count)

