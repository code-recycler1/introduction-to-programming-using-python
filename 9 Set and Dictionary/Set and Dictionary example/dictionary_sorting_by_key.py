word = input('Enter a word: ')
characters = {}

# Go through letters in word
for letter in word:
    # Check if letter is present in dictionary
    if letter in characters:
        characters[letter] += 1    # Increase value via key
    else:
        characters[letter] = 1     # Create new key/value pair

# Print key/value pairs
for character in sorted(characters):
    print(character, characters[character])

print()

for character in sorted(characters, reverse=True):
    print(character, characters[character])
