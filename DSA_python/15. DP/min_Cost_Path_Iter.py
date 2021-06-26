import sys


def mincostpath(a,x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if i==x1 and j==y1:
                dp[i][j]=a[i][j]
                continue
            ans1=ans2=ans3=sys.maxsize
            if i-1>=x1:
                ans1=dp[i-1][j]
            if j-1>=y1:
                ans2=dp[i][j-1]
            if i-1>=x1 and j-1>=y1:
                ans3=dp[i-1][j-1]
            dp[i][j]=min(ans1,ans2,ans3)+a[i][j]
    return dp[x2][y2]

a=[[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
dp=[[-1 for i in range(3)] for j in range(4)]
print(mincostpath(a,1,0,3,1))
print(dp)