import re


def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)


def count_words_starting_with_k(text):
    words = text.split()
    count = 0
    for word in words:
        if word.lower().startswith('к'):
            count += 1
    return count


def main():
    text = '''Кстати, сегодня был плохой день, потому что больше половины группы в колледже получила 
    оценку "три", часть из них - "два", а остальные - "четыре" или "пять". Какое разочарование!'''

    modified_text = replace_word(text, 'три', 'удовлетворительно')
    print("Исходный текст с заменой слова 'три':")
    print(modified_text)

    k_words_count = count_words_starting_with_k(text)
    print("Количество слов, начинающихся на 'к':", k_words_count)


if __name__ == "__main__":
    main()


def remove_spaces_around_brackets(text):
    pattern = r'(\(\s*[^)]+\s*\))'

    modified_text_with_spaces = re.sub(pattern, lambda match: match.group(0).replace(" ", ""), text)

    return modified_text_with_spaces


def main():
    text = "( Вася       ) пошёл в школу, но ( ушёл   ) в (парк      ) и (прогулял  ) (     уроки  )."

    modified_text = remove_spaces_around_brackets(text)
    print("Исходный текст с удаленными пробелами вокруг скобок:")
    print(modified_text)


if __name__ == "__main__":
    main()
