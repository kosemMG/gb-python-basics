# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка.

from functools import reduce

num_list = [number for number in range(100, 1001, 2)]

result = reduce(lambda a, b: a * b, num_list)

print(f'The list: {num_list}\nThe product of all the list numbers: {result}')
