import numpy as np

points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
print('Lowest over all rows:', np.min(points, axis=0))
print('Lowest over all columns:', np.min(points, axis=1))
print('Highest over all rows:', np.max(points, axis=0))
print('Highest over all columns:', np.max(points, axis=1))
