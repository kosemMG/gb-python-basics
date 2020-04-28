# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class DivisionByZeroError(Exception):
    def __init__(self, message: str):
        self.txt = message


try:
    denominator = int(input('Enter the denominator: '))
    if denominator == 0:
        raise DivisionByZeroError('Division by zero!')
except ValueError:
    print('Invalid input!')
except DivisionByZeroError as err:
    print(err)
else:
    inverse_number = 1 / denominator
    print(inverse_number)
