def countZero(n):
    if n==0:
        return 0
    a=n%10
    smalloutput=countZero(n//10)
    if a==0:
        return 1+smalloutput
    else:
        return smalloutput
n=1230340087689098
print(countZero(n))
