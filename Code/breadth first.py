# importeer random module
import random
import copy
import csv

csvFile = open("csv.csv", "w")
wr = csv.writer(csvFile)

csvkid = open("kid.csv", "w")
wrkid = csv.writer(csvkid)

csvtrack = open("track.csv", "w")
wrtrack = csv.writer(csvtrack)

# define melanogaster
class FruitFlies:
    # initieer drosophila
    def __init__(self):
        # definieer random volgorde 25 genen
        self.dros = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
        # set counter voor inversions
        self.count = 0
        #set counter voor genswaps
        self.countgene = 0
        self.mir = range(1, 25)
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
        self.end = 5
        self.start = 1
        # iterate over de genen
        for x in range(0, 5):
            for y in range(x, 5):
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
            q.enqueue(self.back_up, root)
            self.right += 1
            if self.right == len(root):
                self.left += 1
                self.right = self.left + 1
        return self.array

    def broadth_first(self):
        #print self.dros
        Queue.enqueue(q, self.dros, 0)
        while True:
            if q.check() == 1:
                print "found"
                break
            elif q.check() == 2:
                #print q.items[len(q.items) - 1], "deze gaat vast wel goed jo"
                return q.items[len(q.items) - 1]
            else:
                self.root = q.items[len(q.items) - 1]
                #print self.root, "111"
                q.dequeue()
                #print q.items, "113"
                self.Possible_swaps(self.root, 300)
                #print len(q.items), "115"




                #print self.counterr

class Queue:
    def __init__(self):
        self.count1 = 0
        self.items = []
        self.kid = []
        self.track = []
        self.archive = set()
        self.count = 0

    def enqueue(self, item, root):
        self.length_1 = len(self.archive)
        str1 = int(''.join(map(str,item)))
        self.archive.add(str1)
        self.length_2 = len(self.archive)
        if self.length_1 != self.length_2:
            self.items.insert(0, item)
            self.track.insert(0, root)
            self.kid.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def check(self):
        if self.items[len(self.items) - 1] == range(1, 26):
            print self.items[len(self.items) - 1], "kijk ik heb m", len(self.items)
            return 1
        for x in range(len(qt.items)):
            if self.items[len(self.items) - 1] == qt.items[x]:
                return 2
        else:
            return 0
    def path(self, cross):
        if self.count1 == 0:
            self.pathswaps = []
            self.pathswaps.append(cross)
            #print cross, "root"
            self.count1 += 1
        for x in range(len(self.kid)):
            if self.kid[x] == cross and self.pathswaps[len(self.pathswaps) - 1] != 0:
                #print "kiddo"
                if self.track[x] == 0:
                    print self.track[0], "echt hoe komt deze null hier"
                    self.pathswaps.append([0])
                    #print self.track[x], "jeej"
                    print self.pathswaps, "pathswaps"
                    return self.pathswaps
                else:
                    #print self.track[x], "path"
                    self.pathswaps.append(self.track[x])
                    self.path(self.track[x])






class Miranda:
    def __init__(self):
        self.mir = range(1,26)
    def Possible_swaps(self,root, amount_of_pos):
        # initialiseer de grenzen van de array
        self.array = []
        self.right = 1
        self.left = 0
        # doe alle mogelijke swaps voor de huidige 'dros' in array
        for x in range(0,  300):
            root[self.left:self.right + 1] = list(reversed(root[self.left:self.right + 1]))
            self.back_up = copy.deepcopy(root)
            self.array.append(self.back_up)
            root[self.left:self.right + 1] = list(reversed(root[self.left:self.right + 1]))
            qt.enqueue(self.back_up, root)
            #print len(qt.items)
            self.right += 1
            if self.right == len(self.mir):
                self.left += 1
                self.right = self.left + 1
        #print "done with mir"
        return self.array
    def target_queue(self):
        qt.enqueue(self.mir, 0)
        for x in range(10000):
            if x % 100 == 0:
                 print len(qt.items)
            self.root = qt.items[len(qt.items) - 1]
            qt.dequeue()
            self.Possible_swaps(self.root, 300)
            #print len(qt.items), x
        print "done with mir", qt.items[10]
        #wr.writerows(qt.items)
        #wrkid.writerows(qt.kid)
        print qt.track[15], "ging wel nog"
        #wrtrack.writerows(qt.track)



back = []
q = Queue()
qt = Queue()
g = Queue()
dros = FruitFlies()
mir = Miranda()
mir.target_queue()
print dros.Amount_swaps()
#with open("csv.csv", "rb") as f:
 #   reader = csv.reader(f)
  #  for row in reader:
   #     for char in row:
    #        print char, type(char)
     #       print int(char), type(int(char))
      #      back.insert(len(back), int(char))
       # g.items.insert(0, back)
        #back = []
#print g.items[len(g.items) - 11],qt.items[10],"werkt de csv"
x = dros.broadth_first()
print x, "x"
y = qt.path(x)
z =  q.path(x)
print y, "richting mir"
#dros.broadth_first()
print dros.dros




