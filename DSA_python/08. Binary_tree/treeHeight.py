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


def treeHeight(root):
    if root==None:
        return 0
    h1=treeHeight(root.left)
    h2=treeHeight(root.right)
    return max(h1,h2)+1

root=treeInput()
print(treeHeight(root))