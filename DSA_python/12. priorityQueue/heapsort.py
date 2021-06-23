def heapify(a,position,n):
    leftchild=position*2+1
    rightchild=position*2+2
    while leftchild<n:
        parent=position
        if a[leftchild]<a[parent]:
            parent=leftchild
        if rightchild<n and a[rightchild]<a[parent]:
            parent=rightchild
        if parent==position:
            break
        a[parent],a[position]=a[position],a[parent]
        leftchild=parent*2+1
        rightchild=parent*2+2
        position=parent

def heapsort(a):
    n=len(a)
    for i in range((len(a)//2)-1,-1,-1):
        heapify(a,i,n)
    print(a)
    for i in range(len(a)-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,0,i)
        print(a)

a=[7,2,4,1,8,3,9,4,6]
heapsort(a)
print(a)