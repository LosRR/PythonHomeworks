#Задача 16: Требуется вычислить, сколько раз встречается некоторое
#число X в массиве A[1..N]. Пользователь в первой строке вводит
#натуральное число N – количество элементов в массиве. В последующих
#строках записаны N целых чисел Ai
#. Последняя строка содержит число X
n = int(input('Введите количество элементов в массиве: '))
A = []
X = int(input('Введите X (число, встречаемость которого в массиве мы вычисляем): '))
for i in range(n):
    A.append(i+1)
print(f' Вот наш массив: {A}')
if (A.count(X)) >= 1:
    print(f' Число X встречается в массиве: {A.count(X)} раз')
else:
    print(' Число X не встречается в данном массиве')
