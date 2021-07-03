# rotate array
a=[6,1,3,5,2,5,8,6,4,3,2,9,4,7,0]
rotate_by=int(input())
l=len(a)
rotate_by=rotate_by%l
# after rotate 
a=a[rotate_by:]+a[:rotate_by]
print(a)
