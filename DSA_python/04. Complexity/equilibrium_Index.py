a=[8,1,5,3,7,5,2,10,5,6,3,5]
x=sum(a)
l=0
r=x-a[0]
if l==r:
    print(0)
else:    
    c=-1
    for i in range(1,len(a)):
        l+=a[i-1]
        r-=a[i]
        if l==r:
            c=i
            break
    print(c) 
