import sys


class graph:
    def __init__(self,vertices):
        self.nvertices=vertices
        self.adjacencyMatrix=[[0 for i in range(vertices)] for j in range(vertices)]\

    def addEdge(self,v1,v2,distance):
        self.adjacencyMatrix[v1][v2]=distance
        self.adjacencyMatrix[v2][v1]=distance

    def __getMinVertex(self,visited,distance):
        minVertex=-1
        for i in range(self.nvertices):
            if visited[i] is False and (minVertex==-1 or distance[i]<minVertex):
                minVertex=i
        return  minVertex

    def dijkistra(self):
        visited=[False for i in range(self.nvertices)]
        distance=[sys.maxsize for i in range(self.nvertices)]
        distance[0]=0
        for i in range(self.nvertices):
            minVertex=self.__getMinVertex(visited,distance)
            visited[minVertex]=True
            for j in range(self.nvertices):
                if self.adjacencyMatrix[minVertex][j]>0 and visited[j] is False:
                    if distance[minVertex]+self.adjacencyMatrix[minVertex][j]<distance[j]:
                        distance[j]=distance[minVertex]+self.adjacencyMatrix[minVertex][j]
        for i in range(self.nvertices):
            print(0,i,distance[i])


vertices,edgeCount=map(int,input().split())
g=graph(vertices)
for i in range(edgeCount):
    v1,v2,dist=map(int,input().split())
    g.addEdge(v1,v2,dist)
g.dijkistra()

# 5 7
# 0 1 4
# 0 2 8
# 1 2 2
# 1 3 5
# 2 3 5
# 2 4 9
# 3 4 4