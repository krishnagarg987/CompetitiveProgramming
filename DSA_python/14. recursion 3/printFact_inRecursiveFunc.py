def fact(n,come):
    if n==0:
        print(come)
        return
    come=come*n
    fact(n-1,come)

fact(6,1)