# Visa hur man med en for-loop kan beräkna
# 1. summan av alla heltal mellan 0 - 1000000
summa = 0
for tal in range(1000001):
    summa += tal
print(summa)
# 2. summan av alla udda tal mellan 0 - 500
summa = 0
for nummer in range(1, 501, 2):
    summa += nummer
print(summa)