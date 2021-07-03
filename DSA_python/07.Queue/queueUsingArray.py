class Queue:
    def __init__(self):
        self.__array=[]
        self.__size=0

    def enqueue(self,item):
        self.__array.append(item)
        self.__size+=1

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        x=self.__array[0]
        self.__array=self.__array[1:]
        self.__size-=1
        return x

    def size(self):
        return self.__size

    def front(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.__array[0]

    def isEmpty(self):
        return self.size()==0


q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.size())
q.dequeue()
print(q.size())
