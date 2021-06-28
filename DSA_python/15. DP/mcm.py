import sys
def mcm(m,i,j):
    if i==j:
        return 0
    minvalue=sys.maxsize
    for k in range(i,j):
        if dp[i-1][k-1]==-1:
            ans1=mcm(m,i,k)
            dp[i-1][k-1]=ans1
        else:
            ans1=dp[i-1][k-1]
        if dp[k][j-1]==-1:
            ans2=mcm(m,k+1,j)
            dp[k][j-1]=ans2
        else:
            ans2=dp[k][j-1]
        mcost=m[i-1]*m[k]*m[j]
        currentvalue=ans1+ans2+mcost
        minvalue=min(minvalue,currentvalue)
    dp[i-1][j-1]=minvalue
    return dp[i-1][j-1]
m=[2,3,4,5,6]
n=len(m)-1
dp=[[-1 for i in range(n)] for j in range(n)]
print(mcm(m,1,4))
print(dp)