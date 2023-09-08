ui_width = 21
print('-' * ui_width)
print('- NUMANALYZER -'.center(ui_width))
print('-' * ui_width)

#Definera funktion
def räkna_förekomster():
    nollor = 0
    ettor = 0
    tvåor = 0
    treor = 0
    fyror = 0
    femmor = 0
    sexor = 0
    sjuor = 0
    åttor = 0
    nior = 0

    # Öppnar filen
    with open('numbers.csv', 'r') as fil:
        # Läser igenom varje rad
        for rad in fil:
            # Loopar så att varje tecken i raden läses igenom
            for tecken in rad:
                if tecken == '0':
                    nollor += 1
                elif tecken == '1':
                    ettor += 1
                elif tecken == '2':
                    tvåor += 1
                elif tecken == '3':
                    treor += 1
                elif tecken == '4':
                    fyror += 1
                elif tecken == '5':
                    femmor += 1
                elif tecken == '6':
                    sexor += 1
                elif tecken == '7':
                    sjuor += 1
                elif tecken == '8':
                    åttor += 1
                elif tecken == '9':
                    nior += 1
    return nollor, ettor, tvåor, treor, fyror, femmor, sexor, sjuor, åttor, nior


# Anger filnamn
filnamn = 'numbers.csv'

# Anropar funktionen för att räkna förekomsten av talen
nollor, ettor, tvåor, treor, fyror, femmor, sexor, sjuor, åttor, nior = räkna_förekomster()

print(f'| 0 | {nollor}')
print(f'| 1 | {ettor}')
print(f'| 2 | {tvåor}')
print(f'| 3 | {treor}')
print(f'| 4 | {fyror}')
print(f'| 5 | {femmor}')
print(f'| 6 | {sexor}')
print(f'| 7 | {sjuor}')
print(f'| 8 | {åttor}')
print(f'| 9 | {nior}')

print('-' * ui_width)
