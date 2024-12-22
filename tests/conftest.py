import pytest


@pytest.fixture
def card_number():
    return '7000792289606361'


@pytest.fixture
def card_number_error():
    return '-000792289606361'


@pytest.fixture
def account_number():
    return '73654108430135874305'


@pytest.fixture
def account_number_error():
    return '-3654108430135874305'


@pytest.fixture
def name_card():
    return 'Visa Classic'


@pytest.fixture
def date_not_formated():
    return '2024-03-11T02:26:18.671407'


@pytest.fixture
def date_not_formated_error():
    return '24-03-11T02:26:18.671407'


@pytest.fixture
def list_dict():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
