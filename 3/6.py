# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def capitalize(string):
    """
    Function receives a string, verifies it's lowercase and latin and capitalises each word.
    :param string: str
    :return: str - capitalised string
    """
    is_invalid = True
    while is_invalid:
        for char in string:
            if not (97 <= ord(char) <= 122 or ord(char) == 32):
                string = input('Wrong input! Enter lowercase latin words: ')
                break
        else:
            is_invalid = False
    updated_words = []
    words = string.split()
    for word in words:
        updated_words.append(word[0].upper() + word[1:])
    return ' '.join(updated_words)


sentence = input('Enter lowercase latin words: ')
print(capitalize(sentence))
