# due to calculation of height in each loop ...it,s time complexity is in range between nlogn and n^2
# so, to reduce time complexity to n, we made version2

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

def isBalanced(root):
    if root==None:
        return True
    h1=treeHeight(root.left)
    h2=treeHeight(root.right)
    if abs(h1-h2)>1:
        return False
    isleftbalanced=isBalanced(root.left)
    isrightbalanced=isBalanced(root.right)
    if isrightbalanced and isleftbalanced:
        return True
    else:
        return False

root=treeInput()
print(isBalanced(root))
