notes = {
    "Kom ihåg!": "Ta bilen till verkstaden",
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}
try:
    inmatning = input("Anteckning > ")
    print("-----")
    print(f'{notes[inmatning]}')
    print("-----")
except KeyError:
    print('FEL: Anteckning finns inte')