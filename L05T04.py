rus_dic = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}

with open('text__4.txt', 'w', encoding='utf-8') as rus_dictionary:
    with open('text_4.txt', 'r', encoding='utf-8') as eng_dictionary:
        rus_dictionary.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in eng_dictionary])



        # rus_dictionary = replace for key in eng_dictionary}
        # print('new dictionary' + str(rus_dictionary))
        # rus_dictionary.writelines = {key: line.replace(key, rus_dictionary[key]) for key in eng_dictionary}

    # print(content)
    # new_dic = {line.split()[0]: line.split()[1] for word in eng_dic}


