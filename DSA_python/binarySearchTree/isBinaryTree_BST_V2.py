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

def isBinaryTree_BST(root):
    if root==None:
        return [1000000,-1000000,True]
    leftmin,leftmax,isleftBST=isBinaryTree_BST(root.left)
    rightmin,rightmax,isrightBST=isBinaryTree_BST(root.right)
    isTreeBST=True
    if leftmax>=root.data or root.data>rightmin:
        isTreeBST=False
    if not(isleftBST and isrightBST):
        isTreeBST=False
    return [min(leftmin,rightmin,root.data),max(leftmax,rightmax,root.data),isTreeBST]


root=inputLevelWise()
print(isBinaryTree_BST(root))
