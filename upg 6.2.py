print("Robber Translate")
print("-----------------")

while True:
    try:
        Svenska = input("Svenska \t < ").lower()
        if "b" in Svenska:
            Svenska = Svenska.replace("b", "bob")

        if "c" in Svenska:
            Svenska = Svenska.replace("c", "coc")

        if "d" in Svenska:
            Svenska = Svenska.replace("d", "dod")

        if "f" in Svenska:
            Svenska = Svenska.replace("f", "fof")

        if "g" in Svenska:
            Svenska = Svenska.replace("g", "gog")

        if "h" in Svenska:
            Svenska = Svenska.replace("h", "hoh")

        if "j" in Svenska:
            Svenska = Svenska.replace("j", "joj")

        if "k" in Svenska:
            Svenska = Svenska.replace("k", "kok")

        if "l" in Svenska:
            Svenska = Svenska.replace("l", "lol")

        if "m" in Svenska:
            Svenska = Svenska.replace("m", "mom")

        if "n" in Svenska:
            Svenska = Svenska.replace("n", "non")

        if "p" in Svenska:
            Svenska = Svenska.replace("p", "pop")

        if "q" in Svenska:
            Svenska = Svenska.replace("q", "qoq")

        if "r" in Svenska:
            Svenska = Svenska.replace("r", "ror")

        if "s" in Svenska:
            Svenska = Svenska.replace("s", "sos")

        if "t" in Svenska:
            Svenska = Svenska.replace("t", "tot")

        if "v" in Svenska:
            Svenska = Svenska.replace("v", "vov")

        if "w" in Svenska:
            Svenska = Svenska.replace("w", "wow")

        if "x" in Svenska:
            Svenska = Svenska.replace("x", "xox")

        if "z" in Svenska:
            Svenska = Svenska.replace("z", "zoz")

        if len(Svenska) < 1:
            raise Exception("FEL: Ange en text på svenska")
        break
    except Exception as e:
        print(e)

print("Rövarspråk   >", Svenska)