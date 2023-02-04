#Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
from math import pow
N = int(input('Введите число N: '))
listNum = []
sq = int(0)
k = int(1)
while sq <= N:
    sq = pow(2, k)
    listNum.append(int(sq))
    k += 1
print(f'Вот все степени двойки, не превосходящие числа N: {listNum[0:len(listNum)-1]}')

