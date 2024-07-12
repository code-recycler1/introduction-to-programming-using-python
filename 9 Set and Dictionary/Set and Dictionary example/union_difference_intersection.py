vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
vegetables2 = {'cucumber', 'tomato', 'celery'}

vegetable_union = vegetables1.union(vegetables2)
vegetable_difference = vegetables1.difference(vegetables2)
vegetable_intersection = vegetables1.intersection(vegetables2)

print('union:', vegetable_union)
print('difference:', vegetable_difference)
print('intersection:', vegetable_intersection)
