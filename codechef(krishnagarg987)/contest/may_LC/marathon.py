for i in range(int(input())):
    D,d,A,B,C=map(int,input().split())
    total=D*d
    if total<10:
        print(0)
    if total>9 and total<21:
        print(A)
    if total>20 and total<42:
        print(B)
    if total>41:
        print(C)
