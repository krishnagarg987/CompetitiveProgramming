import sys
def mcm(m,i,j):
    n=len(m)-1
    for x in range(i-1,j):
        for y in range(i-1,n-x):
            if y==y+x:
                dp[y][y+x]=0
                continue
            ans1=dp[y][y+x-1]+m[y]*m[y+x]*m[y+x+1]
            ans2=dp[y+1][y+x]+m[y]*m[y+1]*m[x+y+1]
            dp[y][y+x]=min(ans1,ans2)
    return dp[i-1][j-1]

m=[2,3,4,5,6,3,7]
n=len(m)-1
dp=[[-1 for i in range(n)] for j in range(n)]
print(mcm(m,1,6))
print(dp)