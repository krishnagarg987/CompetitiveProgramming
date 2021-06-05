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

def buildTree(inorder,preorder):
    length=len(inorder)
    if length==0:
        return None
    if length==1:
        node=Node(inorder[0])
        return node
    mid=inorder.index(preorder[0])
    leftnode=buildTree(inorder[:mid],preorder[1:(mid+1)])
    rightnode=buildTree(inorder[(mid+1):],preorder[(mid+1):])
    rootnode=Node(inorder[mid])
    rootnode.left=leftnode
    rootnode.right=rightnode
    return rootnode

inorder=list(map(int,input().split()))
preorder=list(map(int,input().split()))

root=buildTree(inorder,preorder)
printTreeLevelWise(root)