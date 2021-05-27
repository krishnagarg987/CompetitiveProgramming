s=input()
if len(s)%2!=0:
    print(-1)
else:
    test=[]
    count=0
    for i in s:
        if i=='{':
                test.append(i)
        elif i=='}':
            if len(test)==0:
                test.append(i)
            elif test[-1]=='{':
                test.pop()
            elif test[-1]=='}':
                test.append(i)
    print(len(test)//2)