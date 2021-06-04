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

def diameterOfTree(root):
    if root==None:
        return 0
    rootdia=treeHeight(root.left)+treeHeight(root.right)
    leftdia=diameterOfTree(root.left)
    rightdia=diameterOfTree(root.right)
    return max(rootdia,leftdia,rightdia)

root=treeInput()
print(diameterOfTree(root))
printTreePreorder(root)
