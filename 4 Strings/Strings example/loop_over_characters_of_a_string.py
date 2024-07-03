sport = "baseball"

# Example 1: Using a while loop
print('Example 1: Using a while loop')
i = 0
while i < len(sport):
    print(sport[i])
    i += 1

print()

# Example 2: Using a for loop with range
print('Example 2: Using a for loop with range')
for i in range(len(sport)):
    print(i, sport[i])

print()

# Example 3: Using a for loop directly
print('Example 3: Using a for loop directly')
for letter in sport:
    print(letter)

