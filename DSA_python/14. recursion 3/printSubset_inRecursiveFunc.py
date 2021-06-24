def printSubset(a,output):
    if a==[]:
        print(output)
        return
    printSubset(a[1:],output)
    printSubset(a[1:],output+[a[0]])

a=[1,2,3,4]
printSubset(a,[])


