# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 129, 55, 62, 299, 18]
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(new_list)
