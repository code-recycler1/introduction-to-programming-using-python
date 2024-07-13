import numpy as np

loaded_data = np.loadtxt(fname='student_grades.txt', delimiter=',')
print(type(loaded_data))
print(loaded_data)

loaded_data = np.loadtxt(fname='student_grades.txt', delimiter=',', dtype=int)
print(type(loaded_data))
print(loaded_data)
