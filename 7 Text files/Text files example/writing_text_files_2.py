appointments = []
appointments.append('25/11;Bob Potters; 08:30\n')
appointments.append('30/11;René François; 12:30\n')
appointments.append('02/12;Chris Benz; 10:15\n')

with open('agenda.txt', 'w', encoding='UTF-8') as file:
    # Write data to file with writelines()
    file.writelines(appointments)


