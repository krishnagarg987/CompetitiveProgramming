def quick_sort(a,s,e):
    if s>=e:
        return a
    p=partition(a,s,e)
    quick_sort(a,s,p-1)
    quick_sort(a,p+1,e)

def partition(a,s,e):
    pivot=a[e]
    i=s
    pIndex=s
    
    while i<e:
        if a[i]<=pivot:
            a[i],a[pIndex]=a[pIndex],a[i]
            pIndex+=1
        i+=1
    a[pIndex],a[e]=a[e],a[pIndex]
    return pIndex

a=[10,9,2,4,6,1,7,3,5,2,8,9]
quick_sort(a,0,11)
print(a)
        
            
