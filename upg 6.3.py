while True:
    try:
        Input = input("Ange sträng: ")
        Innput = Input.replace(" ", "").lower()
        Innput = Innput.replace(",", "")

        print("\r \r")
        if Innput == "":
            raise Exception("FEL: Du måste ange en sträng")
        if Innput == Innput[::-1]:
            print(f'"{Input}" är ett palindrom"')
        else:
            print(f'"{Input}" är inte ett palindrom')
        break
    except Exception as d:
        print(d)


print("\r \r")
input("Tryck på Enter för att avsluta programmet")