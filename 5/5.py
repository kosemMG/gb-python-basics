# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import random


def create_number_list(number: int):
    return [round(random() * 2000 - 1000, 2) for i in range(number)]


with open('text_5.txt', 'r+') as file:
    num_list = create_number_list(int(input('Amount of numbers: ')))
    for num in num_list:
        print(str(num), file=file, end=' ')
    file.seek(0)
    content = file.read()
    num_sum = sum(map(float, content.split()))

print(f'Total sum: {num_sum}')
