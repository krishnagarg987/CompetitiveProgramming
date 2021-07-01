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

    def __isConnectedHelper(self,sv,visited):
        visited[sv]=True
        for i in range(self.nVertices):
            if self.__adjacencyMatrix[sv][i]>0 and visited[i] is False:
                self.__isConnectedHelper(i,visited)

    def isConnected(self):
        sv=0
        visited=[False for i in range(self.nVertices)]
        self.__isConnectedHelper(sv,visited)
        return visited.count(False)==0


    def __str__(self):
        return str(self.__adjacencyMatrix)


g=graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,5)
print(g.isConnected())
