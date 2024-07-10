films = ['Wonder', 'Loving Vincent', 'Red Sparrow', 'Jumanji']

films.append('Loveless')
print(films)  # Output: ['Wonder', 'Loving Vincent', 'Red Sparrow', 'Jumanji', 'Loveless']

films.insert(2, 'Loveless')
print(films)  # Output: ['Wonder', 'Loving Vincent', 'Loveless', 'Red Sparrow', 'Jumanji']

films.remove('Wonder')
print(films)  # Output: ['Loving Vincent', 'Loveless', 'Red Sparrow', 'Jumanji']

films.pop(0)
print(films)  # Output: ['Loveless', 'Red Sparrow', 'Jumanji']

films.sort()
print(films)  # Output: ['Jumanji', 'Loveless', 'Red Sparrow']

films.extend(['It', 'Tenet'])
print(films)  # Output: ['Jumanji', 'Loveless', 'Red Sparrow', 'It', 'Tenet']

print(films.index('It'))  # Output: 3

print(films.count('Red Sparrow'))  # Output: 1

films.reverse()
print(films)  # Output: ['Tenet', 'It', 'Red Sparrow', 'Loveless', 'Jumanji']


