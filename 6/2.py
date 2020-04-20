# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длинаширинамасса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
# метода.


class Road:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def calculate_weight(self, depth: float):
        weight_per_metre = 25
        return self._length * self._width * depth * weight_per_metre / 1000


length = float(input('Enter the road length in metres: '))
width = float(input('Enter the road width in metres: '))

road = Road(length, width)
road_depth = float(input('Enter the asphalt depth in centimetres: '))
print(f'\nIn order to build a road {road.get_length()}m length, {road.get_width()}m width and '
      f'{road_depth}cm depth you need {road.calculate_weight(road_depth)} ton of asphalt.')
