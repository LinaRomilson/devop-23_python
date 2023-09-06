import os.path

# öppna befintlig fil
if os.path.exists('textfil.txt'):
    f = open('textfil.txt', 'a')
else:
    # skapa ny fil
    f = open('textfil.txt', 'x')

# Skriv till en fil
f.write("Rad 1\n")
f.write("Rad 2\n")
f.write("Rad 2\n")

# Läsa från en fil
f = open('textfil.txt', 'r')
text = f.read()

# Stänga en fil
f.close()

# Ta bort en fil (import os ska vara högst upp)
import os

if os.path.exists("textfil.txt"):
    os.remove("textfil.txt")
else:
    print("The file does not exist")

# Filhantering med with (öppna fil)
with open("textfil.txt") as f:
    text = f.read()
print(text)

# Öppna och läs fil
with open("textfil.txt", 'a+') as f:
    f.write("Rad 4\n")
    f.seek(0)
    text = f.read()
print(text)

# Lagra en lista i fil med JSON (import json ska vara högst upp)
import json

attendants = ['Åsa', 'Kalle', 'Olivia', 'Johan']
with open('data.json', 'w') as f:
    f.write(json.dumps(attendants))

# Läsning av JSON- formaterad list från fil
# import json
with open('data.json') as f:
    data = json.loads(f.read())
print(data[0])
