from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Функция принимает тип и номер карты или счета и маскирует номер"""

    user_card_mask = ''
    if 'Счет' in user_card.title():
        number_account = user_card[-20:]
        user_card_mask = user_card[:-20] + get_mask_account(number_account)
    else:
        number_kard = user_card[-16:]
        user_card_mask = user_card[:-16] + get_mask_card_number(number_kard)
    return user_card_mask
