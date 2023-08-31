print('Hur gammal är du? ')
x = int(input())
y = 18 - x
if x < 18 :
    print('Du får inte dricka än,' , y , 'år kvar.')
elif x == 18 :
    print('Grattis! Du får dricka!')
else :
    print('Du får redan dricka!')