# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv(
# )).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не
# целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого
# числа.

from math import floor


class Cell:
    def __init__(self, cells: int):
        self.__cells = cells

    def __str__(self):
        return self.__cells

    def __add__(self, other):
        return self.__cells + other.__cells

    def __sub__(self, other):
        sub = self.__cells - other.__cells
        return sub if sub > 0 else 'Invalid operands. The result is negative!'

    def __mul__(self, other):
        product = self.__cells * other.__cells
        return product if product > 0 else 'Invalid operands. No cells!'

    def __truediv__(self, other):
        try:
            quotient = floor(self.__cells / other.__cells)
        except ZeroDivisionError:
            return 'Invalid operands. Division by zero.'
        return quotient if quotient > 0 else 'No cells!'

    def make_order(self, columns: int):
        num_rows = self.__cells // columns
        remainder = self.__cells % columns
        return (self.__make_row(columns)) * num_rows + self.__make_row(remainder)

    def __make_row(self, number: int):
        return ''.join(['*' for i in range(number)]) + '\n'


cell_1 = Cell(12)
cell_2 = Cell(22)

print(cell_1.make_order(5))
print(cell_2.make_order(6))

print(f'Addition: {cell_1 + cell_2}')
print(f'Subtraction: {cell_1 - cell_2}')
print(f'Multiplication: {cell_1 * cell_2}')
print(f'Division: {cell_1 / cell_2}')
