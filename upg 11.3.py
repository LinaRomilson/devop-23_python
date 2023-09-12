import json
import os
ui_width = 21

def Hämtaheltal():
    TidigareHeltal = {}
    if os.path.exists('TidigareHeltal.json'):
        with open('TidigareHeltal.json', 'r') as json_fil:
            try:
                TidigareHeltal = json.load(json_fil)
            except json.decoder.JSONDecodeError:
                TidigareHeltal = {}
    return TidigareHeltal

def SparaHeltal(TidigareHeltal):
    with open('TidigareHeltal.json', 'w') as json_fil:
        json.dump(TidigareHeltal, json_fil)

def huvudprogram():
    TidigareHeltal = Hämtaheltal()

    while True:
        try:
            inmatning = input('Ange ett heltal(eller "0" för att avsluta): ')

            if inmatning.lower() == '0':
                break

            heltal = int(inmatning)

            if heltal not in TidigareHeltal:
                TidigareHeltal[heltal] = None
                print(f"{heltal} har lagts till i dictionaryn")
            else:
                print(f"{heltal} finns redan i dictionaryn")

        except ValueError:
            print("Ogiltig inmatning. Försök igen.")

    print('Tidigare inmatade heltal.')
    for heltal in TidigareHeltal:
        print(heltal)

    SparaHeltal(TidigareHeltal)

    SparaHeltal(TidigareHeltal)

if __name__ == "__main__":
    huvudprogram()

print('.: intMEMORIZER :.'.center(ui_width))
print('*' * ui_width)

