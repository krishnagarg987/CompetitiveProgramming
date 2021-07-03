class node:
    def __init__(self,data):
        self.data=data
        self.next=None


def linkedlist(a):
    head=None
    current=None
    for i in a:
        if i==-1:
            break
        newnode=node(i)
        if head is None:
            head=newnode
            current=head
        else:
            current.next=newnode
            current=current.next
    return head


def printll(head):
    while head!=None:
        print(head.data,'-> ',end="")
        head=head.next
    print(None)
    
# a=[1,2,3,4,5,6,7,8,-1]
a=map(int,input().split())
head=linkedlist(a)
printll(head)







