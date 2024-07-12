vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
vegetables2 = {'cucumber', 'tomato', 'celery'}
vegetables3 = {'endive', 'fennel'}

print(vegetables2.issubset(vegetables1))         # False
print(vegetables3.issubset(vegetables1))         # True
print(vegetables1.issubset(vegetables1))         # True

print(vegetables2.issuperset(vegetables3))       # False
print(vegetables1.issuperset(vegetables3))       # True

print(vegetables1.isdisjoint(vegetables2))       # False
print(vegetables2.isdisjoint(vegetables3))       # True
