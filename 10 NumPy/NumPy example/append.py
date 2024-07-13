import numpy as np

measurements = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4], float)
new_measurements = np.array([5.2, 3.5], float)
combined_array = np.append(measurements, new_measurements)

print(combined_array)
