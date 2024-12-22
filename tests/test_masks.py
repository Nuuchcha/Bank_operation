import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: str) -> None:
    """Функция проверки москировки номера карты при передаче корректных данных"""

    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_empty() -> None:
    """Функция проверки москировки номера карты при передаче пустых данных"""

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Номер карты не введен"


def test_get_mask_card_number_error(card_number_error: str) -> None:
    """Функция проверки москировки номера карты при передаче не корректных данных"""

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number_error)
    assert str(exc_info.value) == "Не верно введен номер карты"


def test_get_mask_account(account_number: str) -> None:
    """Функция проверки москировки номера счета при передаче корректных данных"""

    assert get_mask_account(account_number) == "**4305"


def test_get_mask_account_empty() -> None:
    """Функция проверки москировки номера счета при передаче пустых данных"""

    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Номер счета не введен"


def test_get_mask_card_account_error(account_number_error: str) -> None:
    """Функция проверки москировки номера счета при передаче не корректных данных"""

    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number_error)
    assert str(exc_info.value) == "Не верно введен номер счета"
