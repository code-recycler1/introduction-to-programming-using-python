from os.path import exists

# check if file exists and if not create the file
if exists('agenda.txt'):
    file = open('agenda.txt', 'a', encoding='UTF-8')
else:
    file = open('agenda.txt', 'w', encoding='UTF-8')

file.write('14/12;Mia Thans;12:30\n')
file.write('15/12;Lian Sanchez;10:00\n')
file.close()


