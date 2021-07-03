import sys


class graph:
    def __init__(self,nvertices):
        self.nvertices=nvertices
        self.adjacencyMatrix=[[0 for i in range(nvertices)] for j in range(nvertices)]

    def addEdge(self,v1,v2,wt):
        self.adjacencyMatrix[v1][v2]=wt
        self.adjacencyMatrix[v2][v1]=wt

    def __getMinVertex(self,visited,weight):
        minVertex=-1
        for i in range(self.nvertices):
            if visited[i] is False and (weight[minVertex]>weight[i] or minVertex==-1):
                minVertex=i
        return minVertex

    def prims(self):
        visited=[False for i in range(self.nvertices)]
        parent=[-1 for i in range(self.nvertices)]
        weight=[sys.maxsize for i in range(self.nvertices)]
        weight[0]=0
        for i in range(self.nvertices-1):
            minVertex=self.__getMinVertex(visited,weight)
            visited[minVertex]=True
            for j in range(self.nvertices):
                if self.adjacencyMatrix[minVertex][j]>0 and visited[j] is False:
                    if weight[j]>self.adjacencyMatrix[minVertex][j]:
                        weight[j]=self.adjacencyMatrix[minVertex][j]
                        parent[j]=minVertex
        for i in range(1,self.nvertices):
            print(i,parent[i],weight[i])

vertices,edgecount=map(int,input().split())
g=graph(vertices)
for i in range(edgecount):
    v1,v2,wt=map(int,input().split())
    g.addEdge(v1,v2,wt)
g.prims()
