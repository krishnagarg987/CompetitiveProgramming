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


def countNodes(root):
    if root==None:
        return 0
    c1=countNodes(root.left)
    c2=countNodes(root.right)
    return c1+c2+1

root=treeInput()
print(countNodes(root))