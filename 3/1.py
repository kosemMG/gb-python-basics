# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


def divide(val_1, val_2):
    try:
        result = val_1 / val_2
    except ZeroDivisionError:
        return 'Error! Division by zero!'
    return result


val1 = int(input('Enter the first number: '))
val2 = int(input('Enter the second number: '))
print(divide(val1, val2))
