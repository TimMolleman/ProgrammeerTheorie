import copy
import random

# dros arrays
dros = random.sample(range(1, 11), 10)
mir = range(1, 11)

# geef het aantal mogelijke swaps voor een array
pos_swaps = 0
num = 1
for i in range(len(dros) - 1):
    pos_swaps += len(dros) - num
    num += 1

archive = []

def hillClimb(dros, mir, swaps):

    # create the first node
    currentnode = dros
    back_up1 = copy.deepcopy(currentnode)
    archive.append(back_up1)

    while (currentnode != mir):

        # create child nodes
        children = []
        right = 1
        left = 0
        for x in range(0, swaps):
            currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
            back_up = copy.deepcopy(currentnode)
            state = False # houdt false als currentnode niet in archief
            for y in archive:
                # print y
                if back_up == y:
                    state = True # maak state true als currentnode wel in archief
                    break
            if state == False:
                children.append(back_up)
            currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
            right += 1
            if right == len(dros):
                left += 1
                right = left + 1

        array_right = []
        currentnode = []

        # vul een array met hoeveel posities elke in vergelijking heeft met mir
        for child in children:
            right_place = 0
            count = 0
            for j in child:
                if j == mir[count]:
                    right_place +=1
                    count += 1
                else:
                    count += 1
            array_right.append(right_place)
        print array_right

        # selecteer de arrays die meeste elementen op hun plek hebben
        m = max(array_right)
        print m
        max_indices = [i for i, j in enumerate(array_right) if j == m]
        print max_indices

        for i in max_indices:
            currentnode.append(children[i])

        print currentnode
        # back_up2 = copy.deepcopy(currentnode)
        # archive.append(back_up2)
        # print archive
        break







hillClimb(dros, mir, pos_swaps)



