# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def calculate_salary():
    try:
        hours, payment_per_hour, prize = map(int, argv[1:])
    except ValueError:
        return f'The input is invalid.'
    return f'The salary is {hours * payment_per_hour + prize}'


print(calculate_salary())
