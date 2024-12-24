import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_data: str, expected: str) -> None:
    """Функция проверки вывода номера счета с указанием 'Счет',
    либо номера карты с указанием имени карты и маскировкой номера счета
    или номера карты при вводе корректных данных"""

    assert mask_account_card(card_data) == expected


def test_mask_account_card_empty() -> None:
    """Функция проверки вывода номера счета с указанием 'Счет',
    либо номера карты с указанием имени карты и маскировкой номера счета
    или номера карты при вводе пустых данных"""

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
    assert str(exc_info.value) == "Данные не введены"


def test_mask_account_card_only_number(card_number: str) -> None:
    """Функция проверки вывода номера счета с указанием 'Счет',
    либо номера карты с указанием имени карты и маскировкой номера счета
    или номера карты при вводе только номера карты или счета"""

    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_number)
    assert str(exc_info.value) == 'Не указано слово "Счет", либо имя карты'


def test_mask_account_card_under_number(name_card: str) -> None:
    """Функция проверки вывода номера счета с указанием 'Счет',
    либо номера карты с указанием имени карты и маскировкой номера счета
    или номера карты при вводе только имени карты или слова 'Счет'"""

    with pytest.raises(ValueError) as exc_info:
        mask_account_card(name_card)
    assert str(exc_info.value) == "Номер карты не введен"


def test_get_date(date_not_formated: str) -> None:
    """Функция проверки получения корректной даты из передаваемых корректных данных"""

    assert get_date(date_not_formated) == "11.03.2024"


def test_get_date_error(date_not_formated_error: str) -> None:
    """Функция проверки получения корректной даты из передаваемых не корректных данных"""

    with pytest.raises(ValueError) as exc_info:
        get_date(date_not_formated_error)
    assert str(exc_info.value) == "Введен не верный формат даты"
