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

def binarySearchTree(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    elif root.data>x:
        return binarySearchTree(root.left,x)
    elif root.data<x:
        return binarySearchTree(root.right,x)



root=inputLevelWise()
print("enter item to search")
item=int(input())
print(binarySearchTree(root,item))
