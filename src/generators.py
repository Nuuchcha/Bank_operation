from typing import Any, Generator


def filter_by_currency(
    list_dicts: list[dict[str, Any]], currency_type: str
) -> Generator[str | dict[str, Any] | None, str, None]:
    """Функция принимает список словарей с транзакциями и возвращает итератор,
    выдающий поочередно транзакции, соответствующие заданной валюте
    """

    filter_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_type, list_dicts))

    if list_dicts == []:
        yield "Пустой список"
    else:
        for item in filter_transactions:
            if filter_transactions is not None:
                yield item
        if filter_transactions == []:
            yield f"Нет операций в валюте '{currency_type}'"


def transactions_descriptions(list_dicts: list[dict[str, Any]]) -> Generator[str | dict[str, Any] | None, str, None]:
    """Функция принимает список словарей с транзакциями и возвращает итератор,
    выдающий описание каждой операции по очереди
    """

    if list_dicts == []:
        yield "Пустой список"
    else:
        list_descriptions = list(
            item_list_dicts["description"]
            for item_list_dicts in list_dicts
            if item_list_dicts.get("description") is not None
        )

        if list_descriptions != []:
            for item in list_descriptions:
                yield item
        else:
            yield "Отсутствуют данные о проведенных операциях"


def card_number_generator(start: int = 1, stop: int = 1) -> Generator[str | dict[str, Any] | None, str, None]:
    """Функция генерирует номера банковских карт в заданном диапазоне
    в формате 'ХХХХ ХХХХ ХХХХ ХХХХ'
    """

    num = 10000000000000000

    if type(start) is int and type(stop) is int:
        if 10000000000000000 > start > 0 and 10000000000000000 > stop > 0:
            if stop == 9999999999999999 or start == 9999999999999999:
                yield "!!!Доcтигнуто предельное значение номера карты - '9999 9999 9999 9999'!!!"
            elif start > stop:
                cards_numbers = (str((num + item)).lstrip("1") for item in range(stop, start + 1))
                for number in cards_numbers:
                    yield f"{str(number[:4])} {str(number[4:8])} {str(number[8:12])} {str(number[12:])}"
            elif stop > start:
                cards_numbers = (str((num + item)).lstrip("1") for item in range(start, stop + 1))
                for number in cards_numbers:
                    yield f"{str(number[:4])} {str(number[4:8])} {str(number[8:12])} {str(number[12:])}"
        else:
            yield "Номер карты не может быть меньше или равным '0' и не должен превышать '9999 9999 9999 9999'"
    else:
        yield "Ошибка: некорректный ввод"
