def sumtok(a,k,output):
    if len(a)==0:
        if k==0:
            print(output)
            return
        else:
            return
    sumtok(a[1:],k,output)
    o=output.copy()
    o.append(a[0])
    sumtok(a[1:],k-a[0],o)



# a=[5,3,8,7]
a=[1,2,3,4,5,6,7,8,9]
sumtok(a,15,[])
