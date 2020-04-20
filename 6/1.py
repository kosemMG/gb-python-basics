# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from termcolor import colored
from time import sleep


class TrafficLight:
    __colours = [
        {'background': 'on_red', 'delay': 7},
        {'background': 'on_yellow', 'delay': 2},
        {'background': 'on_green', 'delay': 7}
    ]

    def running(self):
        i = 0
        print('Traffic Light:')
        direction = 'down'
        while True:
            if i == 2:
                direction = 'up'
            print(colored('   ', None, self.__colours[i]['background']))
            sleep(self.__colours[i]['delay'])
            i = i + 1 if direction == 'down' else i - 1
            if i == 0:
                direction = 'down'


traffic_light = TrafficLight()
traffic_light.running()
