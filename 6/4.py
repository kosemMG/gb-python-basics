# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.


class Car:
    def __init__(self,
                 speed: float,
                 color: str,
                 name: str,
                 is_police: bool):
        self._speed = speed
        self._color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        print(f'{"Police car " if self._is_police else ""}{self.name} started!')

    def stop(self):
        print(f'{self.name} stopped!')

    def turn(self, direction: str):
        print(f'{self.name} is turning to the {direction}.')

    def show_speed(self):
        print(f'The speed of {self.name} is {self._speed}.')


class TownCar(Car):
    __speed_limit = 60

    def show_speed(self):
        if self._speed > self.__speed_limit:
            print(f'Warning! Your speed is {self._speed} km/h. You have broken the speed limit!')
        else:
            print(f'The speed of {self.name} is {self._speed}.')


class SportCar(Car):
    pass


class WorkCar(Car):
    __speed_limit = 40

    def show_speed(self):
        if self._speed > self.__speed_limit:
            print(f'Warning! Your speed is {self._speed} km/h. You have broken the speed limit!')
        else:
            print(f'The speed of {self.name} is {self._speed}.')


class PoliceCar(Car):
    def stop_car(self, car: Car):
        print(f'Police car arrested {car.name}!')


town_car = TownCar(55, 'blue', 'Mazda', False)
town_car.go()
town_car.show_speed()
town_car.turn('right')
town_car.stop()

work_car = WorkCar(60, 'brown', 'Mercedes', False)
work_car.go()
work_car.show_speed()

police_car = PoliceCar(90, 'white', 'Toyota', True)
police_car.go()
police_car.show_speed()
police_car.stop_car(work_car)
work_car.stop()

