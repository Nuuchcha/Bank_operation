import re
from calendar import month

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card_account_number: str) -> str:
    """Функция принимает тип и номер карты или счета и маскирует номер"""

    name_card = ''
    number_card = ''
    if len(user_card_account_number) > 0:
        for el in user_card_account_number:
            if el.isalpha() is True or el == ' ':
                name_card += el
            else:
                number_card += el
    else:
        raise ValueError('Данные не введены')

    if name_card == '':
        raise ValueError('Не указано слово "Счет", либо имя карты')
    else:
        if "Счет" in name_card:
            mask_account = get_mask_account(number_card)
            return name_card + mask_account
        else:
            mask_card = get_mask_card_number(number_card)
        return name_card + mask_card


def get_date(date_not_formatted: str) -> str:
    """Функция возвращает дату в читаемом виде ДД.ММ.ГГГГ"""

    slice_date = date_not_formatted[:10]
    date_str = ''
    for el in slice_date:
        if el.isdigit():
            date_str += el
    if len(date_str) != 8:
        raise ValueError('Введен не верный формат даты')
    else:
        return date_str[6:] + "." + date_str[4:6] + "." + date_str[:4]

