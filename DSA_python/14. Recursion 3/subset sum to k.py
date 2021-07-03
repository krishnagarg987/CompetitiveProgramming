def subsetSum(a,k,output):
    if len(a)>=1:
        if a[0]==k:
            o=[]
            for i in output:
                o.append(i)
            o.append(a[0])
            print(o)
            return
        if a[0]>k:
            subsetSum(a[1:],k,output)
        else:
            subsetSum(a[1:],k,output)
            o1=[]
            for i in output:
                o1.append(i)
            o1.append(a[0])
            subsetSum(a[1:],(k-a[0]),o1)
    else:
        return

# a=[5,3,8,7]
a=[1,2,3,4,5,6,7,8,9]
output=[]
subsetSum(a,15,output)