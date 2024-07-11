from os.path import exists

# check if file exists and if not create the file
if exists('agenda.txt'):
    print('The file already exists and cannot be overwritten')
else:
    with open('agenda.txt', 'w', encoding='UTF-8') as file:
        file.write('14/12;Mia Thans;12:30\n')
        file.write('15/12;Lian Sanchez;10:00\n')


