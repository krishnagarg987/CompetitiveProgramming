def calculate(x1,y1):
    q=1
    w=1
    for i in range(x1-1):
        w+=q
        q+=1
    q=q+1
    for i in range(y1-1):
        w+=q
        q+=1
    return [q,w]
for i in range(int(input())):
    y1,x1,y2,x2=map(int,input().split())
    a,b=calculate(x1,y1)
    c,d=calculate(x2,y2)
    sum=b
    f=b
    for i in range(y2-y1):
        f=f+a
        sum+=f
        a+=1
    a-=1
    for i in range(x2-x1):
        f=f+a
        sum+=f
        a+=1
    print(sum)
