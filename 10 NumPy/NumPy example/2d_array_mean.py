import numpy as np

points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
print('Average per course:', np.mean(points, axis=0))
print('Average per student:', np.mean(points, axis=1))
