count_zeros = 0
sum_positive = 0

with open('a.txt', 'r') as file:
    numbers_str = file.read()

    numbers_list = numbers_str.split(', ')

    for num_str in numbers_list:
        number = float(num_str)

        if number == 0:
            count_zeros += 1
        elif number > 0:
            sum_positive += number

print("Количество нулевых элементов:", count_zeros)
print("Сумма положительных элементов:", sum_positive)


delimiters = [' ', '.', ',', ':', ';', '!', '?', '\n']

with open('входной-файл.txt', 'r') as input_file, open('новый_файл.txt', 'w') as output_file:
    while True:
        char = input_file.read(1)
        if not char:
            break
        if char not in delimiters:
            output_file.write(char)

