def mergesort(a):
    if len(a)==0 or len(a)==1:
        return a
    mid=len(a)//2
    x=a[:mid]
    y=a[mid:]
    mergesort(x)
    mergesort(y)
    merge(a,x,y)

def merge(a,x,y):
    b=c=0
    d=[]
    while b<len(x) and c<len(y):
        if x[b]<=y[c]:
            d.append(x[b])
            b+=1
        else:
            d.append(y[c])
            c+=1
    while b<len(x):
        d.append(x[b])
        b+=1
    while c<len(y):
        d.append(y[c])
        c+=1
    print(a,d)
    for i in range(len(a)):
        a[i]=d[i]

a=[5,9,1,7,9]
mergesort(a)
print(a)
        
        
        
            
