number = int(input('Enter a number: '))
counter_digits = 0
original_number = number
while number > 0:
    counter_digits += 1
    number //= 10  # number = number // 10
print(original_number, 'consists of', counter_digits, 'digits')


