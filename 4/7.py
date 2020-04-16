# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.

from itertools import count, islice
from math import factorial


def fact():
    for element in count(1):
        yield factorial(element)


last_number = int(input('Enter the last number to calculate factorial: '))
for el in islice(fact(), last_number):
    print(el)
