class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.count=0

    def __printBSTHelper(self,root):
        if root==None:
            return
        print(root.data,":",end="")
        if root.left!=None:
            print("L",root.left.data,end="")
        if root.right!=None:
            print("R",root.right.data,end="")
        print()
        self.__printBSTHelper(root.left)
        self.__printBSTHelper(root.right)

    def printBST(self):
        self.__printBSTHelper(self.root)

    def __isPresentHelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True
        if root.data<data:
            return self.__isPresentHelper(root.right,data)
        if root.data>data:
            return self.__isPresentHelper(root.left,data)

    def isPresent(self,data):
        print(self.__isPresentHelper(self.root,data))

    def countNodes(self):
        print(self.count)

    def __insertHelper(self,root,data):
        if root==None:
            return Node(data)
        if root.data<=data:
            rightroot=self.__insertHelper(root.right,data)
            root.right=rightroot
        if root.data>data:
            leftroot=self.__insertHelper(root.left,data)
            root.left=leftroot
        return root

    def insert(self,data):
        newroot=self.__insertHelper(self.root,data)
        self.root=newroot
        self.count+=1

    def __min(self,root):
        if root.left==None:
            return root.data
        return self.__min(root.left)

    def __deleteHelper(self, root, data):
        if root==None:
            return False,None
        if root.data<data:
            isdeleted,newroot=self.__deleteHelper(root.right,data)
            root.right=newroot
            return isdeleted,root
        if root.data>data:
            isdeleted,newroot=self.__deleteHelper(root.left,data)
            root.left=newroot
            return isdeleted,root
        if root.data==data:
            if root.left==None and root.right==None:
                return True,None
            if root.left==None and root.right!=None:
                return True,root.right
            if root.right==None and root.left!=None:
                return True,root.left
            if root.right!=None and root.left!=None:
                replacement=self.__min(root.right)
                root.data=replacement
                isdeleted,newroot=self.__deleteHelper(root.right,replacement)
                root.right=newroot
                return True,root

    def delete(self,data):
        isdeleted,newroot=self.__deleteHelper(self.root, data)
        if isdeleted:
            self.root=newroot
        self.count-=1
        print(isdeleted)

b=BST()
b.insert(6)
b.insert(3)
b.insert(8)
b.insert(1)
b.insert(4)
b.insert(7)
b.insert(9)
b.printBST()
b.isPresent(8)
b.isPresent(11)
b.delete(8)
b.printBST()
b.delete(9)
b.printBST()
b.delete(6)
b.printBST()
b.delete(1)
b.printBST()
b.countNodes()
