# Example
points_Python = float(input('Enter your result for Python: '))
if points_Python >= 10:
    print('You passed')
elif points_Python >= 8:
    print('You can tolerate')
else:
    print("You didn't pass")

# Structured
points_Python = float(input('Enter your result for Python: '))
if points_Python >= 10:
    print('You passed')
else:
    if points_Python >= 8:
        print('You can tolerate')
    else:
        print("You didn't pass")


