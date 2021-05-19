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

def length(head):
    c=0
    while head.next!=None:
        c+=1
        head=head.next
    return c+1  
        
def insert(head1,position,data):
    if position>(l+1):
        return head1
    newnode=node(data)
    head=head1
    if position==1:
        newnode.next=head
        head=newnode
        return head
    else:    
        for i in range(position-2):
            head=head.next
        newnode.next=head.next
        head.next=newnode
        return head1

def printll(head):
    while head!=None:
        print(head.data,'-> ',end="")
        head=head.next
    print(None)
    
a=[1,2,3,4,5,6,7,8,-1]  
head=linkedlist(a)
printll(head)
# insert(head,position,data)
l=length(head)
head=insert(head,1,9)
printll(head)
