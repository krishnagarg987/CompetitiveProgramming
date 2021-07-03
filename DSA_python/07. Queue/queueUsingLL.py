class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class Queue:
    def __init__(self):
        self.__head=None
        self.__size=0
        self.__last=None

    def enqueue(self,item):
        newNode=Node(item)
        if self.__head==None:
            self.__head=newNode
            self.__last=newNode
        else:
            self.__last.next=newNode
            self.__last=newNode
        self.__size+=1

    def dequeue(self):
        if self.__head==None:
            print("queue is empty")
            return
        x=self.__head.data
        self.__head=self.__head.next
        self.__size-=1
        return x

    def isEmpty(self):
        return self.size()==0

    def size(self):
        return self.__size

    def front(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.__head.data

q=Queue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
print(q.size(),q.front(),q.isEmpty())
q.dequeue()
q.dequeue()
print(q.size(),q.front(),q.isEmpty())