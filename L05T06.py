my_dict = {}
digits = '1234567890'

with open('text_6.txt', 'r', encoding='utf-8') as my_file:
    # result = my_file.read()
    # print(result)

    for line in my_file:
        subject, hours = line.split(":")
        my_dict[subject] = sum(map(int, ''. join([num for num in hours if num in digits]).split()))
    print(my_dict)
