from queue import Queue
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printTreeLevelWise(root):
    q=Queue()
    if root==None:
        return None
    q.put(root)
    while (not q.empty()):
        node=q.get()
        print(node.data,end=":")
        if node.left!=None:
            print('L',node.left.data,end=',')
            q.put(node.left)
        if node.right!=None:
            print('R',node.right.data,end='')
            q.put(node.right)
        print()

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

root=inputLevelWise()
printTreeLevelWise(root)


