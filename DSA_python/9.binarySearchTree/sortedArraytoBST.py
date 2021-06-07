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

def sortedArrayToBST(a):
    length=len(a)
    if length==0:
        return None
    if length==1:
        node=Node(a[0])
        return node
    mid=a[length//2]
    rootnode=Node(mid)
    left=sortedArrayToBST(a[:(length//2)])
    right=sortedArrayToBST(a[(length//2+1):])
    rootnode.left=left
    rootnode.right=right
    return rootnode

print("enter sorted array")
a=list(map(int,input().split()))
root=sortedArrayToBST(a)
printTreeLevelWise(root)
