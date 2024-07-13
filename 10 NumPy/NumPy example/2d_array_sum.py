import numpy as np

points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
print("Total per course:", points.sum(0))
print("Total per student:", points.sum(1))
