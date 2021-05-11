def personal_info(name, last_name, phone, email):
    """
    собирает введенные пользователем данные и выводит их в строчку
    """
    print(name, last_name, phone, email)
personal_info(name = input('Введите ваше имя: '), last_name=input('Введите вашу фамилию: '), phone=input('укажите ваш телефон: '), email=input('укажите ваш email '))