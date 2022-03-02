# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
import os


def show_stat(folder_path):
    stat = get_stat(folder_path)
    keys = list(stat)
    keys.sort()
    for key in keys:
        print(f'{key}: {stat[key]}')  # в этой строке была ошибка, stat(key) было взято в круглые скобки


def get_stat(folder_path):
    stat = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            key = get_key(size)
            if key not in stat:
                stat[key] = 0
            stat[key] += 1
    if not stat:
        raise Exception('There are no files in the directory!')
    return stat


def get_key(size):
    num_digits = 1
    while True:
        if size // 10:
            num_digits += 1
        else:
            break
        size //= 10
    return 10 ** num_digits


if __name__ == '__main__':
    try:
        my_folder_path = './'
        show_stat(my_folder_path)
    except Exception as e:
        print(e)
