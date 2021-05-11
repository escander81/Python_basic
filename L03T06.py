# попробовал реализовать постоянный набор слов с окончанием программы при вводе 'q', но так и не добился результата.
# так же я не смог выдать результат в строчку...
def int_func(new_txt):
    """
    принимает прописные латинские буквы (слова) и выводит их с заглавными. кириллицу не выводит
    test: nice авп ъghj jапро hjjпаро вапрghgh cool
    """
    correct = 'abcdefghijklmnopqrstuvwxyz'
    return new_txt.title() if not set(new_txt).difference(correct) else False

while True:
    txt = input('введите слово строчной латиницей: ').split()
    for t in txt:
        if t == 'q':
               False
    for t in txt:
        output = int_func(t)
        if output:
            print(int_func(t))





    # for letter in letters:
    #     if letter in correct:
    #         letter +=1
    # print()
    #
    # for x in txt:
    #     if txt.get('x'):
    #         new.txt.title()
    #     else:
    #         return

    # while True:
    #     txt = input('введите текст: ')
    #     for x in txt:
    #         if x == 'q':
    #             return new_txt
    #     else:
    #
    #         for t in txt:
    #
    #             if t in correct:
    #                 new_txt.title()
    #         else:
    #             return

# print(int_func())

#
# pring(int_func("text"))
#nice авп ъghj jапро hjjпаро вапрghgh cool
# s.title()
# ASCII 97-122
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'