from stackUsingArray import Stack
s1=Stack()
inp=list(map(int,input().split()))
for i in inp:
    s1.push(i)
s2=Stack()
def reverseStack(s1,s2):
    if s1.size()==1 or s1.size()==0:
        return s1
    while s1.size()>1:
        x=s1.pop()
        s2.push(x)
    first=s1.pop()
    while s2.isEmpty() is False:
        x=s2.pop()
        s1.push(x)
    smalloutput=reverseStack(s1,s2)
    s1.push(first)
    return
reverseStack(s1,s2)
while s1.isEmpty() is False:
    print(s1.pop(),end=" ")