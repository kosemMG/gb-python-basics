word_list = input('Enter several words: ').split()

for i, word in enumerate(word_list):
    print(f'{i + 1} - {word[:10]}')
