entered_value = int(input('Please enter a number XXX: '))

first_number = entered_value // 100
third_number = entered_value % 10
second_number = entered_value // 10 % 10

result = first_number * 10 + third_number + second_number * 100

print('The result is: ', result)
