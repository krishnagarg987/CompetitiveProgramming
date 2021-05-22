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

s = Stack()


