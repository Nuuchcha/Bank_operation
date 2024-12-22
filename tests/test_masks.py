import pytest

from src.masks import get_mask_card_number, get_mask_account
from tests.conftest import card_number_error


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('')
    assert str(exc_info.value) == "Номер карты не введен"


def test_get_mask_card_number_error(card_number_error):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number_error)
    assert str(exc_info.value) == 'Не верно введен номер карты'


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == '**4305'


def test_get_mask_account_empty():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account('')
    assert str(exc_info.value) == "Номер счета не введен"


def test_get_mask_card_account_error(account_number_error):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number_error)
    assert str(exc_info.value) == 'Не верно введен номер счета'
