import requests
import json

while True:
    try:
        Heltal = input('Ange ett positivt heltal: ')
        tal = int(Heltal)
        break
    except ValueError:
        print("FEL: Ange ett heltal.")

url = 'https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=' + Heltal
r = requests.get(url)

e = json.loads(r.text)['even']
p = json.loads(r.text)['prime']
f = json.loads(r.text)['factors']

fac = ', '.join(str(fa) for fa in f)
if e == True:
    print(f"{Heltal} är ett jämt nummer.", end="")
else:
    print(f"{Heltal} är ett ojämt nummer.", end="")
if p == True:
    print(f" Numret är ett primtal.")
else:
    print(f" Numret är inte ett primtal.")
print(f"Numrets faktorer är {fac}")
