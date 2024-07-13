import numpy as np

measurements = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4], float)
print('Amount of measurements: ', len(measurements))

for i in range(measurements.size):
    print('index:', i, ':', measurements[i])
