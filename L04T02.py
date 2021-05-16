condition_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list = [condition_list[num] for num in range(1, len(condition_list)) if condition_list[num] > condition_list[num - 1]]
print(condition_list)
print(my_list)