#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
#школьница. Петя помогает Кате по математике. Он задумывает два
#натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
#этого Петя делает две подсказки. Он называет сумму этих чисел S и их
#произведение P. Помогите Кате отгадать задуманные Петей числа.
from math import sqrt

S = int(input('Введите сумму угадываемых чисел: '))
P = -int(input('Введите произведение угадываемых чисел: '))
D = S*S + 4*P
if D > 0:
    sq = sqrt(D)/2
    p = S/2
    x1 = p-sq
    x2 = p+sq
    print(f'Первое из загаданных чисел: {x1}')
    print(f'Второе загаданное число: {x2}')
else: 
    breakpoint