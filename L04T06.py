from itertools import count, cycle
start = int(input(f"введите стартовое целое число: "))
max = int(input('сколько повторений? '))

for el in count(start):
    if el > max:
        break
    else:
        print(el)

c = 0
max_c = int(input('какое максимальное количество повторений? '))
my_cycle = cycle("ABC")

for el in range(max_c):

    print("(my_cycle) = ({})".format(next(my_cycle)))






