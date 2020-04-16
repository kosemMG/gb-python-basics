# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.

user_input = None
with open('text_1.txt', 'w') as file:
    while user_input != '':
        user_input = input('Enter a string (press "Enter" to finish):\n')
        if user_input != '':
            file.write(f'{user_input}\n')
    else:
        print('End of input.')
