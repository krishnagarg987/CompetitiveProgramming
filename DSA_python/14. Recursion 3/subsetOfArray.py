def subset(a):
    if a==[]:
        output=[]
        output.append([])
        return output
    smalloutput=subset(a[1:])
    output=[]
    for i in smalloutput:
        output.append(i)
    for i in smalloutput:
        x=i.copy()
        x.append(a[0])
        output.append(x)
    return output



a=[1,2,3,4]
print(subset(a))