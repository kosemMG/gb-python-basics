# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

total_words_count = 0
try:
    with open('text_2.txt', 'r') as file:
        for i, line in enumerate(file):
            words_count = len(line.split())
            total_words_count += words_count
            print(f'{i + 1} - words: {words_count} - {line}', end='')

    print(f'\nTotal lines: {i + 1}\nTotal words: {total_words_count}')
except IOError:
    print('File not found!')
