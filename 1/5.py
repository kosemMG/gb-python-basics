revenue = float(input('Enter your company revenue: '))
expenses = float(input('Enter your company expenses: '))
income = revenue - expenses

if income > 0:
    print(f'Congratulations! Your company profitability coefficient is {revenue / expenses:0.2f}.')
    employees_number = int(input('How many employees do you have? '))
    print(f'Each employee earned ${income / employees_number:0.2f}.')
elif income < 0:
    print(f'Sorry. Your company is not profitable. Your loss is ${-income:0.2f}')
else:
    print(f'Unfortunately your revenue and expanses are equal. You don\'t have any profit.')
