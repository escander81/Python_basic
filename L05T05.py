from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as my_file:
    my_file.write(' '.join([str(randint(1, 100)) for _ in range (1000)]))
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))

    # sum = 0
    # a = input('введите цифры через пробел: ')
    # b = {x for x in a if x not in ''}
    # sum = str(b).sum (int(b))
    # print(sum)
    # sum(map(int, my_file.readlines().split()))