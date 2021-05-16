for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sa=sorted(a)
    if a==sa:
        print(0)
    elif n==3:
        if a==[1,3,2]:
            print(1)
        elif a==[2,3,1]:
            print(2)
        elif a==[2,1,3]:
            print(1)
        elif a==[3,1,2]:
            print(2)
        elif a==[3,2,1]:
            print(3)
    else:
        if a[0]==1:
            print(1)
        elif a[0]!=1 and a[n-1]==n:
            print(1)
        elif a[0]!=1 and a[0]!=n and a[n-1]!=1 and a[n-1]!=n:
            print(2)
        elif a[0]==n and a[n-1]==1:
            print(3)
        elif a[0]==n and a[n-1]!=1:
            print(2)
        elif a[0]!=n and a[n-1]==1:
            print(2)
