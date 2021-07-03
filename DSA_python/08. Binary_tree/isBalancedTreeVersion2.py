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

def isbalancedV2(root):
    if root==None:
        return (True,0)
    isleftbalanced,leftheight=isbalancedV2(root.left)
    isrightbalanced,rightHeight=isbalancedV2(root.right)
    print(root.data, isleftbalanced,isrightbalanced,leftheight,rightHeight)
    if not (isleftbalanced and isrightbalanced):
        return (False,max(leftheight,rightHeight))
    if abs(leftheight-rightHeight)>1:
        return (False,(max(leftheight,rightHeight)+1))
    else:
        return (True,(max(leftheight,rightHeight)+1))



root=treeInput()
print(isbalancedV2(root)[0])