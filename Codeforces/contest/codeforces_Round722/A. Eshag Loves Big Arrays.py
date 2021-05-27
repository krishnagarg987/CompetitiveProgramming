for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    mi=min(arr)
    co=arr.count(mi)
    print(len(arr)-co)
