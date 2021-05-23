from itertools import accumulate
from math import ceil
for i in range(int(input())):
    G,P,X=input().split(" ",2)
    G=int(G)
    G=10-G+1
    P=int(P)
    X=list(map(int,X.split(" ")))
    X=X[::-1]
    Y=list(accumulate(X))
    min = max = 0
    prev=0
    if G==1:
        min=1
    else:
        prev=Y[G-2]
        min = (prev // P) + 1
    current=Y[G-1]
    max=ceil(current/P)
    print(min,max)



