from typing import Union


def get_mask_card_number(number_kard: Union[int | str]) -> str:
    """Функция маскировки номера банковской карты"""

    number_kard_str = str(number_kard)
    if number_kard_str == '':
        raise ValueError("Номер карты не введен")

    if not number_kard_str.isdigit() or len(number_kard_str) != 16:
        raise ValueError("Не верно введен номер карты")
    else:
        new_card_number = ''
        for index in range(len(number_kard_str)):
            if index % 4 == 0 and index != 0:
                new_card_number += ' '
            if 0 <= index <= 5 or (len(number_kard_str) - 4) <= index <= (len(number_kard_str) - 1):
                new_card_number += number_kard_str[index]
            else:
                new_card_number += '*'
        return new_card_number


def get_mask_account(account_number: Union[int | str]) -> str:
    """Функция маскировки номера банковского счета"""

    account_number_str = str(account_number)
    if account_number_str == '':
        raise ValueError("Номер счета не введен")

    if not account_number_str.isdigit() or len(account_number_str) != 20:
        raise ValueError("Не верно введен номер счета")
    else:
        return f"**{account_number_str[-4:]}"
