# Logical operator: not
warm = False
if not warm:
    print('Put on a sweater')

# Logical operator: and
# Example 1
warm = True
has_cycle = True
if warm and has_cycle:
    print('He drives to school by bike')

# Example 2
length = 125
if length >= 100 and length <= 140:
    print('You pay €29 at the checkout')

# Example 2 simplified
length = 125
if 100 <= length <= 140:
    print('You pay €29 at the checkout')

# Logical operator: or
# Example 1
holiday = False
weekend = True
if holiday or weekend:
    print('We are going out to dinner')

# Example 2
month = 'July'
if month == 'July' or month == 'August':
    print('it is summer')

# Logical operator: in
month = 'July'
if month in ['July', 'August']:
    print('it is summer')

# Combine logical operators
month = 'May'
if month != 'July' and month != 'August':
    print('The academic year is ongoing')

month = 'May'
if month not in ['July', 'August']:
    print('The academic year is ongoing')

month = 'May'
if not month in ['July', 'August']:
    print('The academic year is ongoing')