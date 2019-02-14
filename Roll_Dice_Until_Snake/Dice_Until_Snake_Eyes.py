import random
dice_1 = 0
dice_2 = 0

while ((dice_1 != 1) and (dice_2 != 1)):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print("dice_1 =", dice_1, "\ndice_2 =", dice_2)
    print()


print("Program finished")
