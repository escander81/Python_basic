with open("text_3.txt", 'r', encoding="utf8") as some_file:
    process = some_file.readlines()
    for index, value in enumerate(process, 1):
        words = len(value.split())
        print(f' строка {index} содержит {words} слов')




# with open("text_2.txt", 'w', encoding="utf8") as some_file:
#     for line in iter(input, ""):
#         print(f'Введена строка: {line}', 'в ней символов: ', len(line))
#         some_file.write(f"{line}\n")