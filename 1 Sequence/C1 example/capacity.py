# Number of trains per hour (input as integer)
trains_per_hour = int(input("Enter the number of trains per hour: "))

# Number of places per train (input as integer)
places_per_train = int(input("Enter the number of places per train: "))

# Boarding time in minutes
minutes_boarding_time = 0.5

# Ride duration in minutes
minutes_per_ride = 2

# Calculate capacity per hour
capacity_per_hour = trains_per_hour * places_per_train * 60 / (minutes_boarding_time + minutes_per_ride)

# Print the maximum capacity per hour
print('\nThe maximum capacity of the roller coaster per hour is', int(capacity_per_hour), 'persons')


