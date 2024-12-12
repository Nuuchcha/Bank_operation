from typing import Any, Dict, List


def filter_by_state(list_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и опционально значение для ключа 'state' (по умолчанию 'EXECUTED'),
    и возвращает новый список словарей, содержащий только те словари, у которых ключ 'state' соответствует
    указанному значению
    """

    new_list_dict = []
    for item_list in list_dict:
        if item_list["state"] == state:
            new_list_dict.append(item_list)
    return new_list_dict


def sort_by_date(list_dict: List[Dict[str, Any]], sort: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате
    """

    sorted_list_dict = sorted(list_dict, key=lambda i: i["date"], reverse=sort)
    return sorted_list_dict
