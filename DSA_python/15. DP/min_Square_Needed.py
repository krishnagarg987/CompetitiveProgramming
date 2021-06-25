import sys
def minSquareNeeded(n):
    if n==0:
        return 0
    i=1
    m=sys.maxsize
    while(i*i<=n):
        x=n-(i*i)
        ans1=sys.maxsize
        if dp[x]==-1:
            ans1=minSquareNeeded(x)
            dp[x]=ans1
        else:
            ans1=dp[x]
        m=min(m,ans1)
        i+=1
    dp[n]=m+1
    return dp[n]
n=41
dp=[-1 for i in range(n+1)]
print(minSquareNeeded(n))
print(dp)