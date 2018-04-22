import numpy as np
import random

class HeapBuilder(object):

    def __init__(self, array_length):
        self._heap = np.random.permutation(np.arange(1,array_length+1))
        self.size = len(self._heap)
    def _parent(self, i):
        return (i - 1) // 2

    def _leftChild(self, i):
        return 2 * i + 1

    def _rightChild(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        temp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = temp

    def _siftUp(self, i):
        while (i > 0) and (self._heap[self._parent(i)] < self._heap[i]):
            self._swap(i, self._parent(i))
            i = self._parent(i)
            
    def _siftDown(self, i, size):
        maxindex = i
        l = self._leftChild(i)
        if (l < size) and (self._heap[l] > self._heap[maxindex]):
            maxindex = l
        
        r = self._rightChild(i)
        if (r < size) and (self._heap[r] > self._heap[maxindex]):
            maxindex = r

        if i != maxindex:
            self._swap(i, maxindex)
            self._siftDown(maxindex, size)

    def buildHeap(self):
        for i in reversed(range(0, self._parent(self.size))):
            self._siftDown(i, self.size)

    def heapSort(self):
        self.buildHeap()
        n = self.size
        for _ in range(self.size):
            self._swap(0, n - 1)
            n -= 1
            self._siftDown(0, n)
    def showHeap(self):
        print (self._heap)

if __name__ == '__main__':
    heap = HeapBuilder(1000)
    heap.showHeap()
    heap.heapSort()
    heap.showHeap()
            
