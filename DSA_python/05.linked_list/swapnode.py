# Given a linked list, i & j, swap the nodes that are present at i & j position in the LL. You need to swap the entire nodes, not just the data.
# Indexing starts from 1. You don't need to print the elements, just swap and return the head of updated LL.
# Assume i & j given will be within limits. And i can be greater than j also.
# Input format :

# Line 1 : Linked list elements (separated by space and terminated by -1)

# Line 2 : i and j (separated by space)

# Sample Input 1 :
# 3 4 5 2 6 1 9 -1
# 4 5
# Sample Output 1 :
# 3 4 5 6 2 1 9

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

def swapnode(head,i,j):
    head1=head
    head2=head
    while i>1:
        head1=head1.next
        head2=head2.next
        i-=1
        j-=1
    while j>1:
        head2=head2.next
        j-=1
    head1.data,head2.data=head2.data,head1.data
    return head

a=[6,2,4,1,6,4,7,3,4,9,2,-1]
head=linkedlist(a)
# let i<j, indexing starts with 1
head=swapnode(head,3,8) 
printll(head)
