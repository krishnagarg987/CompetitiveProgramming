def permutations(s,i):
    if len(s)==1:
        output=[]
        output.append(s[0])
        return output
    output=[]
    for j in range(i):
        el=s[j]
        smalloutput=permutations(s[:j]+s[j+1:],i-1)
        for x in smalloutput:
            output.append(el+x)
    return output

print(permutations("abcd",4))