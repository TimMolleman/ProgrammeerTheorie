# importeer random module
import random
import numpy

# define melanogaster
class FruitFlies:
    # initieer drosophila
    def __init__(self):
        # definieer random volgorde 25 genen
        self.dros = random.sample(range(1, 26), 25)
        # definieer genen van miranda 1 tot en met 25
        self.mir = range(1,26)
        # set counter voor inversions
        self.count = 0
        #set counter voor genswaps
        self.countgene = 0
    # pancake sort
    def least_steps(self):
        # itereer over genen
        for x in range(0, 25):
            # zoek het gen in genoom wat op plek x hoort
            for y in range(x, 25):
                # gevonden
                if self.dros[y] == x + 1 and self.dros != self.mir:
                    # flip de genenset zodat gen op juiste plek komt en tel flips
                    self.dros[x:y + 1] = list(reversed(self.dros[x:y + 1]))
                    self.count += 1
                    self.countgene += ((y + 1) - x)
        return (self.countgene, self.count)
    # bubble sort (kleinste inversies)
    def BubbleSort(self):
        # wanneer nog niet opgelost
        while self.dros != self.mir:
            # itereer 25 keer over alle genen
            for x in range(0, 25):
                for y in range(0, 24):
                    # als gen getal hoger is dan de volgende
                    if self.dros[y] > self.dros[y + 1]:
                        # flip het gen en volgende gen
                        self.dros[y:y + 2] = list(reversed(self.dros[y:y + 2]))
                        # tel inversies en genswaps
                        self.countgene += 2
                        self.count += 1
        return (self.countgene, self.count)
    # double pancake
    def new_least_steps(self):
        # set end and start of genome
        self.end = 25
        self.start = 1
        # iterate over de genen
        for x in range(0, 25):
            for y in range(x, 25):
                # als het gen aan het einde hoort flip en set nieuw eind
                if self.dros[y] == self.end and self.dros != self.mir:
                    self.dros[y: self.end] = list(reversed(self.dros[y: self.end]))
                    self.count += 1
                    self.countgene += (self.end - y)
                    self.end -= 1
                # als het gen aan het begin hoort flip en set nieuw begin
                elif self.dros[y] == self.start and self.dros != self.mir:
                    self.dros[self.start - 1: y + 1] = list(reversed(self.dros[self.start - 1: y + 1]))
                    self.count += 1
                    self.countgene += ((y + 1) - (self.start - 1))
                    self.start += 1
        return (self.count, self.countgene)
# av_trials = []
#
# for i in range(100):
#     fly = FruitFlies()
#     fly_count = fly.least_steps()
#     av_trials.append(fly_count)
#
# print numpy.mean(av_trials)

f = FruitFlies()
fly_count2 = f.BubbleSort()
print fly_count2