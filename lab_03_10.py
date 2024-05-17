# Функция для подсчёта
def count_word_frequencies(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        text = file.read().lower()  # Чтение и преобразование текста к нижнему регистру
        words = text.split()  # Соединение текста в слова
        for word in words:
            word = word.strip('.,!?;:"\'()[]{}')  # Удаление пунктуации
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

# Count word frequencies in text1.txt
textDict = count_word_frequencies('text1.txt')

with open('textDict.txt', 'w') as file:
    for word, freq in textDict.items():
        file.write(f"{word}: {freq}\n")

# Вывод результатов
print("Word frequency dictionary:")
print(textDict)
