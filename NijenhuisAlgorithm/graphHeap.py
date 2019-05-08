class MikesGraphHeap:
    """
    Heap that stores nodes with associated keys
    takes as input node = (label, key), key value for node is node[1]
    *Doesn't actually need to be a graph
    was created by adapting 'MikesFirstHeap' in heap.py, modifying all pionts of key comparison
    Something is wrong with this heap because it doesn't work for Primm's algorithm like heapq does
    """
    def __init__(self):
        self.heapList = [(0, 0)]
        self.currentSize = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heapList[i][1] < self.heapList[i // 2][1]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)

    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.min_child(i)
            if self.heapList[i][1] > self.heapList[mc][1]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2][1] < self.heapList[i*2+1][1]:
                return i * 2
            else:
                return i * 2 + 1

    def extract_min(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.perc_down(1)
        return retval

    def delete(self, node):
        i = self.heapList.index(node)
        self.heapList[i] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.perc_down(i)

    def heapify(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1
