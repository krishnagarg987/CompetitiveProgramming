class Node:
    def __init__(self,item):
        self.data=item
        self.left=None
        self.right=None

def treeInput():
    data=int(input())
    if data==-1:
        return
    root=Node(data)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def noOfLeafNode(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        return 1
    c1=noOfLeafNode(root.left)
    c2=noOfLeafNode(root.right)

    return c1+c2

root=treeInput()
print(noOfLeafNode(root))