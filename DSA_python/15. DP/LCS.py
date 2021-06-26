def lcs(s1,s2):
    if s1=="" or s2=="":
        return 0
    if s1[0]==s2[0]:
        ans=0
        if not dp.get(s1[1:]+s2[1:],False):
            ans=lcs(s1[1:],s2[1:])
            dp[s1[1:]+s2[1:]]=ans
        else:
            ans=dp[s1[1:]+s2[1:]]
        dp[s1+s2]=ans+1
    if s1[0]!=s2[0]:
        ans1=ans2=0
        if not dp.get(s1+s2[1:],False):
            ans1=lcs(s1, s2[1:])
            dp[s1+s2[1:]]=ans1
        else:
            ans1=dp[s1+s2[1:]]
        if not dp.get(s1[1:]+s2,False):
            ans2=lcs(s1[1:],s2)
            dp[s1[1:]+s2]=ans2
        else:
            ans2=dp[s1[1:]+s2]
        dp[s1+s2]=max(ans1,ans2)
    return dp[s1+s2]

dp={}
print(lcs("abdgec","bfdmgjc"))
print(len(dp))
