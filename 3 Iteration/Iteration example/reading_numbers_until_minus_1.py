total = count = 0
number = int(input('Enter a number, stop by entering -1: '))
while number != -1:
    count += 1
    total += number
    number = int(input('Enter a number, stop by entering -1: '))
print('Sum of the', count, 'numbers =', total)


