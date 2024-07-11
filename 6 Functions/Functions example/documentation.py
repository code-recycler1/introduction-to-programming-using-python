from random import randint


def roll_dice(number_dice=1):
    """
    This function simulates rolling one or more dice.
    :param number_dice: integer that indicates the number of dice used
    :return: the number of pips rolled
    """
    total = 0
    for counter in range(number_dice):
        total += randint(1, 6)
    return total


help(roll_dice)


