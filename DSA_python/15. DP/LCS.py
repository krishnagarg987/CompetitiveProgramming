def lcs(s1,s2,i,j):
    if i==len(s1) or j==len(s2):
        return 0
    if s1[i]==s2[j]:
        if dp[i+1][j+1]==-1:
            ans=lcs(s1,s2,i+1,j+1)
            dp[i+1][j+1]=ans
        else:
            ans=dp[i+1][j+1]
        dp[i][j]=ans+1
    else:
        if dp[i][j+1]==-1:
            ans1=lcs(s1,s2,i,j+1)
            dp[i][j+1]=ans1
        else:
            ans1=dp[i][j+1]
        if dp[i+1][j]==-1:
            ans2=lcs(s1,s2,i+1,j)
            dp[i+1][j]=ans2
        else:
            ans2=dp[i+1][j]
        dp[i][j]=max(ans1,ans2)
    return dp[i][j]

s1="abd"
s2="bfd"
n=len(s1)
m=len(s2)
dp=[[-1 for i in range(m+1)] for j in range(n+1)]
print(lcs(s1,s2,0,0))
print(dp)