def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
        
for i in range(int(input())):
    n=int(input())
    a=hcfnaive(100,n)
    if 100%a==0:
        print(100//a)
    else:
        print(100)
