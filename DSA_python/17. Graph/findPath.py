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

    def __getPathDFSHelper(self,v1,v2,visited):
        if self.__adjacencyMatrix[v1][v2]>0:
            visited[v1]=visited[v2]=True
            return [v2,v1]

        visited[v1]=True
        answer=None
        for i in range(self.nVertices):
            if self.__adjacencyMatrix[v1][i]>0 and visited[i] is False:
                ans=self.__getPathDFSHelper(i,v2,visited)
                if ans==None:
                    continue
                else:
                    answer=ans.copy()
                    answer.append(v1)
        return answer

    def getPath_DFS(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        return self.__getPathDFSHelper(v1,v2,visited)

    def __getPathBFSHelper(self,v1,v2,visited):
        pd={}
        q=Queue()
        q.put(v1)
        visited[v1]=True
        while q.empty() is False:
            el=q.get()
            isFound=False
            for i in range(self.nVertices):
                if self.__adjacencyMatrix[el][i]>0 and visited[i] is False:
                    q.put(i)
                    pd[i] = el
                    if i==v2:
                        isFound=True
                        break
            if isFound:
                break
        el=v2
        path=[v2]
        while el!=v1:
            path.append(pd[el])
            el=pd[el]
        return path


    def getPath_BFS(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        return self.__getPathBFSHelper(v1,v2,visited)


    def __str__(self):
        return str(self.__adjacencyMatrix)


g=graph(6)
# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(1,3)
# g.addEdge(2,3)
# g.addEdge(2,4)
# g.addEdge(3,5)
# print(g.getPath_DFS(0,6))
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,4)
g.addEdge(3,5)
g.addEdge(4,5)
print(g.getPath_BFS(0,5))