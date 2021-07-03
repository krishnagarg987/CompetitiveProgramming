class edge:
    def __init__(self,source,destination,weight):
        self.source=source
        self.destination=destination
        self.weight=weight

    def __lt__(self, other):
        return self.weight<other.weight

def getParent(v,parent):
    if v==parent[v]:
        return v
    return getParent(parent[v],parent)

def kruskalAlgo(vertices,edges):
    parentArray = [i for i in range(vertices)]
    count = 0
    i = 0
    output = []
    while count < (vertices - 1):
        v1 = edges[i].source
        v2 = edges[i].destination
        p1 = getParent(v1,parentArray)
        p2 = getParent(v2,parentArray)
        if p1 !=p2:
            count += 1
            parentArray[p2] =p1
            output.append(edges[i])
        i+=1
    return output

vertices,edgeCount=map(int,input().split())
edges=[]
for i in range(edgeCount):
    source,destination,weight=map(int,input().split())
    edges.append(edge(source,destination,weight))
edges.sort()
output=kruskalAlgo(vertices,edges)
for i in output:
    print(i.source,i.destination,i.weight)

# 6 11
# 0 1 1
# 0 2 5
# 2 3 10
# 0 3 4
# 1 3 3
# 1 2 6
# 3 4 7
# 2 4 8
# 4 5 2
# 2 5 9
# 3 5 6