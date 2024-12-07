from src.masks import get_mask_account, get_mask_card_number

user_cart_number = input("Введите номер карты без пробелов: ")
print(get_mask_card_number(user_cart_number))

user_account_number = input("Введите номер счета: ")
print(get_mask_account(user_account_number))
