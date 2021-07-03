string={
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}
def keyboard(n):
    if n==0:
        output=[]
        output.append("")
        return output
    smallnumber=n//10
    currentnumber=n%10
    smalloutput=keyboard(smallnumber)
    output=[]
    correspondstring=string[currentnumber]
    for s in correspondstring:
        for i in smalloutput:
            output.append(s+i)
    return output
print(len(keyboard(237)))