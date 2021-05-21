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

def midpoint(head):
    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow 
    
def mergeSort(head):
    if head.next==None:
        return head
    mid=midpoint(head)
    nextmid=mid.next
    mid.next=None
    nhead1=mergeSort(head)
    nhead2=mergeSort(nextmid)
    fhead=merge(nhead1,nhead2)
    return fhead

a=[6,2,4,1,6,4,7,3,4,9,2,-1]
head=linkedlist(a)
head=mergeSort(head)
printll(head)





