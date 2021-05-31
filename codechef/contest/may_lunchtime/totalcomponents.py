from itertools import accumulate
def SieveOfEratosthenes(n):
	prime = [1 for i in range(n+1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == 1):
			for i in range(p * p, n+1, p):
				prime[i] = 0
		p += 1
	return prime[2:n+1]

PRIME=SieveOfEratosthenes(10000001)
PRIME=list(accumulate(PRIME))
for i in range(int(input())):
    n=int(input())
    if n==2:
        print(1)
    elif n==3:
        print(2)
    else:
        lowerbound=(n//2)
        totalprime=PRIME[n-2]-PRIME[lowerbound-2]
        print(totalprime+1)
