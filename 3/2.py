# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(name, surname, year_of_birth, city, email, phone_number):
    print(f'Name - {name}, surname - {surname}, year of birth - {year_of_birth}, city - {city}, email - {email}, phone number - {phone_number}')


user_info(name='Moshe', surname='Gelberg', city='Jerusalem', year_of_birth=1984, phone_number='+972-11111111', email='test@gmail.com')
