# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
#Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def decimal_to_binary(n):
    
    base = int(2)
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= base
    print(result)

decimal_to_binary(45)
