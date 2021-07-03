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

def printTreePreorder(root):
    if root==None:
        return
    print(root.data,end=": ")
    if root.left!=None:
        print('L',root.left.data,end=',')
    if root.right!=None:
        print('R',root.right.data,end='')
    print()
    printTreePreorder(root.left)
    printTreePreorder(root.right)

root=treeInput()
printTreePreorder(root)