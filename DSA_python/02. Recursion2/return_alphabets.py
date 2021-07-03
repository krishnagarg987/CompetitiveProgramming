string=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def printl(a):
    answer=[]
    if len(a)==1:
        print(string[a[0]-1])
        return
    smalloutput=printl(a[1:])
    print(string[a[0]-1])
    smallstring=(a[0]*10)+a[1]
    print(string[smallstring-1])

a=[1,1,2,3]
printl(a)
