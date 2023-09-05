def decorator(func):
    def wrapper_decorator():
        # Запрашиваем у пользователя логин
        user_login = input("Введите логин: ")

        # Проверяем, является ли пользователь админом
        if user_login == "admin":
            # Если пользователь - админ, выполняем функцию и выводим сумму на счете
            return func()
        else:
            # Если пользователь не админ, выводим сообщение о запрете доступа
            return "Доступ запрещен!"

    return wrapper_decorator

# Функция, которая выводит сумму на счете
def get_account_balance():
    return 50000

# Декорируем функцию
get_account_balance = decorator(get_account_balance)

result = get_account_balance()
print(result)
