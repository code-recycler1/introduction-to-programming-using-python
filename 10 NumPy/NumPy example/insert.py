import numpy as np

measurements = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4], float)
add_measurements = np.array([5.2, 3.5], float)
new_measurements = np.insert(measurements, 3, add_measurements)

print(measurements)
print(add_measurements)
print(new_measurements)
