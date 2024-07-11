from roll_dice_2 import roll_dice


assert len(roll_dice()) == 1
assert len(roll_dice(5)) == 5
assert len(roll_dice(0)) == 0
assert len(roll_dice(-3)) == 0

assert sum(roll_dice()) >= 1
assert sum(roll_dice()) <= 6
assert sum(roll_dice(2)) <= 12


