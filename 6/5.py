# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationary:
    def __init__(self, title: str):
        self._title = title

    def draw(self):
        print('Draw start!')


class Pen(Stationary):
    def draw(self):
        print(f'{self._title} draw start!')


class Pencil(Stationary):
    def __init__(self, title: str, material='wood'):
        super().__init__(title)
        self.__material = material

    def draw(self):
        print(f'{self._title} made of {self.__material} draw start!')


class Marker(Stationary):  # Понятия не имею, кто там решил, что Handle - это маркер?! Handle - это ручка (рукоятка).
    def __init__(self, title: str, colour: str):
        super().__init__(title)
        self.__colour = colour

    def draw(self):
        print(f'{self._title} of {self.__colour} colour draw start!')


pen = Pen('Pen')
pen.draw()

pencil = Pencil('Pencil')
pencil.draw()

marker = Marker('Marker', 'blue')
marker.draw()
