#Задача 26: Напишите программу, которая на вход принимает
#два числа A и B, и возводит число А в целую степень B с
#помощью рекурсии.
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
def grade(a, b):
    if b in [1]:
        return a
    else:
        return (a * grade(a, b - 1))    
print(f'Результат возведения в степень равен: {grade(a, b)}')