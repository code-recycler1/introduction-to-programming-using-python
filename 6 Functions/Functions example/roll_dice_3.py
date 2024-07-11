from random import randint


def roll_dice(number_dice=1):
    """    """
    if type(number_dice) != int or number_dice <= 0:
        return None
    else:
        pips_rolled = []
        for i in range(0, number_dice):
            pips_rolled.append(randint(1, 6))
        return pips_rolled


assert roll_dice(2.5) == None
