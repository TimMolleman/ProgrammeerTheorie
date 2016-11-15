import string
import math
import random
dros = random.sample(range(1, 26), 25)
mir = range(1, 26)
count = 0
print dros
while dros != mir:
    for x in range(0, 25):
        for y in range(0, 24):
            if dros[y] > dros[y + 1]:
                dros[y:y + 2] = list(reversed(dros[y:y + 2]))
                print dros
                count += 1
print count