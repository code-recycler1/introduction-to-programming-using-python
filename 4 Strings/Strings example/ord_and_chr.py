# Overview
print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'

# Example 1: alphabet
start = ord('a')
for i in range(26):
    print(chr(start + i) + ' ', end='')

# Example 2: alphabet 6 by 6
for i in range(26):
    print(chr(start + i) + ' ', end='')
    if i % 6 == 5:
        print()


