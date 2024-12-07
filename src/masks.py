from typing import Union


def get_mask_card_number(number_kart: Union[int | str]) -> str:
    """Функция маскировки номера банковской карты"""

    number_kart_str = str(number_kart)
    if not number_kart_str.isdigit() or len(number_kart_str) != 16:
        return "Не верно введен номер карты"
    else:
        return f"{number_kart_str[:4]} {number_kart_str[4:6]}** ****{number_kart_str[-4:]}"


def get_mask_account(account_number: Union[int | str]) -> str:
    """Функция маскировки номера банковского счета"""

    account_number_str = str(account_number)
    if not account_number_str.isdigit() or len(account_number_str) != 20:
        return "Не верно введен номер счета"
    else:
        return f"**{account_number_str[-4:]}"
