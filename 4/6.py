from itertools import count, cycle, islice


def iterator(start, amount, repetitions):
    try:
        start = int(start)
        amount = int(amount)
        repetitions = int(repetitions)
    except ValueError:
        return False

    whole_numbers_list = [number for number in islice(count(start), 0, amount)]
    iterative_list = [number for number in islice(cycle(whole_numbers_list), 0, repetitions)]

    return whole_numbers_list, iterative_list


results = iterator(
    input('Enter the start number: '),
    input('Enter the amount of whole numbers to generate: '),
    input('Enter the number of repetitions: ')
)

if results:
    print(f'Whole numbers list: {results[0]}\nIterative list: {results[1]}')
else:
    print('Invalid input!')
