from random import randint


def roll_dice(number_dice=1):
    """
    This function simulates throwing one or more dice.
    :param number_dice: integer that indicates the number of dice used
    :return: a list with the number of pips on each stone.
    """
    list_pips_rolled = []
    for counter in range(number_dice):
        list_pips_rolled.append(randint(1, 6))
    return list_pips_rolled


pips = roll_dice(3)
total = sum(pips)
for i, pip in enumerate(pips):
    print('Dice', i + 1, ':', pip)
print('Total:', total)
