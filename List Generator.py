x = int(input('Ange ett startvärde:                  '))
y = int(input('Ange ett slutvärde (avslutas innan):  '))
z = int(input('Ange ökningen:                        '))

a = range(x, y, z)

for n in a:
    print(n)