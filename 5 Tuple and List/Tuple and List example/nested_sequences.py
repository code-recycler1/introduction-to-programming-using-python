# Nested list
hours_school_day = [['Mon', 6], ['Tue', 4.5], ['Wed', 3], ['Thu', 0], ['Fri', 4.5]]
print('Day', 'Hours', sep='\t')
for day_hours in hours_school_day:
    for item in day_hours:
        print(item, end='\t')
    print()


