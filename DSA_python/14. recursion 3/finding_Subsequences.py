def subsequences(a):
    if a=="":
        return [""]
    smalloutput=subsequences(a[1:])
    output=[]
    for i in smalloutput:
        output.append(i)
    for i in smalloutput:
        output.append(a[0]+i)
    return output

a="abcd"
ans=subsequences(a)
print(ans)
