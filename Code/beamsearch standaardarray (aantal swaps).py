import copy
import random
import numpy

# dros arrays
dros = random.sample(range(1, 26), 25)
mir = range(1, 26)

# geef het aantal mogelijke swaps voor een array
pos_swaps = 0
num = 1
for i in range(len(dros) - 1):
    pos_swaps += len(dros) - num
    num += 1

# def hillClimb(dros, mir, swaps):
#
#     # create the first node
#     currentnode = dros
#     back_up1 = copy.deepcopy(currentnode)
#     archive.append(back_up1)
#     counter = 0
#
#     while (currentnode != mir):
#
#         # create child nodes
#         children = []
#         right = 1
#         left = 0
#         for x in range(0, swaps):
#             currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
#             back_up = copy.deepcopy(currentnode)
#             state = False # houdt false als currentnode niet in archief
#             for y in archive:
#                 if back_up == y:
#                     state = True # maak state true als currentnode wel in archief
#                     break
#             if state == False:
#                 children.append(back_up)
#             currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
#             right += 1
#             if right == len(dros):
#                 left += 1
#                 right = left + 1
#
#         array_right = []
#
#         # vul een array met hoeveel posities elke in vergelijking heeft met mir
#         for child in children:
#             right_place = 0
#             count = 0
#             for j in child:
#                 if j == mir[count]:
#                     right_place +=1
#                     count += 1
#                 else:
#                     count += 1
#             array_right.append(right_place)
#         # print array_right
#
#         # selecteer de array die meeste elementen op hun plek hebben
#         max_index = array_right.index(max(array_right))
#
#         # verander de huidige currentnode voor array met meeste elementen op juiste plek
#         currentnode = children[max_index]
#
#         # maak hier backup van
#         back_up2 = copy.deepcopy(currentnode)
#
#         # voeg deze backup toe aan het archief
#         archive.append(back_up2)
#         counter += 1
#         print counter
#

def bestFirst(mir, swaps):

        # maak archief om de nodes op te slaan waarvan al kinderen zijn gemaakt
        archive = []

        # maak de eerste node aan (de dros) en sla op in archief
        dros = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
        currentnodes = [dros]
        back_up1 = copy.deepcopy(currentnodes)
        archive.append(back_up1)

        # maak een counter om aantal stappen te tellen van drosophila naar miranda
        counter = 0

        # blijf runnen tot een van de drosophilas gelijk is aan de miranda
        while all(item != mir for item in currentnodes):

            # maak array om child nodes in op te slaan van de currentnodes
            children = []

            # maak voor elke currentnode in currentnodes alle kinderen en sla deze op
            for currentnode in currentnodes:
                right = 1
                left = 0
                for x in range(0, swaps):
                    currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
                    back_up = copy.deepcopy(currentnode)
                    state = False # houdt 'false' als child niet in archief
                    for y in archive:
                        if back_up == y:
                            state = True # maak state 'true' als child wel in archief
                            break
                    if state == False:
                        children.append(back_up)
                    currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
                    right += 1
                    if right == len(dros):
                        left += 1
                        right = left + 1

            # maak arrays aan voor nieuwe currentnodes en array voor score
            currentnodes = []

            '''
            Kijken hoeveel elementen er al gesorteerd naast elkaar staan (zowel oplopend als aflopend)
            en laat score ook toenemen als elementen al op hun goede plek staan
            '''
            scores = []
            # vul array met scores voor elke child op basis van formule
            for child in children:
                score = 0
                score2 = 1
                for i in range(len(child)):

                    if i < (len(child) - 1):
                        # score +1 als volgende element huidige element +1 of -1 is
                        if child[i] + 1 == child[i + 1] or child[i] - 1 == child[i + 1]:
                            score += 0.1
                            score2 += 1

                        else:
                            score2 = 1
                        # 0.05 score erbij als een element op de goede plek staat
                    if child[i] == mir[i]:
                        score += 0.01


                scores.append(score)

            # vindt indices van de max score
            m1 = max(scores)
            max_indices1 = [i for i, j in enumerate(scores) if j >= m1 - 0.05 ]

            # selecteer alle instanties in children met de hoogste score
            for i in max_indices1:
                currentnodes.append(children[i])
            print counter, currentnodes

            # sla al deze instanties op in het archief zodat ze niet nog een keer bereikt worden
            for i in currentnodes:
                back_up2 = copy.deepcopy(i)
                archive.append(back_up2)

            # laat de counter voor aantal swaps met 1 toenemen
            counter += 1
        return counter
