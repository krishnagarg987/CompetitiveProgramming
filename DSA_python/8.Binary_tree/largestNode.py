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

def largestNode(root):
    if root==None:
        return 0
    max1=largestNode(root.left)
    max2=largestNode(root.right)
    return max(root.data,max1,max2)

root=treeInput()
print(largestNode(root))