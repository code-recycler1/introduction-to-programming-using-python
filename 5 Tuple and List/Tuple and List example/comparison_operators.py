# Comparison by content
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True
print(a is b)  # Output: False

c = (1, 2, 3)
d = (4, 5, 6)
print(c < d)  # Output: True
print((1, 2, 5) < c)  # Output: False
print((1, 2, 3, 4, 5) < d)  # Output: True
print(('d', 'e', 'f') > ('a', 'b', 'c'))  # Output: True


print("Memory location a:", id(a))
print("Memory location b:", id(b))
print("Memory location c:", id(c))
print("Memory location d:", id(d))

# Comparison by reference
e = a
print(a is e)  # Output: True
