﻿def get_upper_string(value):
    """Функция переводит строку в верхний регистр"""
    if type(value) == str:
        return value.upper()
    else:
        print("Предусмотрен ввод значений типа string")
