#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
#повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
first = []
second = []
print('Введите последовательно числа первого множества: ')
for i in range(n):
    addfirst = int(input())
    first.append(addfirst)
print(f'Вот первое множество: {first}')
print('Введите последовательно числа второго множества: ')
for i in range(m):
    addsecond = int(input())
    second.append(addsecond)
print(f'Вот второе множество: {second}')
first = set(first)
second = set(second)
final = first.intersection(second)
final = list(final)
def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr
selection_sort(final)
print(f'Числа из обоих множеств в порядке возрастания: {final}')