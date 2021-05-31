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


def printTreeInorder(root):
    if root==None:
        return
    printTreeInorder(root.left)
    print(root.data,end=": ")
    if root.left!=None:
        print('L',root.left.data,end=',')
    if root.right!=None:
        print('R',root.right.data,end='')
    print()
    printTreeInorder(root.right)

root=treeInput()
printTreeInorder(root)
