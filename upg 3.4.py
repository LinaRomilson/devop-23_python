#.casefold() eller .lower()
Land = input('Ange ett land: ')
Land = Land.casefold()

Norden = ["danmark", "finland", "island", "norge", "sverige"]
Storbritanien = ["england", "nordirland", "skottland", "wales"]

if Land in Norden :
    print("Landet tillhör Norden")
elif Land in Storbritanien :
    print("Landet tillhör Storbritanien")
else :
    print("Fel, landet tillhör inte Norden eller Storbritanien")