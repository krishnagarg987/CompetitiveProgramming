def replaceString(s,x,y):
    if len(s)==0:
        return s
    smalloutput=replaceString(s[1:],x,y)
    if s[0]==x:
        return y+smalloutput
    else:
        return s[0]+smalloutput

s="kbarftgbarftgsbha"
print(replaceString(s,'a','b'))
