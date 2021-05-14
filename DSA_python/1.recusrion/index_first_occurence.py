def first_index(l,x):
    if len(l)==0:
        return -1
    if l[0] ==x:
        return 0
    small_output=first_index(l[1:],x)
    if small_output==-1:
        return -1
    else:
        return small_output+1

l=[1,2,3,4,2,1,2,4,5,8]
print( first_index(l,1))
