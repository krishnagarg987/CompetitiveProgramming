import sys
def minSquareNeeded(n):
    if n==0:
        return 0
    dp[0]=0
    for i in range(1,n+1):
        j=1
        m=sys.maxsize
        while(j*j<=i):
            ans1=dp[i-j**2]
            m=min(ans1,m)
            j+=1
        dp[i]=m+1
    return dp[n]

n=41
dp=[-1 for i in range(n+1)]
print(minSquareNeeded(n))
print(dp)