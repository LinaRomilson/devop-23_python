Kön = (input("Ange kön: "))
Kön = Kön.casefold()
Hårfärg = (input("Ange hårfärg: "))
Hårfärg = Hårfärg.casefold()
Ögonfärg = (input("Ange ögonfärg: "))
Ögonfärg = Ögonfärg.casefold()

print("-----")

if Kön == "man" : 
    if Hårfärg =="brun" :
        if Ögonfärg == "brun" :
            print("Egenskaperna matchar med: Daniel Radcliffe")
        elif Ögonfärg == "blå" :
            print("Egenskaperna matchar med: Hampus Wanne")
        else :
            print("FEL")
    elif Hårfärg == "röd" :
        if Ögonfärg == "blå" :
            print("Egenskaperna matchar med: Rupert Grint")
        else : 
            print("FEL")
    elif Hårfärg == "blond" :
        if Ögonfärg == "grön" :
            print("Egenskaperna matchar med: Valter Chrintz")
        else :
            print("FEL")
    else :
        print("FEL")
elif Kön == "kvinna" :
    if Hårfärg == "brun" :
        if Ögonfärg == "brun" :
            print("Egenskaperna matchar med: Emma Watson, Selena Gomez" )
        else :
            print("FEL")
    elif Hårfärg == "blond" :
        if Ögonfärg == "grön" :
            print("Egenskaperna matchar med: Christina Ahuilera")
        elif Ögonfärg == "blå" :
            print("Egenskaperna matchar med: Linn Blohm") 
        else :
            print("FEL")
    elif Hårfärg == "röd" :
        if Ögonfärg == "grön" :
            print("Egenskaperna matchar med: Clara Henry")
        else :
            print("FEL")
    else :
        print("FEL")
else :
    print("FEL")