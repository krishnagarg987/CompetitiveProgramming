-----------------------------------------------------------------------------
# this 1st approach o(n^2) complexity
-----------------------------------------------------------------------------
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

def reversell(head):
    if head.next==None:
        return head
    smalloutput=reversell(head.next)
    noneNode=smalloutput
    while noneNode.next!=None:
        noneNode=noneNode.next
    noneNode.next=head
    head.next=None
    return smalloutput
    
a=[1,2,3,4,5,6,7,8,-1]  
head=linkedlist(a)
printll(head)
l=length(head)
head=reversell(head)
printll(head)



-----------------------------------------------------------------------------
# this 2nd approach o(n) complexity
-----------------------------------------------------------------------------


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

def reversell(head):
    if head.next==None:
        return [head,head]
    smallhead,smalltail=reversell(head.next)
    noneNode=smalltail
    noneNode.next=head
    head.next=None
    return [smallhead,head]
    
a=[1,2,3,4,5,6,7,8,-1]  
head=linkedlist(a)
printll(head)
l=length(head)
head,tail=reversell(head)
printll(head)
