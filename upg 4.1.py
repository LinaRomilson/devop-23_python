print("NUMANALYZER")
print("  v1.33.7")

x = int(input('Tal < '))

NumberList = []

while x > 0 :
    print(x)
    NumberList.append(x)
    x = int(input ('Tal < '))

Summa = sum(NumberList)
Minst = min(NumberList)
Störst = max(NumberList)
Medel = round((Summa / len(NumberList)), 2)

print("Minsta tal: ", Minst)
print("Största tal:", Störst)
print("Summa:      ", Summa)
print("Medelvärde: ", Medel)