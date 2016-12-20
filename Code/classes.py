# importeer random module
import random
import numpy
import copy

# define melanogaster
class FruitFlies:
    # initieer drosophila
    def __init__(self):
        # definieer random volgorde 25 genen
        #self.dros = [3,2,1,6,4,5]
        self.dros = random.sample(range(1, 26), 25)
        #self.dros = [6,7,5,4,3,2,1]
        # definieer genen van miranda 1 tot en met 25
        self.mir = range(1,26)
        # set counter voor inversions
        self.count = 0
        #set counter voor genswaps
        self.countgene = 0
        self.count1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.layer = 0
        self.kitkat = 0
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
            print self.dros
        return (self.count, self.countgene)
    # count possible number of swaps
    def Amount_swaps(self):
        # set counter for possible swaps
        self.pos_swaps = 0
        # set counter for counting swaps
        self.num = 1
        # count and return number of swaps
        for i in range(len(self.dros) - 1):
            self.pos_swaps += len(self.dros) - self.num
            self.num += 1
        return self.pos_swaps
    # gives array of all possible swaps
    def Possible_swaps(self,root, amount_of_pos):
        # initialiseer de grenzen van de array
        self.array = []
        self.right = 1
        self.left = 0
        # doe alle mogelijke swaps voor de huidige 'dros' in array
        for x in range(0, amount_of_pos):
            root[self.left:self.right + 1] = list(reversed(root[self.left:self.right + 1]))
            self.back_up = copy.deepcopy(root)
            self.array.append(self.back_up)
            root[self.left:self.right + 1] = list(reversed(root[self.left:self.right + 1]))
            self.right += 1
            if self.right == len(root):
                self.left += 1
                self.right = self.left + 1

        return self.array


    def brute_force(self, root, mir):
        print "go"
        if self.kitkat == 1:
            return "found"
        self.children = []
        # maak 'dros' de root als er nog geen root is en maak children aan
        if root == 0:
            self.sec_count = 1
            root = self.dros
            self.children = self.Possible_swaps(root, 15)

        # als er al een root is geweest (root == 1), doe onderstaande
        elif root == 1:
            root = self.dros
            self.children = self.Possible_swaps(root, 15)
            for x in range(0, 15):
                if self.count1[x] != 0:
                    self.layer = x
                    print self.layer, "118"
                    if self.count1[x] == 15 and x > 0:
                        self.count[x] = 1
                    for y in range(0, x + 1):
                        #print self.children, "120"
                        root = self.children[self.count1[y] - 1]
                        #print root, "122"
                        self.children = self.Possible_swaps(root, 15)
                        #print self.children
                    break
        else:
            print root, self.mir, "129"
            self.children = self.Possible_swaps(root, 15)


        self.target = mir
        print root, self.children, "dit"
        #print "go", root
        for x in range(0, 15):
            #self.sec_count +=1
            for y in range(0, 15):
                #print self.children[x], self.target[y], "134"
                if self.children[x] == self.mir:
                    print "found", self.children[x]
                    self.count1[self.layer + 1] = x + 1
                    print self.count1
                    self.kitkat = 1
                    return self.count1
                elif self.children[x] == self.target[y]:
                    print "love bottem up", self.layer, self.children[x], self.target[y]
                    self.count1[self.layer + 1] = x + 1
                    self.layer += 1
                    self.brute_force(self.children[x], mir)
                else:
                    self.countgene += 1
        self.count1[self.layer] += 1
        self.layer += 1
        print self.count1, "155", self.layer
        self.brute_force(1, mir)
                    # print "wtf"

class Miranda:
    def __init__(self):
        self.mir = range(1,7)
    def Possible_swaps(self, amount_of_pos):
        # initialiseer de grenzen van de array
        self.array = []
        self.right = 1
        self.left = 0
        # doe alle mogelijke swaps voor de huidige 'dros' in array
        for x in range(0, amount_of_pos):
            self.mir[self.left:self.right + 1] = list(reversed(self.mir[self.left:self.right + 1]))
            self.back_up = copy.deepcopy(self.mir)
            self.array.append(self.back_up)
            self.mir[self.left:self.right + 1] = list(reversed(self.mir[self.left:self.right + 1]))
            self.right += 1
            if self.right == len(self.mir):
                self.left += 1
                self.right = self.left + 1
        return self.array


total = []
for i in range(1000):
    f = FruitFlies()
    shit = f.new_least_steps()
    total.append(shit[1])
print numpy.mean(total)

