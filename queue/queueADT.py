class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def enQueue(self,data):
        newNode=Node(data)
        if self.front is None:
            self.front=newNode
        if self.rear is None:
            self.rear=self.front
        else:
            self.rear.next=newNode
            self.rear=newNode
        self.size+=1

    def deQueue(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        if self.front.next is None:
            self.front=None
            self.rear=None
        else:
            result=self.front
            self.front=self.front.next
            del result
        self.size-=1

    def print(self):
        temp=self.front
        if temp is None:
            print("Queue is empty!")
        while(temp is not None):
            print(temp.data,end=' ')
            temp=temp.next
        print()

