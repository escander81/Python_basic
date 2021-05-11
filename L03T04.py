# первое решение с оператором **
def my_func(x, y):
    """
    возвозит Х в отрицательную степерь У
    """
    if x <= 0:
        print('число X должно быть больше нуля')
        return
    else:
        print(1 / x ** y)
    x = abs(x)
    y = int(y)


my_func(int(input('введите x: ')),
        int(input('введите y: ')))

# второе решение без оператора ** через цикл
def my_func(x, y):
    i = 0
    result = 1
    while i < y:
        result *= x
        i += 1
        if x < 0:

            print("x должен быть больше 0")
            return
    print(1 / result)
#
#
# my_func(int(input('введите x: ')),
#         int(input('введите y: ')))


# решение с тернарным оператором не хочет работать
# def my_func(x, y):
#     print(1 / x ** y)
#     return x if x > 0 else -x
#     # x = abs(x)
#     # y = int(y)
#
# my_func(int(input('введите x: ')),
#         int(input('введите y: ')))

# def my_func(x, y):
#     result = 1
#     i = 1
#     while i < y:
#         result = i * x
#         i += 1
#
#         return x if x > 0 else -x
#         print(1 / result)
#
# my_func(int(input('введите x: ')),
#         int(input('введите y: ')))