# importeer random module
import random

# Maak array met getallen 1 tm 25 (op random posities) voor de Melanogaster
dros = random.sample(range(1, 26), 25)

# Maak array voor het genoom van de Miranda met getallen 1 tm 25
mir = range(1,26)

count = 0

while dros != mir:
    for x in range(0, 25):
        for y in range(x, 25):
            if dros[y] == x + 1:
                dros[x:y + 1] = list(reversed(dros[x:y + 1]))
                count += y + 1 - x
                print dros

print count
