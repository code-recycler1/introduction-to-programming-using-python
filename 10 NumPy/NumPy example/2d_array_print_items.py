import numpy as np

points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])

for i in range(len(points)):
    for j in range(points[i].size):
        print(points[i][j], end="\t")
    print()
