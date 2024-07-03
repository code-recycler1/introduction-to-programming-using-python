count_numbers = int(input('How many numbers do you want to enter: '))
smallest = int(input('First number: '))
for i in range(count_numbers - 1):
    number = int(input('Next number: '))
    if number < smallest:
        smallest = number
print('The smallest number =', smallest)
