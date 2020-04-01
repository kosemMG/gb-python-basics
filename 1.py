print('Hello world!')

first_name = input('Enter your name: ')
surname = input('Enter your surname: ')
print(f'Hello, {first_name} {surname}! I am happy to meet you!')

age = int(input('How old are you? '))

if age < 18:
    print('I am sorry, you are not allowed to buy cigarettes.')
else:
    print('You can buy cigarettes. But smoking is dangerous for your health!')
