with open('kilometers.txt') as file:
    line = file.readline().rstrip()
    smallest = largest = int(line)

    line = file.readline().rstrip()
    while line:
        number = int(line)
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number
        line = file.readline().rstrip()

difference = largest - smallest
print('The difference between the largest and the smallest number =', largest, '-', smallest, '=', difference)


