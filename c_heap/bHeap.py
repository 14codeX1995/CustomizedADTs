class Heap:
    def __init__(self):
        self.heapList=[]
        self.size=0

    #for a node at ith location its parent is at (i-1)/2
    def parent(self,index):
        return (index-1)//2

    def leftChild(self,index):
        return (2*index)+1

    def rightChild(self,index):
        return (2*index)+2
    #returns max element of the heap
    def getMax(self):
        if self.size==0:
            return -1
        else:
            return self.heapList[0]

    def getMin(self):
        if self.size==0:
            return -1
        else:
            return self.heapList[0]

    def minChild(self,i):
        if 2*i+2>self.size:
            return 2*i
        else:
            if self.heapList[2*i+1]<self.heapList[2*i+2]
                return 2*i+1
            else:
                return 2*i+2

    def percolateDown(self,i):
        while 2*i+1<=self.size:
            minimumChild=self.minChild(i)
            if self.heapList[i]>self.heapList[minimumChild]:
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[minimumChild]
                self.heapList[minimumChild]=tmp
            i=minimumChild

    def percolateUp(self,i):
        while i-1//2>0:
            if self.heapList[i]<self.heapList[i-1//2]:
                tmp=self.heapList[i-1//2]
                self.heapList[i-1//2]=self.heapList[i]
                self.heapList[i-1//2]=tmp
            i=i-1//2



