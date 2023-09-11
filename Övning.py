# Skriv ut alla heltal från 0-9 utan att använda while.

# Alt 1 -- Rekommenderas
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numbers:
    print(n)

print('\n\n\n')
# Alt 2
for n in range(10):
    print(n)

print('\n\n\n')
# Alt 3
lista = list(range(10))
for tal in lista:
    print(tal)

#Skriva ut specifik del av nästlad dictionary
server = {
    'type': 'firewall',
    'open_ports': [
        1000,
        1234,
        1337
    ]
}
print(server['open_ports'][0])

#Tolkning av dictionaries
person ={
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris", "age": 3, "typ": "hund"},
        {"name": "Lisa", "age": 3,"typ": "katt"},
        {"name": "Lusy", "age": 7,"typ": "kanin"}
    ]
}
namn = (person['firstname'] + ' ' + person['lastname'])
age = person['age']
pets = person['pets']
pets_count = len(pets)

print(f"{namn} är {age} år gammal och har {pets_count} husdjur:")

for pet in pets:
    print(f"En {pet['age']} år gammal {pet['typ']} som heter {pet['name']}")
