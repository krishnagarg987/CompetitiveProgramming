
# -------------------MIN_PRIORITY_QUEUE--------------------------

class pqnode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority

class priorityQueue:
    def __init__(self):
        self.pqarray=[]

    def size(self):
        return len(self.pqarray)

    def isempty(self):
        return self.size()==0

    def __perculateup(self):
        if self.size()==1:
            return
        childIndex=self.size()-1
        while childIndex>0:
            parentIndex = (childIndex - 1) // 2
            if self.pqarray[parentIndex].priority>self.pqarray[childIndex].priority:
                self.pqarray[parentIndex].priority,self.pqarray[childIndex].priority=self.pqarray[childIndex].priority,self.pqarray[parentIndex].priority
                childIndex=parentIndex
            else:
                break

    def insert(self,value,priority):
        node=pqnode(value,priority)
        self.pqarray.append(node)
        self.__perculateup()

    def getmin(self):
        return self.pqarray[0].priority

    def perculatedown(self):
        if self.size()==1:
            return
        parentindex=0
        leftchildindex=parentindex*2+1
        rightchildindex=parentindex*2+2
        while leftchildindex<=(self.size()-1):
            minimumIndex=parentindex
            if rightchildindex<=(self.size()-1) and self.pqarray[rightchildindex].priority<self.pqarray[parentindex].priority:
                minimumIndex=rightchildindex
            if self.pqarray[leftchildindex].priority<self.pqarray[minimumIndex].priority:
                minimumIndex=leftchildindex
            if minimumIndex==parentindex:
                break
            self.pqarray[minimumIndex],self.pqarray[parentindex]=self.pqarray[parentindex],self.pqarray[minimumIndex]
            parentindex = minimumIndex
            leftchildindex = parentindex * 2 + 1
            rightchildindex = parentindex * 2 + 2

    def removemin(self):
        if self.isempty():
            return
        ans=self.getmin()
        self.pqarray[0]=self.pqarray[self.size()-1]
        self.pqarray.pop()
        self.perculatedown()
        return ans

q=priorityQueue()
q.insert(5,5)
print(q.getmin())
q.insert(9,9)
print(q.getmin())
q.insert(1,1)
print(q.getmin())
q.insert(4,4)
print(q.getmin())
q.insert(7,7)
print(q.getmin())
q.insert(10,10)
print(q.getmin())
print('m')
for i in range(6):
    print(q.getmin())
    q.removemin()
print(q.size())

