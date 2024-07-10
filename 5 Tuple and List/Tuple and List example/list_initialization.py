# Empty list
new_list = []

# List based on another list
films = ['Wonder', 'Loving Vincent', 'Red Sparrow', 'Jumanji']
films2 = ['IT', 'Once upon a time', *films[1:-1], 'Bad Cop']
print(films2)  # Output: ['IT', 'Once upon a time', 'Loving Vincent', 'Red Sparrow', 'Bad Cop']


