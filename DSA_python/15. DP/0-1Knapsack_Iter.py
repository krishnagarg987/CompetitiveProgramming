def knapsack(W,w,v):
    n=len(w)
    for i in range(1,n+1):
        for j in range(1,W+1):
            if j<w[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                ans1=v[i-1]+dp[i-1][j-w[i-1]]
                ans2=dp[i-1][j]
                dp[i][j]=max(ans1,ans2)
    return dp[n][W]
W=8
v=[2,3,1,4]
w=[3,4,6,5]
dp=[[0 for i in range(W+1)] for j in range(len(v)+1)]
print(knapsack(W,w,v))
print(dp)