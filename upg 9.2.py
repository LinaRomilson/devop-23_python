registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälingar = ["Anna", "Erik", "Karl"]

for element in avanmälingar:
    while element in registrerade:
        registrerade.remove(element)

print(registrerade)