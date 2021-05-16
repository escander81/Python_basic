#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24

from math import factorial
from itertools import count

def factorial_generator():
    for el in count(1):
        yield factorial(el)

n = 0
for i in factorial_generator():
    if n == 10:
        break
    else:
        n +=1
        print(f"factorial {n} = {i}")