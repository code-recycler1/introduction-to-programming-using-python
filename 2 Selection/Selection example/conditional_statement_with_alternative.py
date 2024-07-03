# Example 1
result = 4
if result >= 10:
    print("You passed")
else:
    print("You didn't pass")

# Example 2
number = 9
if number % 2 == 0:
    print(number, 'is even')
else:
    print(number, 'is odd')

number = 12
if number % 2 == 0:
    print(number, 'is even')
else:
    print(number, 'is odd')

# Example 3
result_Jan = float(input('Enter the result of Jan: '))
result_Eva = float(input('Enter the result of Eva: '))
if result_Jan > result_Eva:
    best_result = result_Jan
else:
    best_result = result_Eva
print('The best result is', best_result)
