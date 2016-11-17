# importeer random module
import random
import numpy

# define melanogaster
class FruitFlies:
    def __init__(self):
        self.dros = random.sample(range(1, 26), 25)
        self.mir = range(1,26)
        self.count = 0
    def least_steps(self):
        for x in range(0, 25):
            for y in range(x, 25):
                if self.dros[y] == x + 1 and self.dros != self.mir:
                    self.dros[x:y + 1] = list(reversed(self.dros[x:y + 1]))
                    self.count += 1
        return self.count
    def BubbleSort(self):
        print self.dros
        while self.dros != self.mir:
            for x in range(0, 25):
                for y in range(0, 24):
                    if self.dros[y] > self.dros[y + 1]:
                        self.dros[y:y + 2] = list(reversed(self.dros[y:y + 2]))
                        print self.dros
                        self.count += 2
        return self.count
    def new_least_steps(self):
        self.end = 25
        self.start = 1
        for x in range(0, 25):
            for y in range(x, 25):
                if self.dros[y] == self.end and self.dros != self.mir:
                    self.dros[y: self.end] = list(reversed(self.dros[y: self.end]))
                    self.count += 1
                    self.end -= 1
                elif self.dros[y] == self.start and self.dros != self.mir:
                    self.dros[self.start - 1: y + 1] = list(reversed(self.dros[self.start - 1: y + 1]))
                    self.count += 1
                    self.start += 1
        return self.count
# av_trials = []
#
# for i in range(100):
#     fly = FruitFlies()
#     fly_count = fly.least_steps()
#     av_trials.append(fly_count)
#
# print numpy.mean(av_trials)

f = FruitFlies()
fly_count2 = f.new_least_steps()
print fly_count2