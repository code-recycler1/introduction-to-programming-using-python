import numpy as np

loaded_data = np.genfromtxt(fname='student_grades_2.txt', delimiter=',', dtype=int, filling_values='0')
print(loaded_data)
