from queue import Queue
class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]

def printTree(root):
    if root==None:
        return
    print(root.data,":",end=" ")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree(child)

def inputTree():
    print("enter root data")
    rootdata=int(input())
    if rootdata==None:
        return None
    root=Node(rootdata)
    print("enter number of nodes of",rootdata)
    numchild=int(input())
    for i in range(numchild):
        root.children.append(inputTree())
    return root

def noOfNodes(root):
    if root==None:
        return 0
    x=0
    for child in root.children:
        x+=noOfNodes(child)
    return x+1

def inputTreeLevelWise():
    print("enter root data")
    data=int(input())
    if data==None:
        return
    q = Queue()
    root=Node(data)
    q.put(root)
    while q.empty() is False:
        front=q.get()
        print("enter no. of child of ",front.data)
        childs=int(input())
        for i in range(childs):
            x=int(input())
            childnode=Node(x)
            q.put(childnode)
            front.children.append(childnode)
    return  root

def printLevelWise(root):
    if root==None:
        return
    q = Queue()
    q.put(root)
    while q.empty() is False:
        front=q.get()
        print(front.data,end=":")
        for child in front.children:
            q.put(child)
            print(child.data,end=",")
        print()



root=inputTreeLevelWise()
# printTree(root)
printLevelWise(root)
print(noOfNodes(root))