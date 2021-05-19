import json
with open('text_77.json', 'w', encoding='utf-8') as write_f:
    with open('text_7.txt', encoding='utf-8') as f_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        cost = [profit,{'average profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                        len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(cost, write_f, ensure_ascii=False, indent = 4)




        # for line in my_file:
        #     company, income, costs = line.split(" ")
        #     my_file(a) =
        #     if line
        # f_dict =
        # s_dict =