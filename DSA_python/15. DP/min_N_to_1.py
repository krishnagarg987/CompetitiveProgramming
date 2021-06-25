import sys
n=30
dp=[-1 for i in range(n)]
def minimum(number):
    if number==1:
        dp[0]=0
        return dp[0]
    first=minimum(number-1)
    second=sys.maxsize
    if number/2==number//2:
        second=minimum(number//2)
    third=sys.maxsize
    if number/3==number//3:
        third = minimum(number // 3)
    dp[number-1]=min(first,second,third)+1
    return dp[number-1]

print(minimum(n))
print(dp)