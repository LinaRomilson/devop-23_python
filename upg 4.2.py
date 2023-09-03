Multi = int(input('Ange multiplikationstabell > '))
x = 1

while True :
    print(Multi * x)
    x += 1
    print(Multi * x)
    x += 1
    print(Multi * x)
    x += 1
    Val = input("Vill du fortsätta? (ja/nej) ")
    if Val == "nej".lower():
        break