# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [2, 4, 5, 3, 7, 8, 10]
if len(list) % 2 == 0:
    list1 = len(list) / 2
    a = len(list) - 1
    while a >= list1: 
        for i in range(len(list)):
            multipl = list[i] * list[a]
            a = a - 1
            if i >= list1:
                break
            print(multipl, end=' ')
if len(list) % 2 != 0:
    list1 = int(len(list) / 2) 
    a = len(list) - 1
    while a > list1:
        for i in range(len(list)):
            multipl = list[i] * list[a]
            a = a - 1
            if i >= list1:
                break
            print(multipl, end=' ')

    
