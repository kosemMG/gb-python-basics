# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.


def calculate_hours(arr: list):
    hr_sum = 0
    for item in arr:
        if '(' in item:
            hr_sum += int(item.split('(')[0])
    return hr_sum


subjects = {}

try:
    with open('text_6.txt', 'r') as file:
        for line in file:
            subject_line = line.split(':')
            subjects[subject_line[0]] = calculate_hours(subject_line[1].split())

    print(subjects)
except IOError:
    print('File not found!')
