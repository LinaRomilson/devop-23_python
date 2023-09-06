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
