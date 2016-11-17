import random
dros = random.sample(range(1, 6), 5)
print dros
mir = range(1, 6)
print mir
dros_temp = dros
array = []

right = 1
left = 0
for x in range(0 , 10):
    print dros, "dros?"
    dros[left:right + 1] = list(reversed(dros[left:right + 1]))
    array.append(dros)
    print array, "15"
    dros[left:right + 1] = list(reversed(dros[left:right + 1]))
    right += 1
    if right == len(dros):
        left += 1
        right = left + 1
print array, "18"





