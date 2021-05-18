# given two unsorted array, find intersection of two arrays
# normal approach takes n^2 time,optimal solution is using merge sort technique
# first sort two array bcz most of the array problems are getting optimized by sorting them

a=[4,7,11,17,1,19,3,14,9]
b=[8,9,4,2,5,7,11,10,14]
a.sort()
b.sort()
c=[]
i=j=0
# merge sort technique below
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1
    else:
        c.append(a[i])
        i+=1
        j+=1
print(c)        
