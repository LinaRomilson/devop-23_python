ui_bredd = 21

print(".: MATHLETE v2.0 :.".center(ui_bredd))
print("-" * ui_bredd)

lista = []
while True:
    Tal = input('> ')
    try:
        if Tal.lower() == "exit":       #avslutar loopen
            break
        tal = float(Tal)
        lista.append(tal)
    except ValueError:                  #om annat än exit skrivs ut kommer felmeddelande
        print("FEL: Ogiltigt nummer")

print("-" * ui_bredd)
print("Kardinalitet:", len(lista))
print("Summa:\t\t ", sum(lista))
print("Medelvärde:\t ", round((sum(lista)/len(lista)),2))
