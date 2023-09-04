#bredden på ui
ui_bredd = 21

print("*" * ui_bredd)
print("* The Great Divider *".center(ui_bredd))
print("-" * ui_bredd)
print("")
print("\t Beräknar c för uttrycket:".center(ui_bredd))
print("")
print("\t a / b = c")
print("")
print("-" * ui_bredd)

a= input('a = ')
while True:
    try:
        A = float(a)
        break               #Bryter loopen om omvandligen lyckas
    except ValueError:
        print("FEL: Ogiltigt nummer")
        a = input('a = ')


b = input('b =  ')
while True:
    try:
        B = float(b)
        break
    except ValueError:
        print("FEL: Ogiltigt nummer")
        b = input('b = ')




print("-" * ui_bredd)
try:
    C = round(float(A/B),2)
    if A == 0 or B == 0:
        raise Exception("Det går inte att dela med 0")      #skapa exeption
except Exception as e:
    print("FEL: Division med 0")

if A != 0 and B != 0:
    print(A, "/", B, "=", C )