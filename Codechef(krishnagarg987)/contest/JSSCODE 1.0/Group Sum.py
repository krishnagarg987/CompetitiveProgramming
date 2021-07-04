# 2
# 4 6
# 8 10 12
# 14 16 18 20
# 22 24 26 28 30

for i in range(int(input())):
    n=int(input())
    if n==1:
        print(2)
    else:    
        x=n*(n-1)+2
        y=n*(n+1)
        sum=0
        for i in range(x,y+1,2):
            sum+=i
        print(sum)    
