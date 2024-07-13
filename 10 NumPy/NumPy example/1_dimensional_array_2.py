import numpy as np

measurements = np.array((3, 6, 9, 12), int)
print(measurements)

division = measurements / 3
print(division)

price_without_vat = np.array([100, 78.60, 60.99, 45, 1], float)
print(price_without_vat)
price_with_vat = np.around(price_without_vat * 1.21, 2)
print(price_with_vat)
