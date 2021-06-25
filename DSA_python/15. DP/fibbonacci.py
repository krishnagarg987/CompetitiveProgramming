n=10
dp=[-1 for i in range(n+1)]
def fibbonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if dp[n-1]==-1:
        ans1=fibbonacci(n-1)
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]
    if dp[n-2]==-1:
        ans2=fibbonacci(n-2)
        dp[n-2]=ans2
    else:
        ans2=dp[n-2]
    return ans2+ans1
print(fibbonacci(10))
print(dp)
# 0 1 1 2 3 5 8 13 21 44 55