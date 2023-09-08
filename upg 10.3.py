import os
ui_width = 21

while True:
    #Rensa terminalen
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    print('.: PEOPLES DATABASE :.')
    print('-' * ui_width)
    print('get_id | Get person by ID\nscan_f | List people by FORENAME\nscan_s | List people by SURNAME\nexit   | Exit program')
    print('-' * ui_width)
    menu = input('| > ')

    if menu == 'get_id':
        # Skapa funktion för att hämta info baserat på ID
        def HämtaInfoMedID(filnamn,SöktID):
            with open('database.csv', 'r', encoding='utf-8') as fil:
                for rad in fil:
    # Dela upp raden i komponenter
                    komponenter = rad.split(',')
                # Extrahera de specifika delarna
                    id = komponenter[0]
                    if id == SöktID:
                        return komponenter

            return None
# Låter användaren välja ID
        AnvändarID = input('Ange ett ID: ')
#Hämta info från filen
        InfoID = HämtaInfoMedID('database.csv', AnvändarID)

#Skriv ut infon om den hittades
        if InfoID:
            print(f'ID: {InfoID[0]}')
            print(f'Namn: {InfoID[1]}')
            print(f'Efternamn: {InfoID[2]}')
            print(f'Kön: {InfoID[3]}')
            print(f'Födelseår: {InfoID[4]}')
            input('Tryck enter för att fortsätta...')
        else:
            print('Inget ID matchade det angivna ID:t')
            input('Tryck på enter för att fortsätta...')

    elif menu == 'scan_f':
        Förnamn= input('Ange ett förnamn: ')
        #Skapa funktion för att hämta lista med namn utifrån förnamn
        def HämtaInfoMedFörnam(filnamn, SöktNamn):
            matchandeRader =[]
            #öppna fil för läsning
            with open(filnamn, 'r', encoding='utf-8') as fil:
                # Läs igenom raderna i filen
                for rad in fil:
                    komponenter = rad.split(',')
                    förnamn = komponenter[1]
                    # Kontrollera om namnet finns i filen
                    if SöktNamn in förnamn:
                        matchandeRader.append(rad)
            return matchandeRader
        # Ange filnamn och sökt sträng
        filnamn = 'database.csv'
        SöktNamn = Förnamn

        #Anropa funktionen
        InfoFörnamn = HämtaInfoMedFörnam('database.csv',Förnamn)

        #Skriv ut de matchande raderna
        if InfoFörnamn:
            for rad in InfoFörnamn:
                print(rad.strip())

            input('Tryck på enter för att fortsätta...')
        else:
            print('Inget matchande namn hittades')
            input('Tryck på enter för att fortsätta...')
    elif menu == 'scan_s':
        Efternamn= input('Ange ett efternamn: ')
        #Skapa funktion för att hämta lista med namn utifrån förnamn
        def HämtaInfoMedFörnam(filnamn, SöktEfterNamn):
            matchandeRader =[]
            #öppna fil för läsning
            with open(filnamn, 'r', encoding='utf-8') as fil:
                # Läs igenom raderna i filen
                for rad in fil:
                    komponenter = rad.split(',')
                    efternamn = komponenter[2]
                    # Kontrollera om namnet finns i filen
                    if SöktEfterNamn in efternamn:
                        matchandeRader.append(rad)
            return matchandeRader
        # Ange filnamn och sökt sträng
        filnamn = 'database.csv'
        SöktNamn = Efternamn

        #Anropa funktionen
        InfoEfternamn = HämtaInfoMedFörnam('database.csv',Efternamn)

        #Skriv ut de matchande raderna
        if InfoEfternamn:
            for rad in InfoEfternamn:
                print(rad.strip())
            input('Tryck på enter för att fortsätta...')
        else:
            print('Inget matchande namn hittades')
            input('Tryck på enter för att fortsätta...')
    elif menu == 'exit':
        break
    else:
        print('Ange en giltig input')
        input('Tryck på enter för att fortsätta...')
