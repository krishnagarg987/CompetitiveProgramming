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

def itemBwK1_K2(root,k1,k2):
    if root==None:
        return
    if root.data<k1:
        itemBwK1_K2(root.right,k1,k2)
    elif root.data>k2:
        itemBwK1_K2(root.left,k1,k2)
    elif root.data>=k1 and root.data<=k2:
        print(root.data,end=" ")
        itemBwK1_K2(root.left,k1,k2)
        itemBwK1_K2(root.right,k1,k2)

root=inputLevelWise()
print("enter k1 and k2")
k1,k2=map(int,input().split())
itemBwK1_K2(root,k1,k2)