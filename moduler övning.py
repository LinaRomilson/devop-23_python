# Funktioner och moduler i python
import utils
import math

# Anropa en funktion (call / invoke)
print(utils.addera(1, 2))

utils.greet("Lina")
utils.greet("Lina", "Romilson")

print('Minsta talet är:', utils.minimum([10, 2, 5, 50]))

# Anropa en funktion/variabel som finns i standardmodulen math
print(utils.MAX_NUM)
print(math.pi)
print(math.pow(2,5))