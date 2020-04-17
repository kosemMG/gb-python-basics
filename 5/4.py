# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# Google Translate API Instruction: https://stackabuse.com/text-translation-with-google-translate-api-in-python/

from googletrans import Translator

translator = Translator()

lines = []

with open('text_4_translation.txt', 'w') as new_file:
    try:
        with open('textd_4.txt', 'r') as file:
            for line in file:
                line_list = line.split('-')
                translation = translator.translate(line_list[0], src='en', dest='ru').text
                lines.append(f'{translation} -{line_list[1]}')
    except IOError:
        print('File not found!')
    new_file.writelines(lines)
