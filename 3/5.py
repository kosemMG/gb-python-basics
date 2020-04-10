# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_list(arr):
    i = 0
    while i < len(arr):
        try:
            arr[i] = float(arr[i])
        except ValueError:
            # if the special symbol was entered - exit
            if arr[i] == '@':
                return sum(arr[:i]), False
            # if a different symbol was entered - just remove it and continue
            arr.remove(arr[i])
            i -= 1
        i += 1
    return sum(arr), True


result = 0
while True:
    num_list = input('Enter numbers string divided with a whitespace or \'@\' to finish: ').split()
    result_tuple = sum_list(num_list)
    result += result_tuple[0]
    print(f'Current sum: {result}')
    if not result_tuple[1]:
        break

print(f'Total sum: {result}')
