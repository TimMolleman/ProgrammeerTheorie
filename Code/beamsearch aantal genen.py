import copy
import random
import numpy as np
import time

start_time = time.time()

# functie kiest bepaald aantal children
def choose_children(children, percentage):
    scores = []

    for child in children:
        score = 0
        child = child[0]
        for i in range(len(child)):
            # if i < 2 or i > 21:
            #     if child[i] != i + 1:
            #         score += 1000
            # if i < (len(child) - 1):
            #         if child[i] + 1 == child[i + 1]:
            #             score -= 1.5
            #         elif child[i] - 1 == child[i + 1]:
            #             score -= 1.5
            for j in range(len(mir)):
                if mir[j] == child[i]:
                    if j > i:
                        bad = j - i
                    elif j < i:
                        bad = i - j
                    else:
                        bad = 0
                    score += bad
        scores.append(score)

    arr = np.array(scores)
    amount = 70

    sort_ar = arr.argsort()[:amount].tolist()

    child_ar = []
    for i in sort_ar:
        child_ar.append(children[i])
    return child_ar

mir = range(1, 26)

def bestFirst(mir):

        # maak archief om de nodes op te slaan waarvan al kinderen zijn gemaakt
        archive = []

        # waarde van de eerste node
        # dros = [[23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9], 0]
        dros = [random.sample(range(1, 26), 25), 0]

        # geef het aantal mogelijke swaps voor een array
        swaps = 0
        num = 1
        for i in range(len(dros[0]) - 1):
            swaps += len(dros[0]) - num
            num += 1

        # maak de eerste node aan (de dros) en sla op in archief
        currentnodes = [dros]
        back_up1 = copy.deepcopy(currentnodes[0])
        archive.append(back_up1[0])

        # maak een counter om aantal stappen te tellen van drosophila naar miranda
        counter = 0
        #all(item != mir for item in currentnodes)
        # blijf runnen tot een van de drosophilas gelijk is aan de miranda
        while True:

            # state = False

            for currentnode in currentnodes:
                if currentnode[0] == mir:
                    print currentnode[0], "end array"
                    print currentnode[1], "number of gen swaps"
                    return currentnode[1]
                    # state = True

            # if state:
            #     break

            # maak array om child nodes in op te slaan van de currentnodes
            children = []

            # maak voor elke currentnode in currentnodes alle kinderen en sla deze op
            for currentnode in currentnodes:
                right = 1
                left = 0
                for x in range(0, swaps):
                    currentnode[0][left:right + 1] = list(reversed(currentnode[0][left:right + 1]))
                    num_swaps = len(currentnode[0][left:right + 1])
                    back_up = copy.deepcopy(currentnode[0])
                    state = False # houdt 'false' als child niet in archief
                    for y in archive:
                        if back_up == y:
                            state = True # maak state 'true' als child wel in archief
                            break
                    if state == False:
                        children.append([back_up, num_swaps + currentnode[1]])
                    currentnode[0][left:right + 1] = list(reversed(currentnode[0][left:right + 1]))
                    right += 1
                    if right == len(dros[0]):
                        left += 1
                        right = left + 1

            # maak arrays aan voor nieuwe currentnodes en array voor score
            currentnodes = []

            children1 = choose_children(children, 0.1)

            for child in children1:
                currentnodes.append(child)

            # sla al deze instanties op in het archief zodat ze niet nog een keer bereikt worden
            for i in currentnodes:
                back_up2 = copy.deepcopy(i[0])
                archive.append(back_up2)

            # laat de counter voor aantal swaps met 1 toenemen
            counter += 1

        # return counter

# run = bestFirst(mir)

count_total = []
count1 = 0
for i in range(100):
    count1 += 1
    print count1, "count"
    count_total.append(bestFirst(mir))
    print count_total


av_swaps = np.mean(count_total)
print av_swaps

time_sec = ("--- %s seconds ---" % (time.time() - start_time))
time_min = ("--- %s minutes ---" % ((time.time() - start_time) / 60))
print time_sec
print time_min

