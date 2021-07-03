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

def length(head):
    c=0
    while head.next!=None:
        c+=1
        head=head.next
    return c+1    
    
def midpoint(head):
    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next
    print(slow.data)    
    
a=[1,2,3,4,5,6,7,8,-1]  
head=linkedlist(a)
printll(head)
l=length(head)
midpoint(head)
