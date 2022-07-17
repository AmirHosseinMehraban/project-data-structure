from operator import truediv
import sys

class MaxHeap:
    def __init__(self):
        self.Heap=[sys.maxsize]
        self.heap_size=0
        self.FRONT = 1
    def parent(self,pos):
        return pos//2
    def leftChild(self, pos):
        return pos*2
    def rightChild(self, pos):
        return (pos*2)+1
    def size(self):
        return self.heap_size
    def isLeaf(self, pos):
        if pos >= (self.heap_size//2) and pos <= self.heap_size:
            return True
        return False
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos]=self.Heap[spos],self.Heap[fpos]
    def maxHeapify(self, pos): 
        if self.rightChild(pos)<=self.heap_size:

            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                if (self.Heap[self.leftChild(pos)] >self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))


    def insert(self, element):
        self.heap_size+= 1
        self.Heap.append(element)

        current=self.heap_size
        if self.heap_size==1:
            ...
        else:
            while (self.Heap[current] >self.Heap[self.parent(current)]):
                self.swap(current, self.parent(current))
                current = self.parent(current)
    

    def Print(self):

        for i in range(1, (self.heap_size // 2) + 1):
            print("PARENT : " + str(self.Heap[i]) +"LEFT CHILD : " + str(self.Heap[2 * i]) +"RIGHT CHILD : " + str(self.Heap[2 * i + 1]))


    def extractMax(self):
        if self.heap_size<0:
            return
        if len(self.Heap)==1:
            return
        popped = self.Heap[1]
        if len(self.Heap)<=2:
            self.Heap.pop()
        else:
            self.Heap[1] = self.Heap.pop()
        self.heap_size -= 1
        if self.heap_size<0:
            self.heap_size=0
            return
            
        self.maxHeapify(1)

        return popped
    
    def find_max(self):
        if self.heap_size>=1:
            return self.Heap[1]
        return
    
    def clear(self):
        self.Heap.clear()
        self.Heap=[sys.maxsize]
        self.heap_size=0

    def add_to_all(self, number) -> None:
        for i in range(1,len(self.Heap)):
            self.Heap[i]=self.Heap[i]+number

    def bubble_up(self, index):
        buble_array=[]
        x=self.Heap.index(index)
        x=self.parent(x)
        while x!=0:
            buble_array.append(self.Heap[x])
            x=self.parent(x) 
        return buble_array     
maxHeap = MaxHeap()
maxHeap.insert(1)
maxHeap.insert(9)
maxHeap.insert(5)
maxHeap.insert(7)
maxHeap.insert(6)
maxHeap.insert(25)
print(maxHeap.bubble_up(1))

	
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
print("The Max val is " + str(maxHeap.extractMax()))
