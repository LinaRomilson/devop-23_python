while True:
    try:
        TEXT = (input("Ange en text: ")).lower()
        LÄNGD_T = len(TEXT)
        if LÄNGD_T < 1:
            raise Exception("FEL: Ange en text!")
        break
    except Exception as d:
        print(d)
        continue

while True:
    try:
        BOKSTAV = (input("Ange bokstav: ")).lower()
        UPPREPNING = TEXT.count(BOKSTAV)
        if len(BOKSTAV) != 1:
            raise Exception("FEL: Ange EN bokstav")
        break

    except Exception as e:
        print(e)
        continue

print(f"bokstaven '{BOKSTAV}' förekommer {UPPREPNING} gånger i texten")