tal = input("tal > ")

try:
    Tal = int(tal)
    print("RESULTAT:", (Tal*2))
except ValueError:
    print("'" + tal + "'" + " kan inte översättas till ett heltal")
