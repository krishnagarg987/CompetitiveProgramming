def sort_or_not(l):
    if len(l)==0 or len(l)==1:
        return True
    small_output=sort_or_not(l[1:])
    if small_output:
        if l[0]<=l[1]:
            return True
    return False
l=[0,1,2,3,4,4]
print(sort_or_not(l))
