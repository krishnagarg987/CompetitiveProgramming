def knapsack(W,w,v,i):
    if i==len(w):
        return 0
    if w[i]<=W:
        if dp[i+1][W]==-1:
            ans1=knapsack(W,w,v,i+1)
            dp[i+1][W]=ans1
        else:
            ans1=dp[i+1][W]
        if dp[i+1][W-w[i]]==-1:
            smallanswer=knapsack(W-w[i],w,v,i+1)
            dp[i+1][W-w[i]]=smallanswer
            ans2=v[i]+smallanswer
        else:
            ans2=dp[i+1][W-w[i]]
        ans=max(ans1,ans2)
    else:
        if dp[i + 1][W] == -1:
            ans = knapsack(W, w, v, i + 1)
            dp[i + 1][W] = ans
        else:
            ans = dp[i + 1][W]
    dp[i][W]=ans
    return dp[i][W]

W=5
v=[20,30,10]
w=[2,3,3]
dp=[[-1 for i in range(W+1)] for j in range(len(v)+1)]
print(knapsack(W,w,v,0))
print(dp)