class Stack:
    def __init__(self):
        self.__array = []

    def push(self,element):
        self.__array.append(element)

    def pop(self):
        if self.isEmpty():
            print("hey! stack is empty")
            return None
        element=self.__array.pop()
        return element

    def size(self):
        return len(self.__array)

    def top(self):
        if self.isEmpty():
            print("Hey! stack is empty")
            return None
        return self.__array[len(self.__array) - 1]

    def isEmpty(self):
        return self.size()==0

class Queue:
    def __init__(self):
        self.__s1=Stack()
        self.__s2=Stack()
        self.__count=0
        self.__front=None

    def enqueue(self,item):
        if self.size()==0:
            self.__front=item
        self.__s1.push(item)
        self.__count += 1

    def dequeue(self):
        if self.__s1.size()==0:
            return
        while self.__s1.size()>1:
            x=self.__s1.pop()
            self.__s2.push(x)
        item=self.__s1.pop()
        self.__front=self.__s2.top()
        while self.__s2.isEmpty() is False:
            x=self.__s2.pop()
            self.__s1.push(x)
        self.__count-=1
        return item

    def size(self):
        return self.__s1.size()

    def isEmpty(self):
        return self.__s1.size()==0

    def front(self):
        if self.__s1.size()==0:
            return
        return self.__front


q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.size(),q.front(),q.isEmpty())
q.dequeue()
q.dequeue()
q.dequeue()
print(q.size(),q.front(),q.isEmpty())