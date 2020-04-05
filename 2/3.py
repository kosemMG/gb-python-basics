seasons_list = [
    ['winter', [1, 2, 12]],
    ['spring', [3, 4, 5]],
    ['summer', [6, 7, 8]],
    ['autumn', [9, 10, 11]]
]

seasons_dictionary = {
    'winter': [1, 2, 12],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}

while True:
    month_number = int(input('Enter the number of a month (1 to 12): '))
    if month_number in range(1, 13):
        break
    print(f'{month_number} is a wrong number!')

# List solution:
for season in seasons_list:
    if month_number in season[1]:
        print(season[0])

# Dictionary solution:
for season in seasons_dictionary:
    if month_number in seasons_dictionary[season]:
        print(season)
