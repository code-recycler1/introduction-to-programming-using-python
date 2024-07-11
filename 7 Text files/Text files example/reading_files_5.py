with open('schedule.txt') as file:
    # read all lines and place them in a list of strings
    all_lines = file.readlines()
    for line in all_lines:
        if line != '\n':
            print(line, end='')


