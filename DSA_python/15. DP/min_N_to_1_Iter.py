import sys
def minimum(n):
    dp[1]=0
    for i in range(2,n+1):
        ans1=dp[i-1]
        ans2=sys.maxsize
        if i/2==i//2:
            ans2=dp[i//2]
        ans3=sys.maxsize
        if i/3==i//3:
            ans3=dp[i//3]
        dp[i]=min(ans1,ans3,ans2)+1
    return dp[n]
n=30
dp=[-1 for i in range(n+1)]
print(minimum(n))
print(dp)