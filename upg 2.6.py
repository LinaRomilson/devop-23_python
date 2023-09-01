print("-------------------------" )
print(".: KORVKOLLEN 1.0.1 :. ")
print("-------------------------" )
print("Hur många elever vill ha...")
a = int(input('2 vanliga korvar > '))
b = int(input('3 vanliga korvar > '))
c = int(input('2 veganska korvar > '))
d = int(input('3 veganska korvar > '))

print("-------------------------" )
print("-      INKÖPSLISTA      -")
print("-------------------------" )

VanligaKorvar = int(((a * 2) + (b * 3) + 7) / 8)        #för att en ny förpackning krävs för en korv mer än 8 st
VeganskaKorvar = int(((c * 2) + (d * 3) + 3) / 4)       #för att en ny förpackning krävs för en korv mer än 4 st
Dryck = a + b + c + d
Pris = float(VanligaKorvar * 20.95) + float(VeganskaKorvar * 34.95) + float(Dryck * 13.95)

print('| Vanlig korv:  ', VanligaKorvar, 'förpackningar')
print('| Vegansk korv: ', VeganskaKorvar, 'förpackningar')
print('| Dryck:        ', Dryck, 'drickor')
print("-------------------------" )
print('| ', Pris, 'SEK')
print("-------------------------" )
