class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    __head=None
    __count=0

    @staticmethod
    def  pop():
        if Stack.isEmpty():
            print("hey! stack is empty")
            return
        data=Stack.__head.data
        Stack.__head=Stack.__head.next
        Stack.__count-=1
        return data

    @staticmethod
    def top():
        if Stack.isEmpty():
            print("hey! stack is empty")
            return
        return Stack.__head.data

    @staticmethod
    def push(element):
        newnode=Node(element)
        newnode.next=Stack.__head
        Stack.__head=newnode
        Stack.__count+=1

    @staticmethod
    def isEmpty():
        return Stack.__head==None

    @staticmethod
    def size():
        return Stack.__count

s=Stack()
s.push(4)
# s.push(5)
# s.pop()
print(s.size())

