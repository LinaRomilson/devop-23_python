x = int(input('Ange ett tal: '))
y = int(input('Ange ännu ett tal: '))
z = int(input('Ange ett sista tal: '))

print("-----")

if x > y and x > z :
    print(x , 'är det största talet')
elif y > x and y > z :
    print(y , 'är det största talet')
elif y == x and x > z :
    print(y , 'är de största talen')
elif y == z and z > x :
    print(y , 'är de största talen')
elif z == x and x > y :
    print(z , 'är de största talen')
elif z > x and z > y :
    print(z, 'är deet största talet')
else :
    print('Alla talen är lika stora')