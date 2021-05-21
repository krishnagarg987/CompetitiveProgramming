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

def merge(head1,head2):
    fhead=None
    ftail=None
    if head1.data<=head2.data:
        fhead=head1
        ftail=head1
        head1=head1.next
    else:
        fhead=head2
        ftail=head2
        head2=head2.next
    while head1!=None and head2!=None:
        if head1.data<=head2.data:
            ftail.next=head1
            ftail=ftail.next
            head1=head1.next
        else:
            ftail.next=head2
            ftail=ftail.next
            head2=head2.next
    if head1!=None:
        ftail.next=head1
    if head2!=None:
        ftail.next=head2
    return fhead    
            
    
        
a=[1,3,5,7,-1]
b=[2,4,5,6,8,9,-1]
head1=linkedlist(a)
head2=linkedlist(b)
printll(head1)
printll(head2)
head=merge(head1,head2)
printll(head)





