# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать перегрузку метода str() для
# вывода матрицы в привычном виде. Далее реализовать перегрузку метода add() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

from typing import List
from numpy import reshape, array

MatrixType = List[list]


class Matrix:
    def __init__(self, matrix: MatrixType):
        self.__matrix = matrix

    def __str__(self):
        return str('\n'.join(['   '.join([str(number) for number in sublist]) for sublist in self.__matrix]))

    def __add__(self, other):
        result_list = []
        self_flatten_list = self.__flatten(self.__matrix)
        other_flatten_list = self.__flatten(other.__matrix)
        for i in range(len(self_flatten_list)):
            result_list.append(self_flatten_list[i] + other_flatten_list[i])

        num_rows = len(self.__matrix)
        num_columns = int(len(self_flatten_list) / num_rows)

        return Matrix(array(result_list).reshape(num_rows, num_columns))

    def __flatten(self, matrix: MatrixType):
        """Flattens a matrix to a regular list"""
        flat_list = []
        for sublist in matrix:
            for number in sublist:
                flat_list.append(number)
        return flat_list


matrix_1 = Matrix([[1, 3, 5], [2, 3, 4], [8, 7, 6]])
matrix_2 = Matrix([[1, 0, 5], [-2, 1, 2], [-5, -7, 3]])
print(matrix_1 + matrix_2)
