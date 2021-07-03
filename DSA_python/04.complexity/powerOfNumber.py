# find power of some number , forex x^n
# normal approach takes O(n) time
# this approach takes logn time
# let n is even
def power(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    smallpower=power(x,n//2)
    return smallpower*smallpower
 
print(power(5,4))
