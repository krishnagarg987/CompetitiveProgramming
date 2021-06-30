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

    def __hasPathhelper(self,v1,v2,visited):
        if self.__adjacencyMatrix[v1][v2]>0:
            return True
        visited[v1]=True
        haspath=False
        for i in range(self.nVertices):
            if self.__adjacencyMatrix[v1][i]>0 and visited[i] is False:
                ans=self.__hasPathhelper(i,v2,visited)
                if ans:
                    haspath=True
                    break
        return haspath

    def hasPath(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        return self.__hasPathhelper(v1,v2,visited)


g=graph(13)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,5)
g.addEdge(2,4)
g.addEdge(2,6)
g.addEdge(3,7)
g.addEdge(6,12)
g.addEdge(5,8)
g.addEdge(5,9)
g.addEdge(9,11)
g.addEdge(9,10)
print(g.hasPath(1,11))