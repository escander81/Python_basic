def divider():
    """
    принимает два числа и выполняет их деление
    """
    s_1 = float(input('Enter dividend: '))
    s_2 = float(input('Enter divisor: '))

    if s_2 == 0:
        print(f"U can't divide by ZERO")
        return
    else:

        print(f"Your result is: {s_1 // s_2}")
divider()

# решение через Try/Except как-то не получилось. не смог обойти ноль
# def divider():
#     try:
#         s_1 = float(input('Enter dividend: '))
#         s_2 = float(input('Enter divisor: '))
#     except Exception as err:
#         return err
#     except ZeroDivisionError:
#         print(f"U can't divide by ZERO")
#     print(f"Your result is: {s_1 // s_2}")
# divider()
#
#





# def my_f(s_1, s_2):
#     if s_2 == 0:
#         return f"U cant divide by ZERO"
#     else:
#         sub = s_1 // s_2
#         print(f"Your result is: {sub}")
#
# my_f(s_1=int(input('Enter dividend: ')), s_2 = int(input('Enter divisor: ')))





# my_f(s_2 = int(input('Enter dividend: ')), input(s_1 = int(input('Enter divisor: '))))
# if s_2:
        #     s_2 ==0
        #     return f"U can't devide by ZERO"
    # pass
# s_1 = int(input('Enter dividend: '))
# s_2 = int(input('Enter divisor: '))

# =======
# def my_f(s_1, s_2):
#     sub = s_1 // s_2
#     if s_2 == 0:
#         return f"U can't devide by ZERO"
#     else:
#         print(f"Your result is: {sub}")
#
# my_f(s_1=int(input('Enter dividend: ')), s_2 = int(input('Enter divisor: ')))



