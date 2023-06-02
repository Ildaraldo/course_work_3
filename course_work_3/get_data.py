import json
import os


def read_local_json(file_name):
    """Функция считывающий параметры из файла JSON"""

    # проверяем, существует ли такой файл
    if not os.path.exists(file_name):
        print(f"Отсутствует файл '{file_name}'")
        # exit(0)
        return []

    # открываем файл
    with open(file_name) as file:
        # возвращаем список параметров из файла
        return [item for item in json.load(file)]

