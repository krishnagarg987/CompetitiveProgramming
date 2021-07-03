def minOfArray(a,min):
    if len(a)==0:
        print(min)
        return
    if len(a)==1:
        if a[0]<min:
            print(a[0])
        else:
            print(min)
        return
    m=a[-1]
    if m<min:
        minOfArray(a[:-1],m)
    else:
        minOfArray(a[:-1],min)
    return

a=[6,2,8,2,-3,4,5,6,9]
minOfArray(a,1000000)
