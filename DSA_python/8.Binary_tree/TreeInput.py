
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

root=treeInput()
