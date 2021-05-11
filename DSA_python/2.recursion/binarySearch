def binarySearch(l,s,e,x):
    if s<=e:
        mid=(s+e)//2
        if l[mid]==x:
            return mid
        elif x<l[mid]:
            e=mid-1
            return binarySearch(l,s,e,x)
        elif x>l[mid]:
            s=mid+1
            return binarySearch(l,s,e,x)
    else:
        return -1
l=[1,2,3,4,5,6,7,8,9,10]
print(binarySearch(l,0,9,10))
