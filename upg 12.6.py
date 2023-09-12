import os

notes = {
    "Kom ihåg!": "Ta bilen till verkstaden",
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}
while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    try:
        print(".: ALWAYSNOTE :.".center(25))
        print("-- gold edition --".center(25))
        print("*" * 25)

        for meddelande in notes:
            print(f"- {meddelande}")

        print("-" * 25)
        print("view | view note")
        print("add  | add note")
        print("rm   | remove note")
        print("exit | exit program")
        print("-" * 25)

        menu = input("menu > ")
    # Visa note
        if menu == "view":
            try:
                print("-" * 25)
                Title = input('title > ')
                print("-" * 25)
                print(notes[Title])
                print("-" * 25)
                input("Tryck på enter \nför att fortsätta...")
            except KeyError:
                print("FEL: Ange en giltig input.")
                input("Tryck på enter för \natt fortsätta...")
# Lägg till note
        elif menu == "add":
            try:
                print("-" * 25)
                Title = input('title > ')
                print("-" * 25)
                beskrivning = input("Beskrivning > ")
                if Title.strip() == "" or beskrivning.strip() == "":
                    raise Exception("FEL: Du måste ange en input!")
                notes[Title] = beskrivning
                print("INFO: Note added")
                input("Tryck på enter \nför att fortsätta...")
            except Exception as e:
                print(e)
                input("Tryck på enter \nför att fortsätta...")


# Ta bort note
        elif menu == "rm":
            print("-" * 25)
            Title = input('title > ')
            print("-" * 25)
            del notes[Title]
            print("INFO: Note removed")
            print("-" * 25)
            input("Tryck på enter \nför att fortsätta...")
# stäng program
        elif menu == "exit":
            break
        else:
            print("Ange en giltig input!")
            input("Tryck på enter \nför att fortsätta...")
    except KeyError:
        print("FEL: Ange en note som redan finns")
        input("Tryck på enter \nför att fortsätta...")
    except:
        print("Okänt fel!")
