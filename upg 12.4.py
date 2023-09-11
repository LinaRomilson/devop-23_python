notes = {
    "Kom ihåg!": "Ta bilen till verkstaden",
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}

print('Lägg till artikel: ')
while True:
    try:
        titel = input(" titel > ")
        if titel.strip() == "":
            raise Exception("FEL: Du måste ange en titel")
        text = input("  text > ")
        if text.strip() == "":
            raise Exception("FEL: Du måste ange en text")
        notes[titel] = text

        for note, meddelande in notes.items():
            print("-----")
            print(f"Titel: {note}\nText: {meddelande}")
        break
    except Exception as e:
        print(e)
