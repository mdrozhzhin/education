original_text = 'Сегодня был плохой день, так как половина группы в колледже получила три за практическую работу.'

modified_text = original_text.replace("три", "удовлетворительно")

words_start_with_k = sum(1 for word in original_text.split() if word.startswith("к"))

print("Исходный текст с заменой:")
print(modified_text)
print("Количество слов, начинающихся на 'к':", words_start_with_k)


text_with_mistakes = 'Это ( пример ) текста (с выражениями в скобках) . Они (могут быть ) в любом месте (  текста ) .'
# Удаление лишних пробелов вокруг скобок
modified_text = text_with_mistakes.replace("( ", "(").replace("(  ", "(").replace(" )", ")").replace("  )", ")")

print("Исходный текст с удаленными пробелами вокруг скобок:")
print(modified_text)
















mountain_peaks = ["Манаслу", "Амадаблам", "Макалу", "Непал", "Эверест",
                  "Канченджанга", "Макинли", "Лхоцзе", "Чогори", "Гашербрум",
                  "Аннапурна", "Макпхерсон", "Меру", "Коно", "Коммунизма",
                  "Пик Ленина", "Победа", "Тянь-Шань", "Мангышлак", "Алай"]

filtered_peaks = [peak for peak in mountain_peaks if peak[0] == "М"]
filtered_peaks.sort()

print(f"Список вершин, название которых начинается с 'М' и отсортированный по алфавиту:")
for peak in filtered_peaks:
    print(peak)
