# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

total_salary = 0
try:
    with open('text_3.txt', 'r', encoding='utf-8') as file:
        print('Employees with salary less than 20,000:')
        for i, line in enumerate(file):
            employee = line.split()
            salary = float(employee[1])
            total_salary += salary
            if float(salary) < 20000:
                print(employee[0])

    print(f'Average salary: {total_salary / (i + 1)}')
except IOError:
    print('File not found!')
