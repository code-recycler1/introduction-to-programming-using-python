with open('schedule.txt') as file:
    all_lines = file.readlines()
    for line in all_lines:
        if line != '\n':
            # line is split into record of fields
            record = line.split(';')
            print(record[0], record[2].rstrip(), record[1], sep='\t')


