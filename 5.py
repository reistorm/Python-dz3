# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Введите число: "))
numbers = []
for e in range(1, n+1):
    numbers.append(fib(e))
print(numbers)

