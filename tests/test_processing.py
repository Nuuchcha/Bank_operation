from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_execute(list_dict: list) -> None:
    """Функция проверки фильтрации словарей по значению 'EXECUTED'"""

    assert filter_by_state(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(list_dict: list) -> None:
    """Функция проверки фильтрации словарей по значению 'CANCELED'"""

    assert filter_by_state(list_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_empty(list_dict: list) -> None:
    """Функция проверки фильтрации по не существующему значению"""

    assert filter_by_state(list_dict, "EMPTY") == []


def test_sort_by_date_decreasing(list_dict: list) -> None:
    """Функция проверки сортировки словарей по убыванию значения даты"""

    assert sort_by_date(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_increase(list_dict: list) -> None:
    """Функция проверки сортировки словарей по возрастанию значения даты"""

    assert sort_by_date(list_dict, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
