def my_func(i_1, i_2, i_3):
    """
    находит два максмальных введенных значения и выводит их сумму
    """
    sum=0
    if i_1 < i_2:
         sum = i_2+i_3
    elif i_1 > i_3:
        sum = i_1 + i_2
    else:
        sum = i_2 + i_1
    print(sum)
my_func(i_1 = int(input('enter first integer: ')),
        i_2 = int(input('enter second integer: ')),
        i_3 = int(input('enter third integer: ')))
