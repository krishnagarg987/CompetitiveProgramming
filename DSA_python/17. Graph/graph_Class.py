from queue import Queue
class graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.__adjacencyMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.__adjacencyMatrix[v1][v2]=1
        self.__adjacencyMatrix[v2][v1]=1

    def removeEdge(self,v1,v2):
        if not self.containsEdge(v1,v2):
            return
        self.__adjacencyMatrix[v1][v2]=0
        self.__adjacencyMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        return True if self.__adjacencyMatrix[v1][v2]>0 else False

    def __str__(self):
        return str(self.__adjacencyMatrix)


g=graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)
print(g)
