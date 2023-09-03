import random
slump = random.randint(0,99)

Gissningar = []

print(".: THE HIGHER LOWER GAME :.")
print("---------------------------")
print("Welcome to The Higher Lower " )
print("Game. I will randomise a ")
print("number between 0 and 99")
print("Can you guess it?")
print("---------------------------")

Gissning = int(input('Your guess > '))
Gissningar.append(Gissning)
if Gissning == slump :
    print(Gissning, "is correct!")
    print("It took you", len(Gissningar), "guesses")
elif Gissning > slump :
    print("LOWER!")
elif Gissning < slump :
    print("HIGHER!")
else :
    print("FEL")

while True :
    Gissning = int(input('Try again > '))
    Gissningar.append(Gissning)
    if Gissning == slump :
        print(Gissning, "is correct!")
        print("It took you", len(Gissningar), "guesses")
        break
    elif Gissning > slump :
        print("LOWER!")
    elif Gissning < slump :
        print("HIGHER!")
    else :
        print("FEL")
        break
