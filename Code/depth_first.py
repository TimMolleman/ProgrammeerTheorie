import copy
import random
import numpy as np

# maak een stack waarop de nodes gepushed kunnen worden
class Stack:
     def __init__(self):
         self.items = []

    # functie die kijkt of de stack leeg is
     def isEmpty(self):
         return self.items == []

     # functie die een element bovenop de stack gooit
     def push(self, item):
         self.items.append(item)

     # haal het laatste element van de stack af
     def pop(self):
         return self.items.pop()

     # kijk naar het bovenste element dat op de stack zit
     def peek(self):
         return self.items[len(self.items)-1]

     # return de lengte van de stack
     def size(self):
         return len(self.items)

# maak een Child class aan
class Child:
    def __init__(self, array, parent, previous_count):
        self.value = array[0]
        self.parent = parent
        self.swap_count = previous_count + array[1]
        # status geeft aan of een node bezocht is of niet (1 = bezocht, 0 = niet bezocht)
        self.status = 0
        self.archive = []
        self.num_swaps = 0

    # deze functie geeft de array die het 'kind' zelf is
    def return_value(self):
        return self.value

    # deze functie geeft de parent van het kind
    def return_parent(self):
        return self.parent

    # deze functie geeft het aantal gewisselde genen tot dan toe voor Child
    def return_count(self):
        return self.swap_count

    # check of het aantal gewisselde genen hoger is dan de upperbound
    def check_bound(self):
        return self.swap_count >= upperbound

    # functie kijkt of de waarde van het kind gelijk is aan de doelwaarde
    def check_mir(self):
        return self.value == mir

    # functie die kijkt of de node in kwestie al bezocht is
    def check_status(self):
        return self.status == 1

    # functie die het archief van het kind update
    def update_archive(self):
        return self.archive.append(self.parent.value)

# kies slechts een deel van de child nodes wanneer de upperbound boven een bepaald niveau stijgt
def choose_children(children, percentage):
    scores = []

    # bepaal voor elk kind in de gegeven children array de score
    for child in children:
        score = 0
        child = child[0]

        # bepaal voor elk gen in het kind hoe ver deze van de juiste plek staat
        for i in range(len(child)):
            for j in range(len(mir)):
                if mir[j] == child[i]:
                    if j > i:
                        bad = j - i
                    elif j < i:
                        bad = i - j
                    else:
                        bad = 0
                    score += bad
        # voeg score voor ieder kind toe aan scores array
        scores.append(score)

    # transformeer scores array naar een numpy array
    np_arr = np.array(scores)

    # bepaal aantal kinderen dat behouden wordt
    amount = int(percentage * len(np_arr))

    # selecteer de indices met de laagste scores (met hoeveelheid: amount)
    sort_ar = np_arr.argsort()[:amount].tolist()

    # op basis van deze indices, maak een array met de kinderen met laagste scores
    child_arr = []
    for i in sort_ar:
        child_arr.append(children[i])
    return child_arr

# functie die alle kinderen maakt voor een bepaalde node
def create_children(currentnode, pos_swaps):
    right = 1
    left = 0
    children = []
    for x in range(0, pos_swaps):
        currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
        num_swaps = len(currentnode[left:right + 1])
        back_up = copy.deepcopy([currentnode, num_swaps])
        children.append(back_up)
        currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
        right += 1
        if right == len(currentnode):
            left += 1
            right = left + 1
    return children

# maak de drosophila aan die gespecificeerd is in de opdracht en maak de Miranda (target) aan
arr = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
dros = [arr, 0]
mir = range(1, 26)

# sla het aantal mogelijke swaps voor Drosophila array van bepaalde size
pos_swaps = 0
num = 1
for i in range(len(dros[0]) - 1):
    pos_swaps += len(dros[0]) - num
    num += 1

# stel de upperbound vast
upperbound = 99

# maak stack om children op te kunnen gooien
stack = Stack()

# maak de eerste node aan als 'Child' object en gooi deze op de stack
first_node = Child(dros, "null", 0)
stack.push(first_node)

# counter voor het aantal swaps
counter = 0

print stack.peek().value, "first array"

# maak loop die doorgaat tot de stack leeg is
while True:

    # check eerst of de stack leeg is. Zo ja, print upperbound en breek uit de loop
    if stack.isEmpty():
        print upperbound, "number of swaps"
        print last.value, "start array"
        break

    # sla de laatste child van de stack op in een variabele
    last = stack.peek()

    # sla het aantal swaps op van de laatste child op de stack en ook de array-waarde
    last_value = last.value
    current_swaps = last.swap_count

    # als de laatste node op de stack al 'visited' is, pop hem eraf. Want dan zijn er al kinderen gemaakt van deze node
    if last.check_status():
        stack.pop()

    # wanneer het aantal swaps van het laatste element op de stack hoger of gelijk is aan de upperbound:
    # pop het element van de stack
    elif last.check_bound():
            stack.pop()

    # wanneer de laatste node op de stack gelijk is aan de miranda : sla nieuwe upperbound op en pop element
    # van de stack af
    elif last.check_mir():
        upperbound = current_swaps
        stack.pop()

    # wanneer bovenstaande allemaal niet waar is: Maak kinderen voor laatste element
    else:
        # maak voor de waarde van de node nu alle kinderen aan als Child objecten
        children = create_children(last_value, pos_swaps)

        # op basis van aantal swaps, beslis hoeveel kinderen er worden aangemaakt
        if last.num_swaps < 2:
            children = choose_children(children, 0.2)
        elif last.num_swaps >= 2 and last.num_swaps < 10:
            children = choose_children(children, 0.007)
        else:
            children = choose_children(children, 0.004)

        # maak een Child object voor iedere array in de 'children' variabele en push op de stack
        for node in children:

            # check eerst of de node niet in het archief zit van parent node
            if node[0] not in last.archive:
                child = Child(node, last, current_swaps)

                # hier wordt het archief van de parent ook aan het kind gegeven
                parent_backup = copy.copy(child.parent.archive)
                child.archive = parent_backup

                # vervolgens wordt ook nog de waarde van de ouder toegevoegd aan het archief
                child.archive.append(last_value)

                # houdt het aantal swaps van alle aangemaakte kinderen bij
                child.num_swaps = child.parent.num_swaps + 1

                # alle children die
                stack.push(child)

        # maak de status van de node 'visited'. Anders worden straks alle kinderen gemaakt, en wanneer die
        # allemaal van de stack af zijn, gaat hij toch weer alle kinderen maken. Gevolg: infinite loop
        last.status = 1

    if counter % 1000 == 0:
        print last_value, "last"
        print upperbound, "upperbound"
        print last.num_swaps, "number of swaps"
        print stack.size(), "stack size"
        print counter, "counter\n"

    # laat de counter met 1 toenemen
    counter += 1










