# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать
# список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить ее в словарь (со значением убытков). Итоговый список сохранить в виде json-объекта
# в соответствующий файл.

import json

report = []
companies = {}

with open('text_7_report.json', 'w') as json_file:
    try:
        with open('text_7.txt', 'r') as txt_file:
            total = 0
            counter = 0
            for line in txt_file:
                company = line.split()
                profit = int(company[2]) - int(company[3])
                companies[company[0]] = profit
                if profit > 0:
                    counter += 1
                    total += profit

            report = [companies, {'average_profit': total / counter}]
    except IOError:
        print('File not found!')

    json.dump(report, json_file, ensure_ascii=False, indent=2)
