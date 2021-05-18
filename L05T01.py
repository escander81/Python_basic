with open("text_1.txt", 'w', encoding="utf8") as some_file:
    for line in iter(input, ""):
        print(f'Введена строка: {line}')
# print(line, file = some_file)
        some_file.write(f"{line}\n")

# try:
#     with open("test.txt", encoding="utf8") as file_handler:
#         for line in file_handler:
#             print(line)
# except IOError:
#     print("An IOError has occurred!")

# first_file = open('text_1.txt', 'w')
#
# def text_input():
#     while True:
#         try:
#             yield input()
#         except IOError:
#             break
#
# print(text_input(), file=text_1.txt)
# # first_file.writelines(text_list)
# first_file.close()
