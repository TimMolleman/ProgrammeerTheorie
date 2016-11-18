# importeer libraries
import copy
dros = [5, 2, 1, 4, 3, 7, 8]

# geef het aantal mogelijke swaps voor een array
pos_swaps = 0
num = 1
for i in range(len(dros) - 1):
    pos_swaps += len(dros) - num
    num += 1

print pos_swaps

array = []

# initialiseer de grenzen van de array
right = 1
left = 0

# doe alle mogelijke swaps voor de huidige 'dros' array
for x in range(0 , pos_swaps):
    dros[left:right + 1] = list(reversed(dros[left:right + 1]))
    back_up = copy.deepcopy(dros)
    array.append(back_up)
    dros[left:right + 1] = list(reversed(dros[left:right + 1]))
    right += 1
    if right == len(dros):
        left += 1
        right = left + 1

print array, "18"





