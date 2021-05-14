def factorial(n):
    if n==1 or n==0:
        return 1
    small_output=factorial(n-1)
    return n*small_output
n=5
print(factorial(n))
