# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)
list1 = []
for i in range(len(list) - 1):
    if list[i] % 1 == 0:
        del list[i]
for i in range(len(list)):
    result = round(list[i] % 1, 2)
    list1.append(result)
print(list1)

max_num = max(list1)
print(f'Максимальное значение дробной части числа:', max_num)
min_num = min(list1)
print(f'Минимальное значение дробной части числа:', min_num)

result1 = max_num - min_num
print(f'Разница между мин и мах значением: ', result1)