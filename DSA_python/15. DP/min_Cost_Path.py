import sys


def mincostpath(a,x1,y1,x2,y2):
    if x1==x2 and y1==y2:
        return a[x1][y1]
    ans1=ans2=ans3=sys.maxsize
    if x1+1<=x2:
        if dp[x1+1][y1]==-1:
            ans1 = mincostpath(a, x1 + 1, y1, x2, y2)
            dp[x1+1][y1]=ans1
        else:
            ans1=dp[x1+1][y1]
    if y1+1<=y2:
        if dp[x1][y1+1]==-1:
            ans2 = mincostpath(a, x1, y1+1, x2, y2)
            dp[x1][y1+1]=ans2
        else:
            ans2=dp[x1][y1+1]
    if x1+1<=x2 and y1+1<=y2:
        if dp[x1+1][y1+1]==-1:
            ans3 = mincostpath(a, x1 + 1, y1+1, x2, y2)
            dp[x1+1][y1+1]=ans3
        else:
            ans3=dp[x1+1][y1+1]
    dp[x1][y1]=min(ans1,ans2,ans3)+a[x1][y1]
    return dp[x1][y1]

a=[[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
dp=[[-1 for i in range(3)] for j in range(4)]
print(mincostpath(a,1,0,3,1))
print(dp)