for i in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    mindist=abs(a-c)+abs(b-d)
    if k>=mindist:
        if (k-mindist)%2==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
