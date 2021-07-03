def last_index(l,x):
    le=len(l)
    if le==0:
        return -1
    if l[le-1]==x:
        return le-1
    smalloutput=last_index(l[:-1],x)
    return smalloutput

l=[9,1,2,3,2,1,1,2,3,4]
print(last_index(l,9))
    
