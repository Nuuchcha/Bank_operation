from src.widget import mask_account_card

user_cart_number = input("Введите название и номер карты через пробел: ")
print(mask_account_card(user_cart_number))

user_account_number = input("Введите слово 'Счет' и номер счета через пробел: ")
print(mask_account_card(user_account_number))
