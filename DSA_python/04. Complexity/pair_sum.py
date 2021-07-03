# pair sum
a=[-6,3,2,1,-8,6,8,-3]
y=0
# sort array and then take two pointers , 1 at start and 2nd at end 
a.sort()
i=0
j=len(a)-1
while i<j:
    if a[i]+a[j]==y:
        print(a[i],a[j])
        i+=1
        j-=1
    elif a[i]+a[j]>y:
        j-=1
    elif a[i]+a[j]<y:
        i+=1
        
