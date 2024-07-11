# 1: Open file
file = open('agenda.txt', 'w', encoding='UTF-8')
# 2: Write data to file
file.write('25/11;Bob Potters; 08:30\n')
file.write('30/11;René François; 12:30\n')
file.write('02/12;Chris Benz; 10:15\n')
# 3: Close file
file.close()


