import re


def replace_word(text, old_word, new_word):
    """
    Заменяет все вхождения old_word на new_word в тексте.
    """
    return text.replace(old_word, new_word)


def count_words_starting_with_k(text):
    """
    Подсчитывает количество слов, начинающихся на 'к'.
    """
    words = text.split()
    count = 0
    for word in words:
        if word.lower().startswith('к'):
            count += 1
    return count


def main():
    text = '''Кстати, сегодня был плохой день, потому что больше половины группы в колледже получила 
    оценку "три", часть из них - "два", а остальные - "четыре" или "пять".'''

    modified_text = replace_word(text, 'три', 'удовлетворительно')
    print("Исходный текст с заменой слова 'три':")
    print(modified_text)

    # Вычисляем количество слов, начинающихся на 'к'
    k_words_count = count_words_starting_with_k(text)
    print("Количество слов, начинающихся на 'к':", k_words_count)


if __name__ == "__main__":
    main()


def remove_spaces_around_brackets(text):
    """
    Удаляет пробелы после открывающей скобки и перед закрывающей скобкой в тексте.
    """
    # Используем регулярное выражение для поиска выражений в скобках
    pattern = r'(\(\s*[^)]+\s*\))'

    # Заменяем найденные выражения, убирая пробелы вокруг скобок
    modified_text_with_spaces = re.sub(pattern, lambda match: match.group(0).replace(" ", ""), text)

    return modified_text_with_spaces


def main():
    # Получаем текст от пользователя
    text = "( Вася) пошёл в школу, но (его ) сбила (  машина  )."

    # Удаляем пробелы вокруг скобок
    modified_text = remove_spaces_around_brackets(text)
    print("Исходный текст с удаленными пробелами вокруг скобок:")
    print(modified_text)


if __name__ == "__main__":
    main()
