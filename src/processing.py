def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция выводит список словарей, у которых ключ 'state' соответствует заданному значению"""

    new_list_dict = []
    for item_list in list_dict:
        if item_list["state"] == state:
            new_list_dict.append(item_list)
    return new_list_dict


def sort_by_date(list_dict: list, sort: bool = True) -> list:
    """Функция возвращвет список отсортированный по дате"""

    sorted_list_dict = sorted(list_dict, key=lambda i: i["date"], reverse=sort)
    return sorted_list_dict
