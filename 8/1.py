# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

from typing import List


class Date:
    def __init__(self, date_str: str):
        self.__date_str = date_str

    def __str__(self):
        date_list = Date.__modify(self.__date_str)
        if Date.__validate(date_list):
            return '.'.join([str(item) for item in date_list])
        return 'Invalid date input.'

    @classmethod
    def __modify(cls, date_str: str):
        return [int(num) for num in date_str.split('-')]

    @staticmethod
    def __validate(date_list: List[int]):
        return 0 < date_list[0] <= 31 and 0 < date_list[1] <= 12 and 1900 < date_list[2] <= 2100


date = Date('32-01-2020')
print(date)
