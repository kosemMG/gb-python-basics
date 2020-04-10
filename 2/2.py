my_list = []

while True:
    value = input('Enter values one by one. Press "Enter" to finish: ')
    if value == '':
        break
    my_list.append(value)

print(f'Your list is {my_list}')

for i in range(1, len(my_list), 2):
    buffer = my_list[i - 1]
    my_list[i - 1] = my_list[i]
    my_list[i] = buffer

print(f'Changed list is {my_list}')
