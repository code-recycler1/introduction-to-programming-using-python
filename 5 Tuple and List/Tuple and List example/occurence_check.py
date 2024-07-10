weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
day = input('Enter a day: ')

if day in weekdays[0:5]:
    print('Weekday')
elif day in weekdays[5:]:
    print('Weekend')
else:
    print('Input not in series:', *weekdays)


