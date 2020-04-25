# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __str__(self):
        return f'size of fabric: {self.calculate_fabric_size} m.'

    @abstractmethod
    def calculate_fabric_size(self):
        pass


class Coat(Clothes):
    def __init__(self, size: float):
        self.__size = size

    @property
    def calculate_fabric_size(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height: float):
        self.__height = height

    @property
    def calculate_fabric_size(self):
        return round(self.__height * 2 + 0.3, 2)


coat = Coat(40)
print(f'Coat - {coat}')

suit = Suit(1.8)
print(f'Suit - {suit}')
