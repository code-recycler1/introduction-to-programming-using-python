vegetables = {"leek", "tomato", "celery", "endive", "fennel"}
print('The set contains', len(vegetables), 'elements')
for element in vegetables:
    print(element)
print()

# Sorting a set by converting to list
vegetable_list = list(vegetables)
vegetable_list.sort()
for element in vegetable_list:
     print(element)
