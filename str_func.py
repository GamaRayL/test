def get_upper_string(value):
    if type(value) == str:
        return value.upper()
    else:
        print("Предусмотрен ввод значений типа string")


def get_capital_first_letter(value):
    """Функция возвращает строку с первой заглавной буквой и остальными в нижнем регистре"""
    if type(value) == str:
        return print(value[0].upper() + value[1::].lower())
    else:
        print("Предусмотрен ввод значений типа string")


get_capital_first_letter("брр")
