from queue import Queue
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inputLevelWise():
    q=Queue()
    root=int(input())
    if root==-1:
        return None
    rootnode=Node(root)
    q.put(rootnode)
    while (not q.empty()):
        data=q.get()
        print("enter left child of :",data.data)
        left=int(input())
        if left!=-1:
            leftnode=Node(left)
            q.put(leftnode)
            data.left=leftnode
        print("enter right child of :", data.data)
        right=int(input())
        if right!=-1:
            rightnode=Node(right)
            q.put(rightnode)
            data.right=rightnode
    return rootnode

b=[]
def findPath(root,item):
    if root==None:
        return None
    if root.data==item:
        print(item,end=" ")
        return True
    left=findPath(root.left,item)
    right=findPath(root.right,item)
    if left or right:
        print(root.data,end=" ")
        return True
    return


root=inputLevelWise()
a=int(input())
findPath(root,a)



