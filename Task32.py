# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

import random
mylist = [random.randint(-10, 10) for _ in range(int(input('Введите размер списка: ')))]
print(mylist)
final_list = []
min_num = int(input('Введите минимальное число: '))
max_num = int(input('Введите максимальное число: '))
for i in range(len(mylist)):
    if min_num <= mylist[i] <= max_num:
        final_list.append(i)
print(final_list)