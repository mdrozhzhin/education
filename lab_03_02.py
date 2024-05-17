'''
 Множества
'''

# создание множества
b1 = set()
print("Set b1 = ", b1)
b2 = {"bear", "fox", "squirrel", "woodpecker", "woodpecker", "wolf", "hedgehog"}
print("Set b2 = ", b2)

# создание множества из строки
b3 = set("abcdabcdefg")
print("Set b3 from string: ", set(b3))
print("\n")

# строковая переменная s
s = "Electricity is the set of physical phenomena associated with the presence of electric charge. Lightning is one of the most dramatic effects of electricity."

# создание множества set1 из строки s
set1 = set(s.split())

# вывод множества set1 на экран
print("Set set1 from string s: ", set1)

# проход по элементам множества set1 и вывод гласных букв
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # множество гласных букв

print("Гласные буквы в множестве set1:")
for word in set1:
    for char in word:
        if char in vowels:
            print(char, end=' ')  # вывод гласных букв на экран
print()  # печать пустой строки для чистоты вывода

