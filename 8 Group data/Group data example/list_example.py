orders = ['chocolate milk', 'chocolate milk', 'water', 'tea', 'tea']
overview = []
counter = 0

while counter < len(orders):
    drinkind = orders[counter]
    number = 0

    while counter < len(orders) and orders[counter] == drinkind:
        number += 1
        counter += 1

    overview.append([drinkind, number])

print("Overview of the orders:")
print(overview)
