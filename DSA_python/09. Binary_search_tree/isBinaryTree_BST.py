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

def minTree(root):
    if root==None:
        return 1000000
    leftmin=minTree(root.left)
    rightmin=minTree(root.right)
    return min(root.data,leftmin,rightmin)

def maxTree(root):
    if root==None:
        return -1000000
    leftmax=maxTree(root.left)
    rightmax=maxTree(root.right)
    return max(root.data,leftmax,rightmax)

def isBinaryTree_BST(root):
    if root==None:
        return True
    leftmax=maxTree(root.left)
    rightmin=minTree(root.right)
    if root.data<=leftmax or root.data>rightmin:
        return False
    isleftbst=isBinaryTree_BST(root.left)
    isrightbst=isBinaryTree_BST(root.right)
    return isleftbst and isrightbst

root=inputLevelWise()
print(isBinaryTree_BST(root))