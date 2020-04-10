# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def sum_max_two(val1, val2, val3):
    val_list = [val1, val2, val3]
    min_val = min(val_list)
    val_list.remove(min_val)
    return sum(val_list)


print(sum_max_two(3, 9, 4))
