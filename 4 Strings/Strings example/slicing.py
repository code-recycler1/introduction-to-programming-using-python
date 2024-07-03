plant = 'pineapple'

# Slicing with 2 parameters (start:end)
print(plant[4:])   # Output: 'apple'
print(plant[:4])   # Output: 'pine'
print(plant[2:5])  # Output: 'nea'

# Slicing with 3 parameters (start:end:jump_size)
print(plant[1:7:3])    # Output: 'ia'
print(plant[1::2])     # Output: 'iepl'
print(plant[:7:2])     # Output: 'pnap'
print(plant[::2])      # Output: 'pnape'
print(plant[6:1:-1])   # Output: 'ppaen'
print(plant[-2:0:-4])  # Output: 'le'


