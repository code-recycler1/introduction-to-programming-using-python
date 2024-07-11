# 1: open file
with open('schedule.txt') as file:
    # 2: read line by line
    line = file.readline()
    while line:
        if line != '\n':
            record = line.split(';')
            print(record[1])
        line = file.readline()


