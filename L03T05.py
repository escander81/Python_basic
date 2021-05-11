def my_func():
    """
    после ввода чисел через пробел выводит их сумму.
    буквы не принимаются при расчете
    """
    result = 0
    while True:
        a = input('Введите числа через пробел. для выхода из программы нажать "q": ').split()
        for x in a:
            if x == 'q':
                return result
            else:
                try:
                    result += int(x)
                except ValueError:
                    print('Error! это не число. введите числа через пробел, для выхода из программы нажмите "q"')
        print(f"промежуточный итог = {result}")
print(my_func())