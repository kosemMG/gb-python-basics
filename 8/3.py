# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.


class NumberValueError(Exception):
    def __init__(self, message: str):
        self.txt = message


user_input_str = '_'
num_list = []

while True:
    try:
        try:
            user_input_str = input('Input a number (press \'Enter\' to exit): ')
            user_input_int = int(user_input_str)
        except ValueError:
            if user_input_str == '':
                break
            raise NumberValueError('Not a number!')
    except NumberValueError as err:
        print(err)
    else:
        num_list.append(int(user_input_int))

print(num_list)
