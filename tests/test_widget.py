import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('card_data, expected',
                         [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                          ('Счет 64686473678894779589', 'Счет **9589'),
                          ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                          ('Счет 35383033474447895560', 'Счет **5560'),
                          ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                          ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                          ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                          ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(card_data, expected):
    assert mask_account_card(card_data) == expected


def test_mask_account_card_empty():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card('')
    assert str(exc_info.value) == 'Данные не введены'


def test_mask_account_card_only_number(card_number):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_number)
    assert str(exc_info.value) == 'Не указано слово "Счет", либо имя карты'


def test_mask_account_card_under_number(name_card):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(name_card)
    assert str(exc_info.value) == 'Номер карты не введен'


def test_get_date(date_not_formated):
    assert get_date(date_not_formated) == '11.03.2024'


def test_get_date_error(date_not_formated_error):
    with pytest.raises(ValueError) as exc_info:
        get_date(date_not_formated_error)
    assert str(exc_info.value) == 'Введен не верный формат даты'
