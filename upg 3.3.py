import random

dice = random.randint(1,6)
print('Du slog en', dice, 'a')

if dice == 1 :
    print("-----------")
    print("|         |")
    print("|    X    |")
    print("|         |")
    print("-----------")
elif dice == 2 :
    print("-----------")
    print("| X       |")
    print("|         |")
    print("|       X |")
    print("-----------")
elif dice == 3 :
    print("-----------")
    print("| X       |")
    print("|    X    |")
    print("|       X |")
    print("-----------")
elif dice == 4 :
    print("-----------")
    print("| X     X |")
    print("|         |")
    print("| X     X |")
    print("-----------")
elif dice == 5 :
    print("-----------")
    print("| X     X |")
    print("|    X    |")
    print("| X     X |")
    print("-----------")
elif dice == 6 :
    print("-----------")
    print("| X     X |")
    print("| X     X |")
    print("| X     X |")
    print("-----------")
