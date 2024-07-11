from random import randint


def roll_dice(number_dice):
    total = 0
    for counter in range(number_dice):
        total += randint(1, 6)
    return total


attempts = 1
while roll_dice(2) != 12:
    attempts += 1
print('After', attempts, 'attempts you rolled 12.')


