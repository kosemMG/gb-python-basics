number = int(input('Enter a number: '))
max_digit = 0

while number != 0:
    digit = number % 10
    if digit == 9:
        max_digit = digit
        break
    if digit > max_digit:
        max_digit = digit
    number = number // 10

print(f'Maximal digit is {max_digit}.')
