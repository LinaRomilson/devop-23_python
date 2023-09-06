import os

POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:
    # 1. Rensa terminalfönster
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    # 2. Skriv ut instruktioner
    print('.: basicBILLBOARD :.')
    print('********************')
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print('--------------------')
    print('c | Ändra post')
    print('e | Stäng program')
    print('--------------------')

    # 3. Hämta kommando från användaren
    meny = input('meny > ')
    # 4. Utför operationer för inmatat kommando
    if meny == 'c':
        idn = input('id > ')
        if idn == '1':
            meddelande = input('meddelande > ')
            POST_1 = meddelande                         # Ändrar meddelandet i posten
        elif idn == '2':
            meddelande = input('meddelande > ')
            POST_2 = meddelande                         # Ändrar meddelandet i posten
        elif idn == '3':
            meddelande = input('meddelande > ')
            POST_3 = meddelande                         # Ändrar meddelandet i posten
        else:
            print(f"-FEL: Felaktigt ID\n- INFO: Vänligen ge heltal mellan 1-3\n--------------------")
            input('Tryck enter för att fortsätta...')  # Pausa exekvering
    elif meny == 'e':
        break
    else:
        print(f"- FEL: Okänt kommando ({meny})\n--------------------")
        input('Tryck enter för att fortsätta...')  # Pausa exekvering
