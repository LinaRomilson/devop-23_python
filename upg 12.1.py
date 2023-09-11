notes = {
    "Kom ihåg!": "Ta bilen till verkstaden",
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}
try:
    Inmatning = input("Anteckning > ")
    print("-----")
    print(f'{notes[Inmatning]}')
    print("-----")
except KeyError:
    print('FEL: Anteckning finns inte')