with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    # content = my_file.read()
    # print(content)
    info = {line.split()[0]: float(line.split()[1]) for line in my_file}
    print(f"average salary = {round(sum(info.values()) / len(info), 3)}\n"
          f"employees with small salary {[x[0] for x in info.items() if x[1] < 20000]}")