with open('agenda.txt', 'a', encoding='UTF-8') as file:
    # Add data from list to file with writelines()
    appointments = []
    appointments.append('13/12;Anne Davis;08:30\n')
    appointments.append('13/12;Connor Leeds;10:00\n')
    file.writelines(appointments)


