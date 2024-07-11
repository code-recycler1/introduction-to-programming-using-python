from math import sqrt

number = int(input('Enter an integer: '))
if number < 0:
    print('Square root of a negative number does not exist!')
else:
    print('Square root of', number, 'is', sqrt(number))


