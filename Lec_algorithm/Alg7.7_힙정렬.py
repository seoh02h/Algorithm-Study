import math


class Heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        # heap size를 하나 줄여야 한다. 인덱스는 1부터. 인덱스의 2* 연산 가능하도록.
        self.n = len(self.data) - 1

    def addElt(self, elt):
        self.data.append(elt)
        self.n = len(self.data) - 1
        self.siftUp(self.n)

    def siftUp(self, i):
        while (i >= 2):
            if (self.data[i] > self.data[math.floor(i / 2)]):
                temp = self.data[math.floor(i / 2)]
                self.data[math.floor(i / 2)] = self.data[i]
                self.data[i] = temp
            i = math.floor(i / 2)

    def siftDown(self,i):
        siftkey = self.data[i]
        parent = i
        spotfound = False
        while(2*parent <= self.n and spotfound==False):
            if(2*parent < self.n and self.data[2*parent] < self.data[2*parent+1]):
               largerchild = 2*parent +1
            else:
               largerchild = 2*parent
            if(siftkey<self.data[largerchild]):
               self.data[parent]=self.data[largerchild]
               parent=largerchild
            else:
               spotfound = True
        self.data[parent]=siftkey

    def makeHeap(self):
        for i in range (math.floor(len(self.data)/2),0,-1):
            self.siftDown(i)

    def root(self):
        keyout = self.data[1]
        self.data[1] = self.data[self.n]
        del self.data[self.n]
        self.n = self.n - 1
        if (self.n > 0):
            # 추가 하였음. 힙 이 더 이상없을 때는 down 없음
            self.siftDown(1)
        return keyout

    def removeKeys(self):
        s = []
        for i in range(self.n, 0, -1):
            a = self.root()
            s.append(a)
        return s


def heapSort(a):
    a = Heap(a)
    a.makeHeap()
    s = a.removeKeys()
    return s

# 인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort(a)
print(s)
