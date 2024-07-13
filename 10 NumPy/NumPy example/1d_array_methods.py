import numpy as np

measurements = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4], float)
print('Amount of measurements: ', len(measurements))

for i in range(measurements.size):
    print(measurements[i])

print('Highest measurement:', measurements.max())
print('Lowest measurement:', measurements.min())
print('Average:', measurements.mean())
print('Sum of measurements', measurements.sum())
