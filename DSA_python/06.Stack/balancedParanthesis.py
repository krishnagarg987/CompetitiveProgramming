from stackUsingArray import Stack
string=input()
s=Stack()
isbalanced=True
for i in string:
    if i in ['[','{','(']:
        s.push(i)
    elif i in [']','}',')']:
        if s.isEmpty():
            isbalanced=False
            break
        if s.top()=='[' and i==']':
            s.pop()
        elif i=='}' and s.top()=='{':
            s.pop()
        elif i==')' and s.top()=='(':
            s.pop()
        else:
            isbalanced=False
            break
print(isbalanced)

