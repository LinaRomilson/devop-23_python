# Skapa en funktion som returnerar det minsta talet från en lista
def minimum(tal):
    minstaVärdet = min(tal)
    return minstaVärdet


nummer = [3, 7, 12, 2, 8, -8]

print(f"det minsta talet är:\n{minimum(nummer)}")
