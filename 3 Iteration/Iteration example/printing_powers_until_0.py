counter = 1
number = int(input('Enter number ' + str(counter) + ': '))
while number > 0:
    print("x² = " + str(number ** 2), "x³ = " + str(number ** 3), sep='\t')
    counter += 1
    number = int(input('Enter number ' + str(counter) + ': '))


