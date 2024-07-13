import numpy as np

points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
print(points[0, :])
print(points[:, 0])
print(points[:, 1])
print(points[0:2, :])
