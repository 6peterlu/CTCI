#!/bin/python3

import sys

class Heap:
    def __init__(self, isMinHeap):
        self.numElems = 0
        self.data = ['placeholder']
        self.isMinHeap = isMinHeap
    def insert(self, num):
        self.data.append(num)
        self.upheap(len(self.data) - 1)
        self.numElems += 1
    def remove(self):
        removed = self.data[1]
        self.data[1] = self.data[-1]
        del self.data[-1]
        self.downheap(1)
        self.numElems -= 1
        return removed
    def peek(self):
        return self.data[1]
    def getNumElems(self):
        return self.numElems
    def swap(self, index1, index2):
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp
    def upheap(self, index):
        if index == 1:
            return
        parentindex = index//2
        if self.isMinHeap and self.data[parentindex] <= self.data[index]:
            return
        if not self.isMinHeap and self.data[parentindex] >= self.data[index]:
            return
        self.swap(index, parentindex)
        self.upheap(parentindex)
    def downheap(self, index):
        if index >= len(self.data)/2: # in the last half of array.
            return
        if index * 2 == len(self.data)
        child1 = self.data[index * 2]
        child2 = self.data[index * 2 + 1]
        
        indexlarger = index * 2
        indexsmaller = index * 2 + 1
        if child2 > child1:
            indexlarger = index * 2 + 1
            indexsmaller = index * 2

        if self.isMinHeap:
            if self.data[index] <= self.data[indexsmaller]:
                return
            self.swap(index, indexsmaller)
            self.downheap(indexsmaller)
            return
        
        #maxheap
        if self.data[index] >= self.data[indexlarger]:
            return
        self.swap(index, indexlarger)
        self.downheap(indexlarger)
        return
        
                    
n = int(input().strip())
a_i = 0
maxheap = Heap(False)
minheap = Heap(True)
heapsUneven = False

for a_i in range(n):
    a_t = int(input().strip())
    if maxheap.getNumElems() == 0: # fill max heap first.
        maxheap.insert(a_t)
        print("first element")
        print(a_t)
    elif minheap.getNumElems() == 0:
        print("second element")
        if a_t > maxheap.peek():
            removed = maxheap.remove()
            maxheap.insert(a_t)
            minheap.insert(removed)
        else:
            minheap.insert(a_t)
        print((maxheap.peek() + minheap.peek) / 2)
    else:
        print("minheap peek: " + str(minheap.peek()))
        print("maxheap peek: " + str(maxheap.peek()))
        if heapsUneven: # max heap has an extra.
            if a_t >= maxheap.peek():
                minheap.insert(a_t)
            else:
                removed = maxheap.remove()
                maxheap.insert(a_t)
                minheap.insert(removed)
            print((maxheap.peek() + minheap.peek)/2)
            heapsUneven = False
        else: # heaps are even
            if a_t <= minheap.peek():
                maxheap.insert(a_t)
            else:
                removed = minheap.remove()
                minheap.insert(a_t)
                maxheap.insert(removed)
            print(maxheap.peek())
            heapsUneven = True
        
