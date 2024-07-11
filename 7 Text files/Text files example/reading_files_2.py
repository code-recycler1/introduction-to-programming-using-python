# 1: open file
with open('schedule.txt') as file:
    # 2: read line by line
    line = file.readline()
    while line:
        if line != '\n':
            print(line.rstrip())
        line = file.readline()


