# initialize the first node
dros = [3, 5, 2, 4, 1]

# class TrieNode:
#
#     def __init__(self, in_data):
#         self.data = in_data
#         self.pointers={}

class Trie:

    def __init__(self, fly):
        self.root = fly
    def swapamount(self):
        pos_swaps = 0
        num = 1
        for i in range(len(self.root) - 1):
            pos_swaps += len(self.root) - num
            num += 1
        return pos_swaps

shit = Trie(dros)
print shit.swapamount()
