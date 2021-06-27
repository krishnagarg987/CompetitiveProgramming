def lcs(s1,s2):
    n=len(s1)
    m=len(s2)
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    return dp[0][0]


s1 = "abd"
s2 = "bfd"
n = len(s1)
m = len(s2)
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
print(lcs(s1, s2))
print(dp)