run = 0
for x in range(1):
    run += bestFirst(mir, pos_swaps)
    if x % 10 == 0:
        print run
print run/10.0

# count_total = []
# for i in range(100):
#     run = 0
#     run = bestFirst(mir, pos_swaps)
#     count_total.append(run)
#
# av_swaps = numpy.mean(count_total)
# print av_swaps




   # # maak de eerste node aan (de dros) en sla op in archief
   #  currentnodes = [dros]
   #  back_up1 = copy.deepcopy(currentnodes)
   #  archive.append(back_up1)
   #
   #  # maak een counter om aantal stappen te tellen van drosophila naar miranda
   #  counter = 0
   #
   #  # blijf runnen tot een de drosophila gelijk is aan de miranda
   #  while all(item != mir for item in currentnodes):
   #
   #      # maak array om child nodes in op te slaan van de currentnodes
   #      children = []
   #
   #      # maak voor elke currentnode in currentnodes alle kinderen en sla deze op
   #      for currentnode in currentnodes:
   #          right = 1
   #          left = 0
   #          for x in range(0, swaps):
   #              currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
   #              back_up = copy.deepcopy(currentnode)
   #              state = False # houdt 'false' als child niet in archief
   #              for y in archive:
   #                  if back_up == y:
   #                      state = True # maak state 'true' als child wel in archief
   #                      break
   #              if state == False:
   #                  children.append(back_up)
   #              currentnode[left:right + 1] = list(reversed(currentnode[left:right + 1]))
   #              right += 1
   #              if right == len(dros):
   #                  left += 1
   #                  right = left + 1
   #
   #      # maak arrays aan voor nieuwe currentnodes en array voor score
   #      currentnodes = []
   #
   #      '''
   #      Kijken hoeveel elementen er al gesorteerd naast elkaar staan (zowel oplopend als aflopend)
   #      en laat score ook toenemen als elementen al op hun goede plek staan
   #      '''
   #      scores = []
   #      # vul array met scores voor elke child op basis van formule
   #      for child in children:
   #          score = 0
   #          for i in range(len(child)):
   #              if i < (len(child) - 1):
   #                  # score +1 als volgende element huidige element +1 of -1 is
   #                  if child[i] + 1 == child[i + 1] or child[i] - 1 == child[i + 1]:
   #                      score += 1
   #                  # 0.05 score erbij als een element op de goede plek staat
   #              if child[i] == mir[i]:
   #                  score += 0.05
   #          scores.append(score)
   #
   #      # vindt indices van de max score
   #      m1 = max(scores)
   #      max_indices1 = [i for i, j in enumerate(scores) if j == m1]
   #
   #      # selecteer alle instanties in children met de hoogste score
   #      for i in max_indices1:
   #          currentnodes.append(children[i])
   #
   #      # sla al deze instanties op in het archief zodat ze niet nog een keer bereikt worden
   #      for i in currentnodes:
   #          back_up2 = copy.deepcopy(i)
   #          archive.append(back_up2)
   #
   #      # laat de counter voor aantal swaps met 1 toenemen
   #      counter += 1
   #      print counter
   #      print "counter"

        # '''
        # Maximum aantal elementen op goede plaats als score
        # '''
        # array_right = []
        # # vul een array met hoeveel posities elke in vergelijking heeft met mir
        # for child in children:
        #     right_place = 0
        #     count = 0
        #     for j in child:
        #         if j == mir[count]:
        #             right_place +=1
        #             count += 1
        #         else:
        #             count += 1
        #     array_right.append(right_place)
        # print array_right

        # # selecteer de arrays die meeste elementen op de goede plek hebben
        # m = max(array_right)
        # max_indices = [i for i, j in enumerate(array_right) if j == m]
        #
        # # selecteer alle instanties in children met het maximale aantal elementen op goede plek
        # for i in max_indices:
        #     currentnodes.append(children[i])
        #
        # # sla al deze instanties op in het archief zodat ze niet nog een keer bereikt worden
        # for i in currentnodes:
        #     back_up2 = copy.deepcopy(i)
        #     archive.append(back_up2)
        #
        # # laat de counter voor aantal swaps met 1 toenemen
        # counter += 1
        # # print counter




