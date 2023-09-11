notes = {
    "Kom ihåg!": "Ta bilen till verkstaden",
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}


print("-----")
while True:
    TaBort = input("Ta bort artikel: ")
    try:
        del notes[TaBort]
        break
    except KeyError:
        print("FEL")


for note, meddelande in notes.items():
    print("-----")
    print(f"Titel: {note}\nText: {meddelande}")